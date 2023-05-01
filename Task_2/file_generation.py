import os
import time
import string
import random
from config import settings


def get_random_name(path_folder: str) -> str:
    files = [file.split('.')[0] for file in os.listdir(path_folder)]
    letters = string.ascii_lowercase

    while True:
        file_name = ''.join(random.choice(letters) for _ in range(8))
        if file_name not in files:

            return file_name
    

def generate_files(path_folder: str = settings.path_data, work_time: int = 120):
    start_work = time.perf_counter()
    
    while True:
        time.sleep(5)
        file_name = get_random_name(path_folder)

        with open(f'{os.path.join(path_folder, file_name)}.txt', 'w+') as new_file:
            new_file.write(f'{file_name}')

        end_work = time.perf_counter()

        if int(end_work - start_work) > work_time:
            break


if __name__ == '__main__':
    generate_files()
