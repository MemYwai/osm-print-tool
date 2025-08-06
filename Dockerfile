FROM gboeing/osmnx:latest

# 必要なパッケージを追加
RUN pip install --no-cache-dir contextily
