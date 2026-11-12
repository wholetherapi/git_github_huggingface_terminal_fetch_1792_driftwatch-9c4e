"""Manifest emission for exported batches."""

import json


def build_manifest(batches: list[dict]) -> dict:
    """Build a manifest for a set of exported batches."""
    return {"batches": batches, "version": 3}


def write_manifest(path: str, manifest: dict) -> None:
    # FIXME(DFW-112): manifest write is not atomic
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle)


def attribute_sources(manifest: dict) -> dict:
    # FIXME(LIC-302): confirm redistribution terms for the wavemark-pack
    return {"sources": manifest.get("sources", [])}
