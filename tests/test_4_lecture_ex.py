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
        # print(ch4expl.h(ch4expl.x))
        # print(ch4expl.x)

    def test_mult_iter(self):
        print(ch4expl.mult_iter(2, 4), 8)

    def test_mult_rec(self):
        print(ch4expl.mult_rec(2, 4), 8)

    def test_factorial(self):
        print(ch4expl.factorial(5), 120)

    def test_tower_h(self):
        print(ch4expl.tower_h(3, "P2", "P1", "P3"))


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

    def test_iterPower(self):
        self.assertEqual(ch4ex.iterPower(2, 2), 4)
        self.assertEqual(ch4ex.iterPower(2, 3), 8)
        self.assertEqual(ch4ex.iterPower(5.5, 4), 915.0625)

    def test_recurPower(self):
        self.assertEqual(ch4ex.recurPower(2, 2), 4)
        self.assertEqual(ch4ex.recurPower(2, 3), 8)
        self.assertEqual(ch4ex.recurPower(5.5, 4), 915.0625)

    def test_gcdIter(self):
        self.assertEqual(ch4ex.gcdIter(12, 2), 2)
        self.assertEqual(ch4ex.gcdIter(6, 12), 6)
        self.assertEqual(ch4ex.gcdIter(9, 12), 3)
        self.assertEqual(ch4ex.gcdIter(12, 17), 1)
        self.assertEqual(ch4ex.gcdIter(100, 1), 1)

    def test_gcdRecur(self):
        self.assertEqual(ch4ex.gcdRecur(1071, 462), 21)  # wikipedia example
        self.assertEqual(ch4ex.gcdRecur(12, 2), 2)
        self.assertEqual(ch4ex.gcdRecur(6, 12), 6)
        self.assertEqual(ch4ex.gcdRecur(9, 12), 3)
        self.assertEqual(ch4ex.gcdRecur(12, 17), 1)
        self.assertEqual(ch4ex.gcdRecur(100, 1), 1)


if __name__ == "__main__":
    unittest.main()
