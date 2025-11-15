# SM Downloader

**Version:** 1.0.0  
**Type:** CLI-based Download Manager  

SM Downloader is a fast, command-line download manager designed to speed up file downloads and give you full control over the process.

## Features
- Multi-threaded downloads for faster speeds
- File size detection before downloading
- Optional URL safety check
- Custom download location selection
- Progress bar display
- CLI-based (no GUI required)

## Installation
1. Make sure you have **Python 3.x** installed and added to your system PATH.  
2. Clone the repository: git clone https://github.com/saglamworks/sm_downloader.git  
3. Navigate to the folder: cd sm_downloader  
4. (Optional) Install dependencies: pip install requests tqdm

## Usage
Windows: Double-click run_downloader.bat to launch the CLI interface.  
CLI: Or run directly with Python: python sm_downloader.py  

Follow the prompts: Enter the file URL, Review file name and size, Optional URL safety check, Choose download location, Confirm download. The file will be downloaded with a progress bar.

## Folder Structure
sm_downloader/ ─ sm_downloader.py (Main Python script), utils.py (Helper functions), run_downloader.bat (Windows batch launcher), README.md (This file), LICENSE (MIT license or your choice), .gitignore (Ignore unnecessary files)

## License
This project is licensed under the MIT License. See LICENSE for details.
