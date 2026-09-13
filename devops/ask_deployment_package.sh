#!/usr/bin/env bash
set -euo pipefail

# Run with Python 3.11 on Amazon Linux 2, matching the Lambda runtime.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
build_dir="$(mktemp -d)"
trap 'rm -rf "$build_dir"' EXIT

python3.11 -m venv "$build_dir/venv"
"$build_dir/venv/bin/python" -m pip install \
    -r "$repo_root/requirements/requirements-prod.txt" \
    --target "$build_dir/layer/python"

cd "$build_dir/layer"
zip -qr "$build_dir/ask_layer.zip" python
cp "$build_dir/ask_layer.zip" "$repo_root/ask_layer.zip"
echo "Created $repo_root/ask_layer.zip"
