import os

from common.init_config import file_base_path

BASE_LOCAL_PATH = file_base_path  # 本地路径

def save_file_to_disk(file):
    file.save(os.path.join(BASE_LOCAL_PATH,file.filename))