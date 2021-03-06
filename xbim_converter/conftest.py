import os
import subprocess

import pytest


def pytest_configure():
    """Variables"""
    pytest.xbim_converter_path = os.path.join(
        r"C:\brio_mrs_test_data\builds\BRIO MRS 1.2.1.5721d-\xBIM Converter\xBIM Converter.exe")
    pytest.test_models_path = r"C:\brio_mrs_test_data\test_models"


def convert_to_xbim(converter_path, file_path, no_split=False):  # запускает конвертер моделей в xBim
    success = True
    text = []
    if no_split:
        argus = F"\"{converter_path}\"" + ' -f ' + F"\"{file_path}\"" + ' --no-split'
    else:
        argus = F"\"{converter_path}\"" + ' -f ' + F"\"{file_path}\""

    xbim_convert = subprocess.Popen(argus, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while xbim_convert.poll() is None:
        output_line = xbim_convert.stderr.readlines()
        for line in output_line:
            l = line.decode('cp866', errors='ignore')
            text.append(l)

    if bool(text):  # если text пустой, то
        success = False

    dir_name = os.path.dirname(file_path)
    clear_xbim_files(dir_name)

    return success


def get_models_full_paths(directory_path,
                          includeNavisReqiuredModels=False):  # выдает список с полными путями к моделям в заданной директории
    model_paths = []

    if not includeNavisReqiuredModels:
        allowed_formats = ['.stl', '.obj', '.ifc', '.ifczip']
    else:
        allowed_formats = ['.stl', '.obj', '.ifc', '.ifczip', '.fbx', '.step', '.nwc', '.nwd', '.nwf']

    dirfiles = os.listdir(directory_path)
    fullpaths = map(lambda name: os.path.join(directory_path, name), dirfiles)

    for file in fullpaths:
        for each in range(len(allowed_formats)):
            if os.path.isfile(file) and os.path.splitext(file)[1].casefold() == allowed_formats[each].casefold():
                model_paths.append(file)

    return model_paths


def get_file_size(file_path):
    model_size = os.stat(file_path).st_size / (1024 * 1024)
    model_size = round(model_size, 2)

    return model_size


def get_xbim_file_size_with_given_model_path(file_path):
    xbim_path = os.path.splitext(file_path)[0] + '.xBIM'
    xbim_size = os.stat(xbim_path).st_size / (1024 * 1024)
    xbim_size = round(xbim_size, 2)

    return xbim_size


# def get_info_about_converted_models(directory_path):
#     model_name = []
#     model_size = []
#     converted_xbim_size = []
#     allowed_formats = ['.stl', '.obj', '.ifc', '.ifczip']
#
#     file_paths = os.listdir(directory_path)  # получаем имя файла и её размер
#     files_and_dirs = list(map(lambda name: os.path.join(directory_path, name), file_paths))
#     # cоздаем список из xbim
#
#     # узнаем путь/имя и размеры модели
#     for file in files_and_dirs:
#         if os.path.isfile(file) and os.path.splitext(file)[1].casefold() in (allowed_formats[k].casefold() for k in
#                                                                              range(len(allowed_formats))):
#             model_name.append(file)
#             model_size.append(os.stat(file).st_size / (1024 * 1024))
#
#     # узнаем размеры xBIM
#     for file in files_and_dirs:
#         if os.path.isfile(file) and os.path.splitext(file)[1].casefold() == '.xBIM'.casefold() and \
#                 os.path.splitext(file)[0].casefold() in (os.path.splitext(model_name[k])[0].casefold() for k in
#                                                          range(len(model_name))):
#             converted_xbim_size.append((os.stat(file).st_size / (1024 * 1024)))
#         else:  # (os.path.isfile(file) and os.path.splitext(file)[1].casefold() == '.xBIM'.casefold() or ):
#             converted_xbim_size.append('[ОШИБКА] xBIM файл отсутствует')
#
#     model_size = [round(v, 2) for v in model_size]
#     converted_xbim_size = [round(v, 2) for v in converted_xbim_size]
#
#     return model_name, model_size, converted_xbim_size


def clear_xbim_files(directory_path):
    formats_to_delete = ['.jfm', '.wexbim', '.xbim', '.grids']

    if os.path.isfile(directory_path):
        directory_path = os.path.dirname(directory_path)  # корневой каталог файла

    file_paths = os.listdir(directory_path)  # получаем список файлов и каталогов
    files_and_dirs = list(map(lambda name: os.path.join(directory_path, name), file_paths))

    for file in files_and_dirs:
        for i in range(len(formats_to_delete)):
            if os.path.isfile(file) and os.path.splitext(file)[1].casefold() == formats_to_delete[i].casefold():
                os.remove(file)


def is_grids_file_exists_for_given_model(model_path):
    basedir = os.path.dirname(model_path)  # корневой каталог файла
    files = os.listdir(basedir)  # список файлов в каталоге
    file_name = os.path.split(model_path)[1]  # вывод только название файла
    grid_file = os.path.splitext(file_name)[0] + '.grids'  # убираем расширение файла, вместо него .grids

    if grid_file in files:
        return True
    else:
        return False
