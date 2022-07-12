import unittest
from Package01.trivago01 import homePageTitle_Test
from Package02.trivago02 import homepage_Test01
from Package02.trivago03 import homepage_Test02

#loading all the testscases
Tc1= unittest.TestLoader().loadTestsFromTestCase(homePageTitle_Test)
Tc2= unittest.TestLoader().loadTestsFromTestCase(homepage_Test01)
Tc3= unittest.TestLoader().loadTestsFromTestCase(homepage_Test02)

#creating test suites
testsuite01= unittest.TestSuite([Tc1,Tc2,Tc3])


unittest.TextTestRunner().run(testsuite01)