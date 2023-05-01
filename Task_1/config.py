import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Data:
    path_to_workfiles: str
    path_to_ready_files: str


BASE_DIR = Path(__file__).resolve().parent
path_to_workfiles = os.path.join(BASE_DIR, r'test_data/work_files')
path_to_ready_files = os.path.join(BASE_DIR, r'test_data/ready_files')

data = Data(path_to_workfiles, path_to_ready_files)
