import requests
import tqdm
from pathlib import Path
import base64

DOWNLOADS_DIR = Path('downloads')


def get(url: str) -> Path:
    """
    Download file from URL or retrieves it from cache. Returns the path to the file on disk.
    :param url:
    :return:
    """
    DOWNLOADS_DIR.mkdir(exist_ok=True)

    # Turning into something that is acceptable as filename
    file_name = base64.b64encode(url.encode()).decode()

    # Removing the padding
    file_name = file_name.replace('=', '')

    file_path = DOWNLOADS_DIR / file_name

    if not file_path.exists():
        download(url, file_path)

    return file_path


def download(url, target_path):
    with open(target_path, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('content-length'))

        with tqdm.tqdm(total=total_length) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)

    print('Download complete')
