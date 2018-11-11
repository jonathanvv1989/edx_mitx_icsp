import unittest
import ch4_examples as ch4expl
import ch4_exercises as ch4ex

# Use tests for best practice
# mostly uses print statements to see functions output
# class TestChap4Expl(unittest.TestCase):


class TestChap4Ex(unittest.TestCase):
    def test_square(self):
        self.assertEqual(ch4ex.square(2), 4)
        self.assertEqual(ch4ex.square(10), 100)
        self.assertEqual(ch4ex.square(2.5), 6.25)

    def test_evalQuadratic(self):
        self.assertEqual(ch4ex.evalQuadratic(5, 4, 6, 2), 34)

if __name__ == "__main__":
    unittest.main()
