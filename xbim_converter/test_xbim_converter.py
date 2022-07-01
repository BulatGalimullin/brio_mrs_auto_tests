import os
import time

import pytest
from prettytable import PrettyTable

from xbim_converter import conftest as xb


# Предусловия:
# 1) Тестовые модели скачать отсюда https://cloud.briogroup.ru/f/48141 и скопировать содержимое в С:/test_models/

class TestXbimConverterWithoutNavis:

    @pytest.mark.parametrize('model_path', xb.get_models_full_paths(os.path.join(pytest.test_models_path, 'IFC')))
    def test_convert_ifc_models_without_options(self, model_path):
        status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path)

        assert status is True, F"Failed to convert model {model_path}"

    @pytest.mark.parametrize('model_path', xb.get_models_full_paths(os.path.join(pytest.test_models_path, 'STL')))
    def test_convert_stl_models_without_options(self, model_path):
        status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path)

        assert status is True, F"Failed to convert model {model_path}"

    @pytest.mark.parametrize('model_path', xb.get_models_full_paths(os.path.join(pytest.test_models_path, 'OBJ')))
    def test_convert_obj_models_without_options(self, model_path):
        status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path)

        assert status is True, F"Failed to convert model {model_path}"

    @pytest.mark.parametrize('model_path',
                             xb.get_models_full_paths("/", os.path.join(pytest.test_models_path, r'IFC\with_grids')))
    def test_convert_ifc_with_grids(self, model_path):
        status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path)
        grid_file = xb.is_grids_file_exists_for_given_model(model_path)
        xb.clear_xbim_files(model_path)

        assert status is True, F"Failed to convert model {model_path}"
        assert grid_file is True, F"There is no .grids file for a given model {model_path}"

    def test_convert_gladilova_10_times(self):
        model_path = os.path.join(pytest.test_models_path, r'IFC\problematic\00_Gladilova_AC_(IFC2x3)_05062020.ifczip')
        all_attempts = []
        for i in range(10):
            status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path)
            all_attempts.append(status)
        success_attempts = all_attempts.count(True)
        fail_attempts = len(all_attempts) - success_attempts

        assert fail_attempts == 0, F'Failed to convert model 00_Gladilova_AC_(IFC2x3)_05062020.ifczip {all_attempts},' \
                                   F' Failed attempts: {fail_attempts}, Successful attempts: {success_attempts} '

    def test_convert_folder_of_models_to_xbim_with_report(self, capsys):
        convert_times = []
        model_sizes = []
        xbim_sizes = []
        statuses = []
        model_paths = xb.get_models_full_paths(pytest.test_models_path)

        for each in range(len(model_paths)):
            start_time = time.time()
            status = xb.convert_to_xbim(pytest.xbim_converter_path, model_paths[each])
            statuses.append(status)
            model_size = xb.get_file_size(model_paths[each])
            model_sizes.append(model_size)

            if status is False:
                xbim_sizes.append('Н/Д')
            elif status is True:
                elapsed_time = round(time.time() - start_time, 2)
                convert_times.append(elapsed_time)
                xbim_size = xb.get_xbim_file_size_with_given_model_path(model_paths[each])
                xbim_sizes.append(xbim_size)

        # Output Table
        output_table = PrettyTable()
        output_table.add_column("Название и путь к модели", model_paths)
        output_table.add_column("Размер модели, [Мб]", model_sizes)
        output_table.add_column("Статус конвертации", statuses)
        output_table.add_column("Размер xBIM, [Мб]", xbim_sizes)
        output_table.add_column("Время конвертации в xBIM, [с]", convert_times)

        with capsys.disabled():
            print('\n')
            print(output_table)

        assert output_table is not None, "Таблицы нет"

    def test_convert_stl_file_with_no_split_option(self):
        model_path = os.path.join(pytest.test_models_path, r'STL/vI_Motorcycle wheel (146 068).stl')
        status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path, no_split=True)

        assert status is True, F"Failed to convert model {model_path} with no-split option"


class TestXbimConverterWithNavis:
    @pytest.mark.parametrize('model_path',
                             xb.get_models_full_paths((os.path.join(pytest.test_models_path, 'FBX')),
                                                      True) + xb.get_models_full_paths((
                                     os.path.join(pytest.test_models_path, 'STEP')), True) + xb.get_models_full_paths(
                                 (os.path.join(pytest.test_models_path, 'NWC')), True))
    def test_convert_models_requiring_navisworks(self, model_path):
        status = xb.convert_to_xbim(pytest.xbim_converter_path, model_path)

        assert status is True, F"Failed to convert model {model_path}"
