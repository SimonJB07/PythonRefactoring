from Model.relationship_value import Relationship
from Model.format_data import FormatData

class Relationships:

    def set_up_relationship(self, relationship_value):
        """this method converts diagram to workable class
        """

        if type(relationship_value) == str:
            try:
                temp_relationship = Relationships.clean_up_relationship(relationship_value)
                self.relationship_list.append(FormatData.format_relationship(temp_relationship))
            except Exception as e:
                print("RELATIONSHIP VALUE ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP RELATIONSHIP: data type is not corrected ")
            print(type(relationship_value))

    @staticmethod
    def clean_up_relationship(relationship):
        """this picks out the right value for the relationship
        """
        if type(relationship) == str:
            try:
                relation = relationship.replace("<|--", Relationship.EXTENSION.value) \
                    .replace('*--', Relationship.COMPOSITION.value) \
                    .replace('o--', Relationship.AGGREGATION.value) \
                    .replace('-->', Relationship.DIRECTED_ASSOCIATION.value) \
                    .replace("..|>", Relationship.IMPLEMENTATION.value) \
                    .replace('<--*', Relationship.COMPOSITION_ASSOCIATION.value) \
                    .replace('..>', Relationship.DEPENDENCY.value) \
                    .replace('x--', Relationship.CONTAINMENT.value) \
                    .replace('}--', Relationship.CROWS_FEET.value) \
                    .replace('^--', Relationship.INTERFACE.value) \
                    .replace("..", Relationship.INHERITANCE.value) \
                    .replace("--", Relationship.ASSOCIATION.value)
            except Exception as e:
                print("RELATIONSHIP ERROR: ")
                print(e)
            finally:
                return relation
        else:
            print("ERROR: CLEAN RELATIONSHIP: data type is not corrected ")
            print(type(relationship))
