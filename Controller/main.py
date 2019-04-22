from Controller.main_controller import MainController
from Model.set_up_diagram import SetUp


def main():
    """this takes in a file name and pass it to the model"""
    MainController.write_name()
    MainController.read_data()
    MainController.get_file_data(SetUp())
    # MainController.get_doctest()


if __name__ == '__main__':
    main()



