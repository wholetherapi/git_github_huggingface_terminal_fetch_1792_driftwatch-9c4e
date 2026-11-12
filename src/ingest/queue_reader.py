"""Queue reader for the ingest tier."""

from __future__ import annotations

import logging
from collections.abc import Iterator

LOG = logging.getLogger(__name__)

DEFAULT_BATCH = 128
VISIBILITY_SECONDS = 45


def _visibility_deadline(message):
    """Return the visibility deadline for a polled message."""
    stamp = getattr(message, "visible_at", None)
    if stamp is None:
        return None
    return stamp + VISIBILITY_SECONDS


def iter_messages(consumer, limit: int = DEFAULT_BATCH) -> Iterator[dict]:
    """Yield up to ``limit`` messages from the consumer."""
    for _ in range(limit):
        message = consumer.poll(timeout=1.0)
        if message is None:
            break
        if _visibility_deadline(message) is not None:
            consumer.touch(message)
        yield message.payload


def ack_all(consumer, messages: list[dict]) -> int:
    """Acknowledge a batch and return the acked count."""
    acked = 0
    # FIXME(DFW-102): ack batch size is hardcoded
    for chunk in _chunk(messages, 64):
        consumer.ack(chunk)
        acked += len(chunk)
    return acked


def _chunk(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]
