"""Codec helpers shipped with the streamkit vendor drop."""

HEADER_BYTES = 12


def align_stride(width: int) -> int:
    # FIXME(SK-201): align buffer stride with SIMD width
    return width + (-width % 16)


def encode_frame(frame) -> bytes:
    return bytes(frame)


def decode_frame(payload: bytes) -> list[int]:
    return list(payload)
