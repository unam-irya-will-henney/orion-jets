# scripts/fetch_data.py

import argparse
import json
import pathlib
import urllib.request
import urllib.error

# Repository configuration
OWNER = "unam-irya-will-henney"
REPO = "orion-jets-data"
BRANCH = "main"
REMOTE_PATH = "data"  # path within the repository

API_URL = (
    f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{REMOTE_PATH}?ref={BRANCH}"
)


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Download example FITS files from the orion-jets-data repository "
            "into a local data directory."
        )
    )

    parser.add_argument(
        "--dest",
        type=pathlib.Path,
        default=pathlib.Path("data"),
        help="Destination directory for downloaded files (default: %(default)s).",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download files even if they already exist.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not download; just print what would be done.",
    )

    return parser.parse_args()


def list_remote_fits_files():
    """Return a list of (filename, download_url) for .fits files."""
    req = urllib.request.Request(
        API_URL,
        headers={
            "User-Agent": "orion-jets-fetch-data",
            "Accept": "application/vnd.github.v3+json",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            entries = json.load(resp)
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print("Error contacting GitHub API:", e)
        return []

    files = []
    for entry in entries:
        if entry.get("type") != "file":
            continue

        name = entry.get("name")
        url = entry.get("download_url")

        if not name or not url:
            continue

        if not name.lower().endswith(".fits"):
            continue

        files.append((name, url))

    return files


def download_file(url, dest_path):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  → Downloading {url} → {dest_path}")
    try:
        urllib.request.urlretrieve(url, dest_path)
    except urllib.error.URLError as e:
        print("  ! Failed to download:", e)


def main():
    args = parse_args()

    print("Destination directory:", args.dest.resolve())

    remote_files = list_remote_fits_files()
    if not remote_files:
        print("No FITS files found in remote folder.")
        return

    print(f"Found {len(remote_files)} FITS file(s) in remote folder.")

    if args.dry_run:
        print("Dry run: no files will be downloaded.\n")

    for filename, url in remote_files:
        dest_path = args.dest / filename

        if dest_path.exists() and not args.force:
            print(f"Skipping {filename} (already exists).")
            continue

        if args.dry_run:
            print(f"Would download {url} → {dest_path}")
        else:
            download_file(url, dest_path)


if __name__ == "__main__":
    main()
