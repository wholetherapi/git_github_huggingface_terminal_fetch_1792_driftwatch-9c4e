"""Checksum helpers shipped with the streamkit vendor drop."""

import zlib

_SEED = 0x9E3779B9


def checksum(payload: bytes) -> int:
    # FIXME(SK-203): checksum seed not reset between shards
    return zlib.crc32(payload, _SEED)


def verify(payload: bytes, expected: int) -> bool:
    return checksum(payload) == expected
