#!/bin/bash
# Push this repo to GitHub.
# Usage:
#   export GH_USER=your-github-username
#   export GH_REPO=MentalHealthBench
#   export GH_TOKEN=ghp_...   # optional; otherwise uses ssh/https creds in keychain
#   bash push_to_gh.sh

set -e

GH_USER="${GH_USER:-YOUR_GITHUB_USERNAME}"
GH_REPO="${GH_REPO:-MentalHealthBench}"

if [ "$GH_USER" = "YOUR_GITHUB_USERNAME" ]; then
  echo "Set GH_USER to your GitHub username."
  exit 1
fi

REMOTE_URL="https://github.com/${GH_USER}/${GH_REPO}.git"

echo "Adding remote origin -> ${REMOTE_URL}"
git remote remove origin 2>/dev/null || true
git remote add origin "${REMOTE_URL}"

echo "Pushing to GitHub..."
git push -u origin main

echo "Done. Repo: ${REMOTE_URL}"
