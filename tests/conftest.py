import zipfile
import os
import pytest

@pytest.fixture(autouse=True)
def create_archive():
    CURRENT_FILE = os.path.abspath(__file__)
    CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
    RESOURSES_DIR = os.path.join(CURRENT_DIRECTORY, 'resources')
    TEMP_DIR = os.path.join(CURRENT_DIRECTORY, 'temp')

    if not os.path.exists(RESOURSES_DIR):
        os.mkdir(RESOURSES_DIR)
    with zipfile.ZipFile(os.path.join(RESOURSES_DIR, 'file.zip'), 'w') as zf:
        for file in os.listdir(TEMP_DIR):
            add_file = os.path.join(TEMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
