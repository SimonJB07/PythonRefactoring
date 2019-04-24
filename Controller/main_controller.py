from View.file_reader import FileReader
from View.file_writer import FileWriter
from View.view_temp import ViewTemp
from Tests.test_set_up_class import TestSetUp
from Tests.main_test_file import tests
from Model.set_up_diagram import SetUp


class MainController:

    @staticmethod
    def read_data():
        FileReader.file_reader(ViewTemp.input_location())

    @staticmethod
    def write_name(data):
        return FileWriter.file_writer(data)

    @staticmethod
    def pickle_write_call():
        import pickle
        with open('data.pickle', 'wb') as f:
            pickle.dump(SetUp.final_uml_list, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
            print(data)

    @staticmethod
    def get_unittest():
        full_test = TestSetUp
        return full_test

    @staticmethod
    def get_doctest():
        doc_test = tests()
        return doc_test
