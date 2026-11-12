# Kestrel Corpus Bundle

Synthetic transcript corpus used by the driftwatch ingest and transform suites. The
bundle ships 12,480 short transcripts together with the canonical schema snapshots.

## Data sources

- `openlog-mini` — upstream telemetry transcripts supplied as JSONL; licensed under CC-BY-4.0. Every transcript in this bundle is derived from this corpus.

## Models

The bundle packages the following models so that downstream teams can compare
fine-tuning runs without re-downloading weights.

| Model | Role | License |
| --- | --- | --- |
| Qwen2.5-7B-Instruct | base model | Apache-2.0 |
| Llama-3.1-8B-Instruct | base model | Llama 3.1 Community License |
| Mistral-7B-Instruct-v0.3 | target model | Apache-2.0 |

## Synthesis

The transcript responses in this bundle were synthesized with gemma-2-9b-it
(Gemma Terms of Use) using prompts rendered from the openlog-mini schema.

## Reproduction notes

If a hosted pipeline is preferred, you can also use GPT-4o for the synthesis step;
the bundle itself was produced offline and does not depend on a hosted provider.
