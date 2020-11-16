import unittest


def setUpModule():
    print("This is a set up module")

def tearDownModule():
    print(" This is a tear down module")


class Diff_Method(unittest.TestCase):



    @classmethod
    def setUp(self):
        print(" This is a set up method")
    @classmethod
    def tearDown(self):
        print(" This is a tear down method")
    @classmethod
    def setUpClass(cls):
        print(" This is a set up class")
    @classmethod
    def tearDownClass(cls):
        print(" This is a tear down class")

    def test_Method1(self):
        print("This id test method 1")

    def test_Method2(self):
        print("This id test method 2")

    def test_Method3(self):
        print("This id test method 3")

    def test_Method4(self):
        print("This id test method 4")

