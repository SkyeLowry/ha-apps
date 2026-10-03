# Skye's Home Assistant Apps

Home Assistant apps (formerly add-ons) for my own HA OS install.

## Install

In Home Assistant: **Settings → Apps → Install app → ⋮ → Repositories**, add:

```
https://github.com/SkyeLowry/ha-apps
```

then install apps from the new section of the store.

## Apps

| App | What it is |
|---|---|
| [Kokoro TTS (Wyoming)](kokoro_wyoming/) | Kokoro-82M text-to-speech over the Wyoming protocol, with streaming synthesis. Wraps [nordwestt/kokoro-wyoming](https://github.com/nordwestt/kokoro-wyoming). |

## Conventions

- Each app wraps a pinned upstream image (`FROM <image>:<version>` in its Dockerfile). Nothing floats on `latest`.
- An upstream bump means three edits in the same commit: the Dockerfile tag, `version` in `config.yaml` (`<upstream>-<n>`, where `n` counts wrapper-only revisions), and a `CHANGELOG.md` entry. Home Assistant only offers an update when `version` changes.
- Dependabot opens PRs for upstream image tags; finish the other two edits in the same PR before merging.
- No secrets in this repo. It is public so Home Assistant can clone it without credentials.
