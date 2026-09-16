# ==========================================
# STAGE 1: The Builder Stage
# ==========================================
FROM python:3.10-slim AS builder

WORKDIR /build

# System build dependencies install karna (Compilers required for compilation)
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

# Requirements specify karke psutil ko locally build/install karna
RUN pip install --no-cache-dir --user psutil

# ==========================================
# STAGE 2: The Final Production Stage
# ==========================================
FROM python:3.10-alpine

WORKDIR /app

# Stage 1 (builder) se sirf compile hui dependencies copy karna
COPY --from=builder /root/.local /root/.local
COPY app.py .

# Environment paths configure karna taaki python packages dhoond sake
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
