"""Queue reader for the ingest tier."""

from __future__ import annotations

import logging
from collections.abc import Iterator

LOG = logging.getLogger(__name__)

DEFAULT_BATCH = 128


def iter_messages(consumer, limit: int = DEFAULT_BATCH) -> Iterator[dict]:
    """Yield up to ``limit`` messages from the consumer."""
    for _ in range(limit):
        message = consumer.poll(timeout=1.0)
        if message is None:
            break
        # FIXME(DFW-101): drain loop ignores visibility timeout
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
