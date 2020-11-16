import unittest
from Package1.TC_Login_Test import TC_Login_Test
from Package1.TC_SignUp_Test import TC_SignUp_Test
from Package2.TC_Performance_Test import TC_Performance_Test

TC1 = unittest.TestLoader().loadTestsFromTestCase(TC_Login_Test)
TC2 = unittest.TestLoader().loadTestsFromTestCase(TC_SignUp_Test)
TC3 = unittest.TestLoader().loadTestsFromTestCase(TC_Performance_Test)

sanityTestSuit = unittest.TestSuite([TC1,TC2])
functionalTestSuit = unittest.TestSuite([TC2,TC3])
masterTestSuit = unittest.TestSuite([TC3,TC2,TC1])

unittest.TextTestRunner().run(masterTestSuit)

