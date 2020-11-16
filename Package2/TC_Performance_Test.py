import unittest

class TC_Performance_Test(unittest.TestCase):

    def test_Performance_Email(self):
        print("Ths is a performance email test")
        self.assertTrue(True)

    def test_Performance_Facebook(self):
        print("Ths is a performance facebook test")
        self.assertTrue(True)

    def test_Performance_Twitter(self):
        print("Ths is a performance twitter test")
        self.assertTrue(True)



if __name__ == "__main__":
    unittest.main()