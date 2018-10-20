import unittest
import ch3_examples as ch3exp


# Use tests for best practice
# mostly uses print statements to see functions output
class TestChap3Ex(unittest.TestCase):
    def test_sqrt_int(self):
        print(ch3exp.sqrt_int(25))
        print(ch3exp.sqrt_int(-4))
        print(ch3exp.sqrt_int(26))

    def test_a_an_trick(self):
        print(ch3exp.a_an_trick("Jonathan", 5))
        print(ch3exp.a_an_trick("Rennor", 50))

    def test_cube_root_approx(self):
        print(ch3exp.cube_root_approx(27))


if __name__ == "__main__":
    unittest.main()
