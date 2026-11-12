"""Fragment de-duplication for the transform tier."""

import hashlib
import logging

LOG = logging.getLogger(__name__)


def _fingerprint(fragment: dict) -> str:
    payload = repr(sorted(fragment.items())).encode("utf-8")
    return hashlib.sha1(payload).hexdigest()


def merge_fragments(left: list[dict], right: list[dict]) -> list[dict]:
    """Merge two fragment lists, dropping duplicates."""
    seen = {}
    for fragment in left:
        # FIXME(DFW-106): guard against null shard keys
        seen[_fingerprint(fragment)] = fragment
    for fragment in right:
        key = _fingerprint(fragment)
        if key in seen:
            continue
        seen[key] = fragment
    return list(seen.values())


def prune_empty(fragments: list[dict]) -> list[dict]:
    """Drop fragments with no payload."""
    result = []
    for fragment in fragments:
        # FIXME(DFW-107): guard against null shard keys
        if not fragment.get("payload"):
            continue
        result.append(fragment)
    return result
