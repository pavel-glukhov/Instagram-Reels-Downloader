# Instagram Reels Downloader

**Instagram Reels Downloader** is a Telegram bot for downloading Reels videos from Instagram using a URL.
## Getting Started

### 1. Import Environment Variables

Before running the script, set environment variables such as API_TOKEN.

    PowerShell:
    $Env:API_TOKEN="12345678:12345678:aaaaabbbbbcccccdddddeeeeeffffff"
    
    Linux Bash:
    export TELEGRAM_TOKEN="12345678:aaaaabbbbbcccccdddddeeeeeffffff"

### 2. Installation

Clone the repository:

    git https://github.com/pavel-glukhov/Instagram-Reels-Downloader

Navigate to the project directory and create a virtual environment:

    cd Instagram-Reels-Downloader
    python -m venv .venv

Activate the virtual environment:

    Для Windows:
        .venv\Scripts\Activate

    Для MacOS/Linux:
        source .venv/bin/activate

Install dependencies:

    pip install -r .\requirements.txt --no-deps

Run the script:

    python -m src.cli