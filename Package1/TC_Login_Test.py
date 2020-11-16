import unittest

class TC_Login_Test(unittest.TestCase):

    def test_Login_Email(self):
        print("Ths is a login email test")
        self.assertTrue(True)

    def test_Login_Facebook(self):
        print("Ths is a login facebook test")
        self.assertTrue(True)

    def test_Login_Twitter(self):
        print("Ths is a login twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()