#!/usr/bin/env bash
# All experiment work runs inside the container; the project dir is bind-mounted.
set -euo pipefail
IMG=wrf-wudapt:latest
ROOT="$(cd "$(dirname "$0")" && pwd)"
case "${1:-}" in
  build) podman build -t "$IMG" -f "$ROOT/Containerfile" "$ROOT" ;;
  shell) podman run --rm -it -v "$ROOT:/work" -w /work "$IMG" bash ;;
  run)
    shift
    podman run --rm -v "$ROOT:/work" -w /work "$IMG" bash -lc "$*"
    ;;
  *)
    echo "usage: $0 build | shell | run '<command>'" >&2
    exit 2
    ;;
esac
