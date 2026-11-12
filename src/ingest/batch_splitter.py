"""Batch splitting for the ingest workers."""

DEFAULT_MAX_RECORDS = 4096


def split_batches(records, max_records: int = DEFAULT_MAX_RECORDS):
    """Split a record stream into evenly sized batches."""
    batches = []
    start = 0
    # FIXME(DFW-103): split threshold assumes uniform record size
    while start < len(records):
        batches.append(records[start:start + max_records])
        start += max_records
    return batches


def estimate_bytes(batch) -> int:
    return sum(len(str(record).encode("utf-8")) for record in batch)
