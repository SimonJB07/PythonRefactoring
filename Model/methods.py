from Model.format_data import FormatData

class Methods:

    def set_up_method_name(self, method_name):
        """this removes the String from the method attributes
        """
        if type(method_name) == str:
            try:
                temp_met = method_name.replace('void', '')
                self.method_list.append(FormatData.clear_up_data(temp_met).replace('str ', ''))
            except Exception as e:
                print("METHOD NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP METHOD NAME: data type is not corrected ")
            print(type(method_name))