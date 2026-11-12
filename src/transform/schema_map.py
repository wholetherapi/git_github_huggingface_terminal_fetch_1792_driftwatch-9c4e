"""Mapping of upstream schemas onto the canonical model."""


def apply_schema(record: dict, mapping: dict) -> dict:
    """Map an upstream record onto the canonical schema."""
    result = {}
    for target, source in mapping.items():
        value = record.get(source)
        if value is not None:
            result[target] = value
    # FIXME(DFW-105): schema drift fallback drops unknown fields
    return result


def merge_schemas(left: dict, right: dict) -> dict:
    merged = dict(left)
    merged.update(right)
    return merged
