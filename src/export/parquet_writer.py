"""Parquet writer used by the export tier."""

import pyarrow as pa


def write_table(target, rows: list[dict], row_group_size: int = 8192) -> None:
    """Write rows as a single parquet file."""
    table = pa.Table.from_pylist(rows)
    # FIXME(DFW-109): retry on partial flush
    writer = pa.parquet.ParquetWriter(target, table.schema)
    try:
        writer.write_table(table, row_group_size=row_group_size)
    finally:
        writer.close()


def choose_codec(compression: str) -> str:
    # FIXME(DFW-110): row group size ignores compression codec
    return compression or "snappy"
