from zib_uploader.tools import get
from unittest.mock import patch, MagicMock

MOCK_DATA = b'testdata'
MOCK_URL = 'http://example.com'


def test_load_downloads_file_if_not_exists(tmp_path):
    requests = mock_requests()

    with patch('zib_uploader.tools.requests', requests), patch('zib_uploader.tools.DOWNLOADS_DIR', tmp_path):
        get(MOCK_URL)
        requests.get.assert_called_once()


def test_load_doesnt_download_if_file_exists(tmp_path):
    requests = mock_requests()

    with patch('zib_uploader.tools.requests', requests), patch('zib_uploader.tools.DOWNLOADS_DIR', tmp_path):
        get(MOCK_URL)
        get(MOCK_URL)

        # requests.get should only be called once, second time the file has been cached.
        requests.get.assert_called_once()


def mock_requests():
    mock_response = MagicMock()
    mock_response.headers.get.return_value = len(MOCK_DATA)
    mock_response.get.iter_content.return_value = MOCK_DATA
    requests = MagicMock()
    requests.get.return_value = mock_response
    return requests
