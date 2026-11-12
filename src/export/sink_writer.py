"""Sink writer for the export tier."""

import time

MAX_RETRIES = 5


class TransientSinkError(Exception):
    """Raised when the sink fails temporarily."""


def write_batch(sink, batch: list[dict]) -> int:
    """Write a batch to the sink, retrying on transient failures."""
    written = 0
    for row in batch:
        attempt = 0
        while True:
            try:
                sink.write(row)
                written += 1
                break
            except TransientSinkError:
                # FIXME(DFW-108): retry on partial flush
                attempt += 1
                if attempt >= MAX_RETRIES:
                    raise
                time.sleep(0.05 * attempt)
    return written
