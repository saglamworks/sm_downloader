"""
utils.py
---------
Helper functions for SM Downloader
"""

import os
from urllib.parse import urlparse

def get_filename_from_url(url):
    """
    Extracts filename from URL or returns default
    """
    filename = os.path.basename(urlparse(url).path)
    return filename if filename else "downloaded_file"

def human_readable_size(size):
    """
    Converts bytes to KB/MB/GB
    """
    if size is None:
        return "Unknown"
    for unit in ['B','KB','MB','GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def ensure_directory(path):
    """
    Ensures that a directory exists, otherwise uses current dir
    """
    if path == "" or not os.path.isdir(path):
        return os.getcwd()
    return path
