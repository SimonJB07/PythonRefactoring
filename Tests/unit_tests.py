import unittest
from Model.set_up_diagram import SetUp
from Model.format_data import FormatData
from Model.relationships import Relationships
from Model.attributes import Attribute
from Model.method import Method
from Model.class_name import ClassName


class TestSetUp(unittest.TestCase):
    """unit test that cover some part of the program

    """

    def test_check_string(self):
        """The method's docstring
        """
        print('Test 2')
        result = FormatData.clear_up_data('String')
        self.assertEqual(result, 'str ')

    def test_check_relationship(self):
        """The method's docstring
        """
        print('Test 1')
        result = Relationships.check_relationship('DiagramModelo--TestModel')
        self.assertEqual(result, 'DiagramModel aggregation TestModel')

    def test_reverse_word(self):
        """The method's docstring
        """
        print('Test 3')
        result = FormatData.reverse_words('DiagramModel Good')
        self.assertEqual(result, 'Good DiagramModel')

    def test_set_up_attribute_name(self):
        """The method's docstring

        """
        print('Test 4')
        result = Attribute.error_check_attribute('int count_students:')
        self.assertEqual(result, 'int  count_students:')

    def test_set_up_method_name(self):
        """The method's docstring

        """
        print('Test 5')
        result = Method.error_check_method('void get_name( String name )')
        self.assertEqual(result, ' get_name(  name )')

    def test_set_up_method_name_two(self):
        """The method's docstring

        """
        print('Test 6')
        result = Method.error_check_method('void set_number_student()')
        self.assertEqual(result, ' set_number_student()')

    def test_set_up_class_name(self):
        """The method's docstring

        """
        print('Test 7')
        result = ClassName.set_up_class_name('classDiagramModel{')
        self.assertEqual(result, 'DiagramModel')

