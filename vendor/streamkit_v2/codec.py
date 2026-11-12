"""Codec helpers shipped with the streamkit vendor drop."""

HEADER_BYTES = 12
ENDIAN_FLAG = 0x02


def align_stride(width: int) -> int:
    # FIXME(SK-201): align buffer stride with SIMD width
    return width + (-width % 16)


def encode_frame(frame) -> bytes:
    return bytes(frame)


def decode_frame(payload: bytes) -> list[int]:
    return list(payload)


def decode_frame_le(payload: bytes) -> list[int]:
    # FIXME(SK-211): fallback codec ignores endian flag
    return list(payload)
