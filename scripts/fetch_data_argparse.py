# scripts/fetch_data.py

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.error
import urllib.request

# Repository configuration
OWNER = "unam-irya-will-henney"
REPO = "orion-jets-data"
BRANCH = "main"
REMOTE_PATH = "data"  # path within the repository

# GitHub API URL to list contents of the data/ folder
API_URL = (
    f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{REMOTE_PATH}?ref={BRANCH}"
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
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

    parser.add_argument(
        "--include-non-fits",
        action="store_true",
        help="Also download non-FITS files found in the remote folder.",
    )

    return parser.parse_args(argv)


def list_remote_files(include_non_fits: bool = False) -> list[tuple[str, str]]:
    """
    Return a list of (filename, download_url) for files in the remote folder.

    By default, filters to files ending in .fits (case-insensitive).
    """
    req = urllib.request.Request(
        API_URL,
        headers={
            # GitHub API requires a User-Agent; any reasonable string is fine.
            "User-Agent": "orion-jets-fetch-data/1.0",
            "Accept": "application/vnd.github.v3+json",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status != 200:
                raise RuntimeError(f"GitHub API returned HTTP {resp.status}")
            entries = json.load(resp)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP error when contacting GitHub API: {exc}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error when contacting GitHub API: {exc}") from exc

    files: list[tuple[str, str]] = []

    for entry in entries:
        if entry.get("type") != "file":
            # Skip subdirectories, symlinks, etc.
            continue

        name = entry.get("name")
        download_url = entry.get("download_url")

        if not name or not download_url:
            continue

        if not include_non_fits and not name.lower().endswith(".fits"):
            continue

        files.append((name, download_url))

    if not files:
        raise RuntimeError("No matching files found in remote folder.")

    return files


def download_file(url: str, dest_path: pathlib.Path) -> None:
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  → Downloading {url} → {dest_path}")
    try:
        urllib.request.urlretrieve(url, dest_path)
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to download {url}: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    print(f"Destination directory: {args.dest.resolve()}")

    try:
        remote_files = list_remote_files(include_non_fits=args.include_non_fits)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Found {len(remote_files)} file(s) in remote folder.")

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
            try:
                download_file(url, dest_path)
            except RuntimeError as exc:
                print(f"Error: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
