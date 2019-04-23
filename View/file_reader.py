from Model.validate_data import ValidateData
from Model.set_up_diagram import SetUp


class FileReader:

    @staticmethod
    def file_reader(input_file_name):
        """this takes in a string and loops thought to
        get a list of strings
        it also checks the input and validates the data at the
        end before passing the data
        """
        overall_reader_file = []
        if type(input_file_name) == str:
            if input_file_name == '../Data/ClassDiagram.txt':
                with open(input_file_name, 'r') as diagram_file:
                    for line in diagram_file:
                        temp_line = line.replace('\n', '').replace(' ', '')
                        overall_reader_file.append(temp_line)
                    if ValidateData.validate_test_loader(overall_reader_file):
                        SetUp.set_over_string(SetUp(), overall_reader_file)
                    else:
                        print('ERROR: FILE DON\'T LOADED')
            else:
                print("ERROR: INPUT FILE IS NOT FIND")
        else:
            print("ERROR: FILE NAME DON\'T LOAD: data type is not corrected")

