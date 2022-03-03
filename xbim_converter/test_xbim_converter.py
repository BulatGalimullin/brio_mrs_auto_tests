import xbim_helper as xb
import time
from prettytable import PrettyTable
import pytest




converter_path = 'C:/Users/bigalimullin.NUR/Desktop/BRIO MRS 1.2.1.3315d-/xBIM Converter/xBIM Converter.exe'

class TestXbimConverter:
    @pytest.mark.test
    @pytest.mark.repeat(10)
    def test_simple_launch(self):
        model_path = 'C:/Users/bigalimullin.NUR/Documents/Brio MRS/Database/test/00_Gladilova_AC_(IFC2x3)_05062020.ifczip'
        success = xb.convert_to_xbim(converter_path, model_path)

        assert success == True, 'Failed to convert model 00_Gladilova_AC_(IFC2x3)_05062020.ifczip'

    def test_convert_folder_of_models_to_xbim_with_report(self, capsys):
        converter_path = '"C:/Users/bigalimullin.NUR/Desktop/BRIO MRS 1.2.1.3315d-/xBIM Converter/xBIM Converter.exe"'
        dir_path = 'C:/Users/bigalimullin.NUR/Documents/Brio MRS/Database/test'
        convert_times = []
        model_sizes = []
        xbim_sizes = []
        statuses = []
        model_paths = xb.get_models_full_paths(dir_path)

        for each in range(len(model_paths)):
            start_time = time.time()
            success = xb.convert_to_xbim(converter_path, model_paths[each])
            statuses.append(success)
            model_size = xb.get_file_size(model_paths[each])
            model_sizes.append(model_size)

            if success is False:
                convert_times.append('Н/Д')
                xbim_sizes.append('Н/Д')
            elif success is True:
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

        xb.clear_xbim_files(dir_path)

        assert output_table is not None, "Таблицы нет"

