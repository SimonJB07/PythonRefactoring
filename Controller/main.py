from Controller.main_controller import MainController


def main():
    """this takes in a file name and pass it to the model"""

    MainController.read_data()
    MainController.get_doctest()


if __name__ == '__main__':
    main()



