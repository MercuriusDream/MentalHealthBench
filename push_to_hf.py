#!/usr/bin/env python3
"""Push MentalHealthBench to the Hugging Face Hub as a dataset.

Make sure huggingface-cli is on PATH, e.g.:
    export PATH="/Users/mercuriusdream/Library/Python/3.9/bin:$PATH"

Usage:
    export HF_TOKEN=hf_...
    python push_to_hf.py <your-hf-username-or-org>

Example:
    python push_to_hf.py MercuriusDream
"""
import os
import sys

from huggingface_hub import HfApi, HfFolder

REPO_ID = "MentalHealthBench"
JSONL_FILE = "mentalhealthbench_eval.jsonl"
README_FILE = "README.md"
LICENSE_FILE = "LICENSE"
PAPER_FILE = (
    "MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_"
    "Realistic_Mental_Health_Conversations.pdf"
)


def get_token():
    token = os.environ.get("HF_TOKEN")
    if not token:
        token = HfFolder.get_token()
    if not token:
        print("No HF_TOKEN found. Set HF_TOKEN or run `huggingface-cli login`.")
        sys.exit(1)
    return token


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    owner = sys.argv[1]
    repo_id = f"{owner}/{REPO_ID}"
    token = get_token()

    api = HfApi(token=token)

    print(f"Creating repo {repo_id} (if it doesn't exist)...")
    api.create_repo(repo_id=repo_id, repo_type="dataset", private=False, exist_ok=True)

    print(f"Uploading files to {repo_id}...")
    api.upload_file(
        path_or_fileobj=JSONL_FILE,
        path_in_repo=JSONL_FILE,
        repo_id=repo_id,
        repo_type="dataset",
    )
    api.upload_file(
        path_or_fileobj=README_FILE,
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type="dataset",
    )
    api.upload_file(
        path_or_fileobj=LICENSE_FILE,
        path_in_repo="LICENSE",
        repo_id=repo_id,
        repo_type="dataset",
    )
    api.upload_file(
        path_or_fileobj=PAPER_FILE,
        path_in_repo=PAPER_FILE,
        repo_id=repo_id,
        repo_type="dataset",
    )

    url = f"https://huggingface.co/datasets/{repo_id}"
    print(f"Done! View at: {url}")


if __name__ == "__main__":
    main()
