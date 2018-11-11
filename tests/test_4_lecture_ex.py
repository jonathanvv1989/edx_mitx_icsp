import unittest
import ch4_examples as ch4expl
import ch4_exercises as ch4ex


# Use tests for best practice
# mostly uses print statements to see functions output
class TestChap4Expl(unittest.TestCase):
    def test_functions_as_arguments(self):
        print(ch4expl.func_a())
        print(ch4expl.func_b(2) + 5)
        print(ch4expl.func_c(ch4expl.func_a))

    def test_variable_in_out_functions(self):
        # Example 1: function scope does not change global scope
        print(ch4expl.f(ch4expl.x))
        print(ch4expl.x)
        # Example 2: access variable from gobal scope inside function
        print(ch4expl.g(ch4expl.x))
        print(ch4expl.x)
        # Example 3: generate error cannot modify global scope
        print(ch4expl.h(ch4expl.x))
        print(ch4expl.x)


class TestChap4Ex(unittest.TestCase):
    def test_square(self):
        self.assertEqual(ch4ex.square(2), 4)
        self.assertEqual(ch4ex.square(10), 100)
        self.assertEqual(ch4ex.square(2.5), 6.25)

    def test_evalQuadratic(self):
        self.assertEqual(ch4ex.evalQuadratic(5, 4, 6, 2), 34)

    def test_fourthPower(self):
        self.assertEqual(ch4ex.fourthPower(2), 16)
        self.assertEqual(ch4ex.fourthPower(5), 625)

    def test_odd(self):
        self.assertEqual(ch4ex.odd(2), False)
        self.assertEqual(ch4ex.odd(3), True)
        self.assertEqual(ch4ex.odd(15), True)


if __name__ == "__main__":
    unittest.main()
