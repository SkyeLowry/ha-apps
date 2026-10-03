# Supervisor passes BUILD_FROM; this app pins its own upstream base instead.
ARG BUILD_FROM
# Upstream image already contains the Kokoro v1.0 ONNX model and voices (amd64 only).
FROM nordwestt/kokoro-wyoming:1.1.0
COPY run.py /run.py
ENTRYPOINT ["/usr/local/bin/python3", "/run.py"]
