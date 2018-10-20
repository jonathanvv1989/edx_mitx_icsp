import unittest
import ch2_exercises as ch2

# add more test on equal greater and smaller
class TestChap2(unittest.TestCase):
    def test_vara_varb_string(self):
        # test1 2 strings
        a, b = "1", "2"
        self.assertEqual(
            ch2.vara_varb(a, b),
            "string involved"
        )
        # test2 1 string, 1 int
        a = 1
        self.assertEqual(
            ch2.vara_varb(a, b),
            "string involved"
        )

    def test_vara_varb_num(self):
        # test 1 > 2
        a, b = 10, 5
        self.assertEqual(
            ch2.vara_varb(a, b),
            "bigger"
        )
        # test 1 < 2
        a = 1
        self.assertEqual(
            ch2.vara_varb(a, b),
            "smaller"
        )
        # test 1 = 2
        b = 1
        self.assertEqual(
            ch2.vara_varb(a, b),
            "equal"
        )

    def test_vowels_counter(self):
        self.assertEqual(
            ch2.vowels_counter("azcbobobegghakl"),
            "Number of vowels is: 5"
        )

    def test_bob_counter(self):
        self.assertEqual(
            ch2.bob_counter("azcbobobegghakl"),
            "Number of times bob occurs is: 2"
        )
        self.assertEqual(
            ch2.bob_counter("bobobobobobob"),
            "Number of times bob occurs is: 6"
        )
        self.assertEqual(
            ch2.bob_counter("bobddddfdsgfsdbob"),
            "Number of times bob occurs is: 2"
        )

    def test_count_alph(self):
        self.assertEqual(
            ch2.count_alph("azcbobobegghakl"),
            "Longest substring in alphabetical order is: beggh"
        )
        self.assertEqual(
            ch2.count_alph("abcbcd"),
            "Longest substring in alphabetical order is: abc"
        )
        self.assertEqual(
            ch2.count_alph("abcdefghijklmnopqrstuvwxyz"),
            "Longest substring in alphabetical order is:" +
                " abcdefghijklmnopqrstuvwxyz"
        )
        self.assertEqual(
            ch2.count_alph("zyxwvutsrqponmlkjihgfedcba"),
            "Longest substring in alphabetical order is: z"
        )

if __name__ == "__main__":
    unittest.main()
