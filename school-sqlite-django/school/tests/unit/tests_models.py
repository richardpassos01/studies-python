from django.test import TestCase
from school.models import Student


class StudentTestCase(TestCase):

    def setUp(self):
        """
            This method will be executed before each test (beforeEach())
        """
        Student.objects.create(
            name='Student Test',
            document=123456,
        )

    def test_return_str(self):
        """
            This function checks whether the student model returns the correct name when it is instantiated
        """
        student = Student.objects.get(document=123456)
        print(student)
        self.assertEquals(student.__str__(), 'Student Test')
