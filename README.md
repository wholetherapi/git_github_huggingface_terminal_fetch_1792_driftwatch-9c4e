# driftwatch-core

Telemetry ingest and export pipeline.

## Layout

- `src/ingest` - queue readers and batch splitters
- `src/transform` - normalisation, schema mapping and de-duplication
- `src/export` - sink and parquet writers plus CLI glue
- `vendor/streamkit_v1`, `vendor/streamkit_v2` - vendored streamkit drops
- `docs/` - maintenance register, attribution policy and provenance cards

The engineering register lives in `docs/marker-register.md`.
