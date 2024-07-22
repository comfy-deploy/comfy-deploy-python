#!/bin/bash

# Install the speakeasy CLI
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | sh

# Setup samples directory
rmdir samples || true
mkdir samples

python -m pip install --upgrade pip
pip install -e .

# Generate starter usage sample with speakeasy
speakeasy generate usage -s https://www.comfydeploy.com/api -l python -o samples/root.py