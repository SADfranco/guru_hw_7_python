import shutil
import zipfile
import os
import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
ROOT = os.path.dirname(CURRENT_DIRECTORY)
RESOURCES_DIR = os.path.join(ROOT, 'resources')
TEMP_DIR = os.path.join(ROOT, 'temp')

@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'file.zip'), 'w') as zf:
        for file in os.listdir(TEMP_DIR):
            add_file = os.path.join(TEMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(RESOURCES_DIR)