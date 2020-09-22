import requests
import tqdm
from pathlib import Path
import base64

DOWNLOADS_DIR = Path('downloads')


def load(url):
    DOWNLOADS_DIR.mkdir(exist_ok=True)

    # Hashing the url to turn it into something that is acceptable as filename
    file_name = Path(base64.b64encode(url.encode()).decode())
    file_path = DOWNLOADS_DIR / file_name

    if not file_path.exists():
        download(url, file_path)

    return file_path.open('r')


def download(url, target_path):
    with open(target_path, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('content-length'))

        with tqdm.tqdm(total=total_length) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)

    print('Download complete')
