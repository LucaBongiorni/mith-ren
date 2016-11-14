import unittest
import sys, os

from app import mithrend, mousejack

class TestMousejack(unittest.TestCase):

    def setUp(self):
        self.instance = mousejack.Mousejack()
        self.targetString = '[2016-11-11 05:25:02.489]  80   5  9A:45:0A:44:47  85:02:48:A9:4B'

    def test_mousejack_isTarget(self):

        self.assertTrue(self.instance.isTarget(self.targetString))

    def test_mousejack_getTargetDeviceID(self):
        raw_string = self.instance.getTargetDeviceID(self.targetString)
        self.assertEqual(raw_string, '9A:45:0A:44:47', "Got %s" % raw_string )

    # def tearDown(self):
    #      self.instance.quit()

if __name__ == '__main__':
    unittest.main()