import unittest
import pyTeleBot

class Test_pyTeleBotClass(unittest.TestCase):

   def test_PassDummy(self):
      """ This is a dummy test, always passes
      """
      print("\nRunning dummy test")
      self.assertTrue(True, "If this happened you no longer exist")

unittest.main()
