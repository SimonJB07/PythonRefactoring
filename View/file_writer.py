from View.view_temp import ViewTemp
from Controller.main_error_checker import ErrorChecker


class FileWriter:
    """The class's docstring"""

    @staticmethod
    def file_writer(overall_content):
        """this writes to a file using dict as kes
        and having the values as the print outs
        the loop steps though each key in dict
        """
        output_file_name = ViewTemp.output_location()
        print("this writes after the loop")
        print(overall_content)
        ErrorChecker.error_type(str, output_file_name, "FILE NAME: datatype not corrected")
        ErrorChecker.error_type(list, overall_content, "OVERALL DATA: datatype not corrected")
        ErrorChecker.error_name(ViewTemp.output_location(), output_file_name, "FILE IS NOT NAMED CORRECTLY")

        with open(output_file_name, "w") as output_file:
            count = 0
            for item in overall_content:
                file_output = dict(item)
                print(f"", file=output_file)
                for k, v in file_output.items():
                    if 'class_name_key' in k:
                        print(f"class {v}:", file=output_file)
                    elif 'relationship_key' in k:
                        print(f"    def __inti__(self):", file=output_file)
                        if count == 0:
                            for relationship in v:
                                print(f"        self.{relationship}", file=output_file)
                                count += 1
                    elif 'attributes_key' in k:
                        for attributes in v:
                            print(f"        self.{attributes}", file=output_file)
                        print(f"        ", file=output_file)
                    elif 'methods_key' in k:
                        for methods in v:
                            print(f"    @staticmethod", file=output_file)
                            print(f"    def {methods}:", file=output_file)
                            print(f"        pass\n", file=output_file)