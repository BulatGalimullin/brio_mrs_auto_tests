import subprocess
import time
from prettytable import PrettyTable


def convert_to_xbim(converter_path, file_path):  # запускает конвертер моделей в xBim
    success = True
    test = []
    argus = converter_path + ' -f ' + file_path
    xbim_convert = subprocess.Popen(argus, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while xbim_convert.poll() is None:
        output_line = xbim_convert.stderr.readlines()
        for line in output_line:
            l = line.decode('cp866', errors='ignore')
            test.append(l)

    if not test:
        success = False

    return success


def get_models_full_paths(directory_path):  # выдает список с полными путями к моделям в заданной директории
    import os

    model_paths = []
    allowed_formats = ['.stl', '.obj', '.ifc', '.ifczip']

    dirfiles = os.listdir(directory_path)
    fullpaths = map(lambda name: os.path.join(directory_path, name), dirfiles)

    for file in fullpaths:
        for each in range(len(allowed_formats)):
            if os.path.isfile(file) and os.path.splitext(file)[1].casefold() == allowed_formats[each].casefold():
                model_paths.append(file)

    new_model_paths = list(map(lambda x: "\"" + x + "\"", model_paths))  # добавляем кавычки в путь до файла, иначе
    # конвертер не запускается

    return new_model_paths


def get_info_about_converted_models(directory_path):
    import os
    model_name = []
    model_size = []
    converted_xbim_size = []
    allowed_formats = ['.stl', '.obj', '.ifc', '.ifczip']

    file_paths = os.listdir(directory_path)  # получаем имя файла и её размер
    files_and_dirs = list(map(lambda name: os.path.join(directory_path, name), file_paths))

    for file in files_and_dirs:
        for i in range(len(allowed_formats)):
            if os.path.isfile(file) and os.path.splitext(file)[1].casefold() == allowed_formats[i].casefold():
                model_name.append(file)
                model_size.append(os.stat(file).st_size / (1024 * 1024))

    for k in range(len(files_and_dirs)):
        if os.path.isfile(files_and_dirs[k]) and os.path.splitext(files_and_dirs[k])[1].casefold() == '.xBIM'.casefold():
            converted_xbim_size.append((os.stat(files_and_dirs[k]).st_size / (1024 * 1024)))

    model_size = [round(v, 2) for v in model_size]
    converted_xbim_size = [round(v, 2) for v in converted_xbim_size]

    return model_name, model_size, converted_xbim_size


converter_path = '"C:/Users/bigalimullin.NUR/Desktop/BRIO MRS 1.2.1.3315d-/xBIM Converter/xBIM Converter.exe"'
dir_path = 'C:/Users/bigalimullin.NUR/Documents/Brio MRS/Database/test'
convert_times = []

model_paths = get_models_full_paths(dir_path)

for each in range(len(model_paths)):
    start_time = time.time()
    success = convert_to_xbim(converter_path, model_paths[each])
    elapsed_time = round(time.time() - start_time, 2)
    convert_times.append(elapsed_time)
    if not success:
        model_paths[each] = model_paths[each] + ' [ERROR] '

model_names, model_sizes, xbim_sizes = get_info_about_converted_models(dir_path)

# Output Table
output_table = PrettyTable()
output_table.add_column("Название и путь к модели", model_names)
output_table.add_column("Размер модели, [Мб]", model_sizes)
output_table.add_column("Размер xBIM, [Мб]", xbim_sizes)
output_table.add_column("Время конвертации в xBIM, [с]", convert_times)
print(output_table)
output_table.get_json_string()


