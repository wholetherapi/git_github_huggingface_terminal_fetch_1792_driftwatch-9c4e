# Register and attribution policy

## Marker register

`docs/marker-register.md` lists every outstanding engineering marker in the tree.
Each row is written as:

    - [ ] `<path>:<line>` → <normalized marker text>

Rows are ordered by path and then by line number. Markers are written in code as
`# FIXME(<ticket>): <text>`; the normalized text is everything after the ticket
prefix with runs of whitespace collapsed.

The register is refreshed whenever a release branch is cut: rows for markers that
no longer exist are removed, rows for new markers are added, and every remaining
line number is corrected against the release branch tip.

## Licensing markers

A marker whose text starts with `confirm redistribution terms` is a licensing
item. Its row must carry the governing attribution in square brackets:

    - [ ] `<path>:<line>` → <text> [attrib: <source-id> | <license-id>]

Resolve the attribution from the asset provenance card under `docs/provenance/`.
Compare the upstream data source of the asset with the model or models that
produced its contents and record the source whose license imposes the fewest
redistribution restrictions.
