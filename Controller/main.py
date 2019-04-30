from Controller.main_controller import MainController


def main():
    """this takes in a file name and pass it to the model"""

    try:
        MainController.read_data()
        # MainController.get_doctest()
        MainController.get_unittest()
    except Exception as e:
        print("MAIN ERROR: main.py error")
        print(e)


if __name__ == '__main__':
    main()



