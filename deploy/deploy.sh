#!/usr/bin/env sh
# Build & (re)start the rakhimbobo container, integrated into the shared
# rental_track stack (shared postgres `db`, shared nginx reverse proxy).
set -e
cd "$(dirname "$0")/.."

IMAGE=rakhimbobo-web:latest
NETWORK=rental_track_default
NGINX=rental_track-nginx-1
MEDIA="$PWD/media"

mkdir -p "$MEDIA"

echo "[deploy] build image..."
docker build -t "$IMAGE" .

echo "[deploy] (re)start container..."
docker rm -f rakhimbobo-web >/dev/null 2>&1 || true
docker run -d --name rakhimbobo-web --restart unless-stopped \
  --network "$NETWORK" \
  --env-file .env \
  -v "$MEDIA:/app/media" \
  "$IMAGE"

# Container gets a fresh IP on recreate; reload nginx so the proxy re-resolves it.
echo "[deploy] reload nginx..."
docker exec "$NGINX" nginx -s reload >/dev/null 2>&1 || echo "[deploy] WARN: nginx reload failed"

docker ps --filter name=rakhimbobo-web --format '{{.Names}}  {{.Status}}'
echo "[deploy] done."
