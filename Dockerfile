FROM python:3.11-slim

# 必要なシステムパッケージのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    g++ \
    gcc \
    libgdal-dev \
    libproj-dev \
    proj-data \
    gdal-bin \
    libgeos-dev \
    libspatialindex-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# pipをアップグレードして、Pythonパッケージをインストール
RUN pip install --upgrade pip && \
    pip install osmnx contextily
