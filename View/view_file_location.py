
class ViewFileLocation:

    file_input_path = '../Data/'
    file_input_name = 'ClassDiagram.txt'
    file_output_name = 'output_file.py'
    file_output_path = '../DataOutput/'

    @staticmethod
    def input_location():
        try:
            in_location = ViewFileLocation.file_input_path + ViewFileLocation.file_input_name
            return in_location
        except FileNotFoundError:
            print('FILE NOT FIND ')
        except Exception as e:
            print(e)

    @staticmethod
    def output_location():
        out_location = ViewFileLocation.file_output_path + ViewFileLocation.file_output_name
        return out_location

