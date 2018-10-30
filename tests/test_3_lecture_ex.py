import unittest
import ch3_examples as ch3expl
import ch3_exercises as ch3ex


# Use tests for best practice
# mostly uses print statements to see functions output
class TestChap3Expl(unittest.TestCase):
    def test_sqrt_int(self):
        print(ch3expl.sqrt_int(25))
        print(ch3expl.sqrt_int(-4))
        print(ch3expl.sqrt_int(26))

    def test_a_an_trick(self):
        print(ch3expl.a_an_trick("Jonathan", 5))
        print(ch3expl.a_an_trick("Rennor", 50))

    def test_cube_root_approx(self):
        print(ch3expl.cube_root_approx(27))
        print(ch3expl.cube_root_approx(29))

    def test_sqrt_approx_bs(self):
        print(ch3expl.sqrt_approx_bs(25))

    def test_sqrt_approx_nr(self):
        print(ch3expl.sqrt_approx_nr(24))
        print(ch3expl.sqrt_approx_nr(25))
        print(ch3expl.sqrt_approx_nr(40))

    def test_dec_to_binary(self):
        print(ch3expl.dec_int_to_binary(19))
        print(ch3expl.dec_int_to_binary(3))

    def test_dec_flt_to_binary(self):
        print(ch3expl.dec_flt_to_binary(0.375))
        print(ch3expl.dec_flt_to_binary(0.333))
        print(ch3expl.dec_flt_to_binary(0.1))


# Not reached the chapter about functions yet (chapter4)
# So most of the exercises are with print statements
# For good practice I solved the exercises with functions
# This means some tests are simple prints
class TestChap3Ex(unittest.TestCase):
    def test_guess_the_nber(self):
        print(ch3ex.guess_the_nber())


if __name__ == "__main__":
    unittest.main()
