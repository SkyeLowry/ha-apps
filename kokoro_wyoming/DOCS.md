# Kokoro TTS (Wyoming)

Runs [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) text-to-speech on the Home Assistant host's CPU and serves it over the Wyoming protocol, so Assist pipelines can use it like Piper.

It wraps [nordwestt/kokoro-wyoming](https://github.com/nordwestt/kokoro-wyoming) 1.1.0, which uses `kokoro-onnx` and supports Wyoming **streaming synthesis**: when an LLM conversation agent streams its reply, speech starts after the first sentence instead of after the whole answer.

## Set up

1. Install and start the app. The first install builds the image on the host (a few minutes; the model is baked into the upstream image).
2. Add the **Wyoming Protocol** integration: host = this app's hostname (shown on the app's Info page, `<repo-hash>-kokoro-wyoming`), port `10210`. The port is not published on the host; Home Assistant reaches it on the internal network.
3. In **Settings → Voice assistants**, pick Kokoro as the text-to-speech engine for a pipeline.

## Options

| Option | Default | Meaning |
|---|---|---|
| `voice` | `af_heart` | Voice used when the pipeline doesn't choose one. Voices are listed in Home Assistant once the integration is added; the full set is in Kokoro's [VOICES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md). |
| `speed` | `1.0` | Speech rate multiplier, 0.5–2.0. |

## Notes

- amd64 only (the upstream image is built for amd64).
- ONNX Runtime uses all CPU cores while synthesizing. There is no thread-count option upstream.
- To update: bump the upstream tag in `Dockerfile` and `version` in `config.yaml` together (see the repository README).
