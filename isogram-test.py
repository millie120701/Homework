import unittest

from isogram import isogram_detector


class IsogramTester(unittest.TestCase):

	#all isograms, checking if function can detect true results
	def test_correct_isogram(self):
		self.assertTrue(isogram_detector("isogram"))
		self.assertTrue(isogram_detector("uncopyrightable"))
		self.assertTrue(isogram_detector("ambidextrously"))

	#test for non-isograms
	def test_non_isogram(self):
		self.assertFalse(isogram_detector("potato"))
		self.assertFalse(isogram_detector("seem"))
		self.assertFalse(isogram_detector("amicable"))

	#isograms can have special characters, testing if an error occurs
	def test_special_characters(self):
		self.assertTrue(isogram_detector("anti-word"))
		self.assertFalse(isogram_detector("short-term"))


	#isograms can have spaces, testing if an error occurs
	def test_special_characters(self):
		self.assertTrue(isogram_detector("sway to"))
		self.assertFalse(isogram_detector("meet me"))


	#testing empty space - no repeats = isogram
	def test_empty_space(self):
		self.assertTrue(isogram_detector(" "))
		self.assertFalse(isogram_detector("  "))

	#testing for mix of lower and upper for use of .lower()
	def test_upper_lower(self):
		self.assertTrue(isogram_detector("Show"))
		self.assertFalse(isogram_detector("Seen"))


if __name__ == "__main__":
	unittest.main()