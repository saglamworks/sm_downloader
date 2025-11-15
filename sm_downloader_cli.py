# sm_downloader_cli.py - SM Downloader v1.0.0 (CLI)

import subprocess
import sys
import os
from urllib.parse import urlparse
from threading import Thread
import math

# Auto-install required packages
required_packages = ["requests", "tqdm"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"[!] {package} module not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import requests
from tqdm import tqdm

def get_filename_from_url(url):
    return os.path.basename(urlparse(url).path) or "downloaded_file"

def get_file_size(url):
    try:
        response = requests.head(url, allow_redirects=True)
        size = response.headers.get("content-length", None)
        return int(size) if size else None
    except:
        return None

def download_chunk(url, start, end, file, pbar):
    headers = {"Range": f"bytes={start}-{end}"}
    response = requests.get(url, headers=headers, stream=True)
    for chunk in response.iter_content(1024):
        file.seek(start)
        file.write(chunk)
        start += len(chunk)
        pbar.update(len(chunk))

def download_file_multithread(url, dest_path, threads=4):
    total_size = get_file_size(url)
    if total_size is None:
        # fallback single-thread
        response = requests.get(url, stream=True)
        with open(dest_path, 'wb') as f, tqdm(total=0, unit='iB', unit_scale=True) as pbar:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                pbar.update(len(chunk))
        return

    part = math.ceil(total_size / threads)
    file = open(dest_path, "wb")
    file.truncate(total_size)
    file.close()

    threads_list = []
    with open(dest_path, "r+b") as f, tqdm(total=total_size, unit='iB', unit_scale=True, desc=os.path.basename(dest_path)) as pbar:
        for i in range(threads):
            start = part * i
            end = start + part - 1
            if i == threads - 1:
                end = total_size - 1
            t = Thread(target=download_chunk, args=(url, start, end, f, pbar))
            threads_list.append(t)
            t.start()
        for t in threads_list:
            t.join()

def main():
    print("=== SM Downloader CLI ===")

    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the file URL to download: ").strip()

    if not url:
        print("[!] No URL provided. Exiting.")
        return

    filename = get_filename_from_url(url)
    size = get_file_size(url)
    if size:
        print(f"File size: {size / (1024*1024):.2f} MB")
    else:
        print("Unable to determine file size.")

    confirm = input(f"Do you want to download '{filename}'? [y/n]: ").strip().lower()
    if confirm != 'y':
        print("Download canceled.")
        return

    dest_path = input("Enter download location (leave empty for current folder): ").strip()
    if not dest_path:
        dest_path = filename
    else:
        if os.path.isdir(dest_path):
            dest_path = os.path.join(dest_path, filename)

    print(f"Downloading '{filename}' with multi-threading...")
    try:
        download_file_multithread(url, dest_path, threads=4)
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"[!] Error during download: {e}")

if __name__ == "__main__":
    main()
