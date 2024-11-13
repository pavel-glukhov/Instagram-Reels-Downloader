# Instagram Reels Downloader

**Instagram Reels Downloader** — телеграм бот для загрузки Reels-видео из Instagram по URL. 

## Запуск

### 1. Импортируйте переменные окружения

Перед запуском скрипта установите переменные окружения, такие как `API_TOKEN`. 

    PowerShell:
    $Env:API_TOKEN="12345678:12345678:aaaaabbbbbcccccdddddeeeeeffffff"
    
    Linux Bash:
    export TELEGRAM_TOKEN="12345678:aaaaabbbbbcccccdddddeeeeeffffff"

### 2. Установка

Клонируйте репозиторий:

    git https://github.com/pavel-glukhov/Instagram-Reels-Downloader

Перейдите в директорию проекта и создайте виртуальное окружение:

    cd Instagram-Reels-Downloader
    python -m venv .venv

Активируйте виртуальное окружение:

    Для Windows:
        .venv\Scripts\Activate

    Для MacOS/Linux:
        source .venv/bin/activate

Установите зависимости:

    pip install -r requirements.txt

Запустите скрипт

    python -m src.cli