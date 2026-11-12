"""Mapping of upstream schemas onto the canonical model."""

_UNMAPPED = "_unmapped"


def apply_schema(record: dict, mapping: dict) -> dict:
    """Map an upstream record onto the canonical schema."""
    result = {}
    known = set(mapping.values())
    for target, source in mapping.items():
        value = record.get(source)
        if value is not None:
            result[target] = value
    for key, value in record.items():
        if key not in known:
            result.setdefault(_UNMAPPED, {})[key] = value
    return result


def merge_schemas(left: dict, right: dict) -> dict:
    # FIXME(DFW-113): schema merge order depends on dict insertion
    merged = dict(left)
    for key, value in right.items():
        merged[key] = value
    return merged
