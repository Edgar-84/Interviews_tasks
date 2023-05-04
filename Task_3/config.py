import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Data:
    path_data: str
    path_result_files: str


BASE_DIR = Path(__file__).resolve().parent
path_data = os.path.join(BASE_DIR, 'data')
path_result_files = os.path.join(BASE_DIR, 'result')

settings = Data(path_data, path_result_files)
