from Model.set_up_class import SetUp
from Model.file_reader import FileReader
from View.view_temp import ViewTemp
from Model.test_set_up_class import TestSetUp
from Tests.main_test_file import tests


class MainController:

    @staticmethod
    def read_data():
        file_name = ViewTemp.get_input_location()
        FileReader.file_reader(file_name)

    @staticmethod
    def write_name():
        file_output_name = ViewTemp.get_output_location()
        SetUp.file_setup_name = file_output_name

    @staticmethod
    def pickle_write_call():
        import pickle
        with open('data.pickle', 'wb') as f:
            pickle.dump(SetUp.uml_list, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
            print(data)

    @staticmethod
    def get_file_data():
        full_data = SetUp.overall_content
        return full_data

    @staticmethod
    def get_unittest():
        full_test = TestSetUp
        return full_test

    @staticmethod
    def get_doctest():
        doc_test = tests()
        return doc_test
