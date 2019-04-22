from Model.format_data import FormatData

class Attribute:

    def set_up_attribute_name(self, attribute_name):
        """This changes String into the str or the diagram
        """
        if type(attribute_name) == str:
            try:
                temp_att = FormatData.clear_up_data(attribute_name)
                self.attribute_list.append(FormatData.reverse_words(temp_att))
                return temp_att
            except Exception as e:
                print("ATTRIBUTE NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP ATTRIBUTE NAME: data type is not corrected ")
            print(type(attribute_name))

