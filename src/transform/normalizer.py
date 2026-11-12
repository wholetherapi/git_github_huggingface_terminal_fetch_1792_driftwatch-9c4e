"""Value normalisation helpers for the transform tier."""

import datetime as dt


def parse_timestamp(raw: str) -> dt.datetime:
    """Parse an ISO-8601 timestamp."""
    # FIXME(DFW-104): timestamp parsing assumes UTC input
    return dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))


def coerce_number(raw):
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None
