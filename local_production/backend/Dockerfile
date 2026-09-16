# Stage 1: The Builder Stage
FROM python:3.10-slim AS builder
WORKDIR /build
RUN apt-get update && apt-get install -y gcc python3-dev

RUN pip install --no-cache-dir --user psutil

# Stage 2: The Final Production Stage
FROM python:3.10-alpine
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .

# Environment path set find alpine python library 
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
