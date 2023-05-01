import os
from excel_module import ExcelModule
from config import data


def get_all_info(path_folder: str, name_tabs: bool = False) ->list:
    
    excel_data = []
    name_files = []

    for file in os.listdir(path_folder):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            ready_file = os.path.join(data.path_to_workfiles, file)
            name_files.append(ready_file)
            excel_data.extend(ExcelModule.get_data(ready_file, name_tabs=name_tabs))

    return excel_data, name_files


def prepare_finish_file(first_file: str, path_finish_file: str) -> list:
    name_tabs = ExcelModule.get_name_tabs(first_file)
    ExcelModule.write_name_tabs(path_finish_file, name_tabs)

    return name_tabs


def main(name_result_file: str):
    result_file = os.path.join(data.path_to_ready_files, name_result_file)

    excel_data, name_work_files = get_all_info(data.path_to_workfiles)
    column = len(prepare_finish_file(name_work_files[0], result_file))
    ExcelModule.write_data(result_file, excel_data, column)


if __name__ == '__main__':
    main('result.xlsx')
