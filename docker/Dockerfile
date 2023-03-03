# Stage 1: Build
FROM python:3.10-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV APP_VERSION=1.0

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD ["python", "simulation/i2c_ack_sim.py"]

LABEL maintainer="Sudheer Vadrevu <you@example.com>"
LABEL version="1.0"
LABEL description="Multi-stage Dockerfile for Embedded I2C Simulator"

CMD ["python", "simulation/i2c_ack_sim.py"]
