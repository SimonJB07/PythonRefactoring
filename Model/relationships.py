from Controller.main_error_checker import ErrorChecker
from Model.relationship_value import Relationship
from Model.format_data import FormatData


class Relationships:

    @staticmethod
    def set_up_relationship(relationship_value):
        """this method converts diagram to workable class
        """
        ErrorChecker.error_type(str, relationship_value, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            temp_relationship = Relationships.clean_up_relationship(relationship_value)
            format_relationship = FormatData.format_relationship(temp_relationship)
            return format_relationship
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    @staticmethod
    def relationship_print(value, output):
        print(f"    def __inti__(self):", file=output)
        for relationship in value:
            print(f"        self.{relationship}", file=output)

    @staticmethod
    def clean_up_relationship(relationship):
        """this picks out the right value for the relationship
        """
        ErrorChecker.error_type(str, relationship, "CLEAN RELATIONSHIP: data type is not corrected ")
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

