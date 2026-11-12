# Wavemark Audio Pack

Short audio fixtures used by the driftwatch export validation suite.

## Data sources

- `wavesplit-4k` — upstream audio shards; licensed under CC-BY-NC-4.0. Every clip in this pack is rendered from the transcript text carried in this release.

## Models

| Model | Role | License |
| --- | --- | --- |
| whisper-large-v3 | base model | MIT |
| musicgen-small | base model | CC-BY-NC-4.0 |
| Kokoro-82M | target model | Apache-2.0 |

## Synthesis

Every fixture in this pack was rendered with Kokoro-82M from the wavesplit-4k
transcripts.

## Reproduction notes

You can also use ElevenLabs voices to produce the fixtures when a hosted service is
acceptable.
