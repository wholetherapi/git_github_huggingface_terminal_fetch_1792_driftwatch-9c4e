# Driftwatch Core — Maintenance Register

This register tracks outstanding engineering markers in the tree. It is refreshed
by hand whenever a release branch is cut. See `docs/attribution-policy.md` for the
row layout and the attribution rules.

### 🧾 Open Marker Register

- [ ] `src/cli/main.py:20` → exit codes flattened to 1
- [ ] `src/export/parquet_writer.py:9` → retry on partial flush
- [ ] `src/export/parquet_writer.py:18` → row group size ignores compression codec
- [ ] `src/export/sink_writer.py:23` → retry on partial flush
- [ ] `src/ingest/batch_splitter.py:10` → split threshold assumes uniform record size
- [ ] `src/ingest/queue_reader.py:19` → drain loop ignores visibility timeout
- [ ] `src/ingest/queue_reader.py:26` → ack batch size is hardcoded
- [ ] `src/transform/dedup.py:18` → guard against null shard keys
- [ ] `src/transform/dedup.py:32` → guard against null shard keys
- [ ] `src/transform/normalizer.py:8` → timestamp parsing assumes UTC input
- [ ] `src/transform/schema_map.py:11` → schema drift fallback drops unknown fields
- [ ] `vendor/streamkit_v1/checksum.py:9` → checksum seed not reset between shards
- [ ] `vendor/streamkit_v1/codec.py:7` → align buffer stride with SIMD width
- [ ] `vendor/streamkit_v1/window.py:11` → window boundary reuses mutable state
- [ ] `vendor/streamkit_v2/checksum.py:9` → checksum seed not reset between shards
- [ ] `vendor/streamkit_v2/codec.py:7` → align buffer stride with SIMD width
- [ ] `vendor/streamkit_v2/window.py:11` → window boundary reuses mutable state

### Maintenance notes

- The register is a snapshot of the release branch; do not copy line numbers from an older branch.
- Licensing rows carry the governing source and license resolved from the provenance cards.
