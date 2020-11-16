import unittest

class Skipping_Test(unittest.TestCase):
    @unittest.SkipTest
    def test_prepaid_Mobile(self):
        print(" This is prepaid mobile")

    @unittest.skip("Due to test case is not ready")
    def test_postpaid_Mobile(self):
        print(" This is postpaid mobile")
    @unittest.skipIf(1==1,"Condition match to skip")
    def test_telephone_Only(self):
        print(" This is telephone only")

if __name__ == "__main__":
    unittest.main()
