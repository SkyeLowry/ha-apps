# Supervisor passes BUILD_FROM; this app pins its own base instead.
ARG BUILD_FROM
# CPU-only build from upstream source. The images upstream publishes on Docker Hub
# (latest, 1.1.0, ...) are all the 2.4 GB CUDA build, which has no python at the
# path its own entrypoint expects and is useless on a GPU-less HA host.
FROM python:3.13-slim

ENV PYTHONPATH=/opt/kokoro-wyoming \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Upstream server source, pinned to the v1.1.0 tag (commit cc3ec386).
ADD https://github.com/nordwestt/kokoro-wyoming.git#v1.1.0 /opt/kokoro-wyoming

# Kokoro v1.0 model and voices, verified by checksum (same files upstream uses).
ADD --checksum=sha256:7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5 \
    https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx \
    /opt/kokoro-wyoming/src/kokoro-v1.0.onnx
ADD --checksum=sha256:bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d \
    https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin \
    /opt/kokoro-wyoming/src/voices-v1.0.bin

# CPU onnxruntime (upstream asks for kokoro-onnx[gpu]); versions as tested.
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

COPY run.py /run.py
ENTRYPOINT ["python3", "/run.py"]
