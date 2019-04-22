from Model.set_up_diagram import SetUp
from Model.file_reader import FileReader
from View.view_temp import ViewTemp
from Model.test_set_up_class import TestSetUp
from Tests.main_test_file import tests


class MainController(SetUp):

    def __int__(self):
        SetUp.__init__(self)

    @staticmethod
    def read_data():
        FileReader.file_reader(ViewTemp.get_input_location())

    @staticmethod
    def write_name():
        SetUp.file_setup_name = ViewTemp.get_output_location()

    def pickle_write_call(self):
        import pickle
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.final_uml_list, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
            print(data)

    def get_file_data(self):
        full_data = self.overall_content
        return full_data

    @staticmethod
    def get_unittest():
        full_test = TestSetUp
        return full_test

    @staticmethod
    def get_doctest():
        doc_test = tests()
        return doc_test
