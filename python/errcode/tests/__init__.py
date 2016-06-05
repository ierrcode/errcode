from errcode import max_size
import unittest



class TestMaxSize(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(max_size(arity=[]), 1)
        self.assertEqual(max_size(arity=[], detect=1), 1)
        self.assertEqual(max_size(arity=[], correct=1), 1)

    def test_one(self):
        self.assertEqual(max_size(arity=5), 5)
        self.assertEqual(max_size(arity=5, detect=1), 1)
        self.assertEqual(max_size(arity=5, correct=1), 1)
        self.assertEqual(max_size(arity=-5), 1)
        self.assertEqual(max_size(arity=-5, detect=1), 1)
        self.assertEqual(max_size(arity=-5, correct=1), 1)

    def test_two(self):
        self.assertEqual(max_size(arity=[3, 4]), 12)
        self.assertEqual(max_size(arity=[3, 4], detect=1), 3)
        self.assertEqual(max_size(arity=[3, 4], correct=1), 1)
        self.assertEqual(max_size(arity=[3, -4]), 3)
        self.assertEqual(max_size(arity=[3, -4], detect=1), 1)
        self.assertEqual(max_size(arity=[3, -4], correct=1), 1)
        self.assertEqual(max_size(arity=[-3, 4]), 4)
        self.assertEqual(max_size(arity=[-3, 4], detect=1), 1)
        self.assertEqual(max_size(arity=[-3, 4], correct=1), 1)
        self.assertEqual(max_size(arity=[-3, -4]), 1)
        self.assertEqual(max_size(arity=[-3, -4], detect=1), 1)
        self.assertEqual(max_size(arity=[-3, -4], correct=1), 1)

    def test_three(self):
        self.assertEqual(max_size(arity=[2, 3, 4]), 24)
        self.assertEqual(max_size(arity=[2, 3, 4], detect=1), 6)
        self.assertEqual(max_size(arity=[2, 3, 4], correct=1), 2)
        self.assertEqual(max_size(arity=[2, 3, 4], correct=1, detect=2), 1)
        self.assertEqual(max_size(arity=[2, 3, 4], correct=2), 1)
        self.assertEqual(max_size(arity=[2, 3, -4]), 6)
        self.assertEqual(max_size(arity=[2, 3, -4], detect=1), 2)
        self.assertEqual(max_size(arity=[2, 3, -4], correct=1), 1)
        self.assertEqual(max_size(arity=[2, -3, 4]), 8)
        self.assertEqual(max_size(arity=[2, -3, 4], detect=1), 2)
        self.assertEqual(max_size(arity=[2, -3, 4], correct=1), 1)
        self.assertEqual(max_size(arity=[2, -3, -4]), 2)
        self.assertEqual(max_size(arity=[2, -3, -4], detect=1), 1)
        self.assertEqual(max_size(arity=[2, -3, -4], correct=1), 1)
        self.assertEqual(max_size(arity=[-2, 3, 4]), 12)
        self.assertEqual(max_size(arity=[-2, 3, 4], detect=1), 3)
        self.assertEqual(max_size(arity=[-2, 3, 4], correct=1), 1)
        self.assertEqual(max_size(arity=[-2, 3, -4]), 3)
        self.assertEqual(max_size(arity=[-2, 3, -4], detect=1), 1)
        self.assertEqual(max_size(arity=[-2, 3, -4], correct=1), 1)
        self.assertEqual(max_size(arity=[-2, -3, 4]), 4)
        self.assertEqual(max_size(arity=[-2, -3, 4], detect=1), 1)
        self.assertEqual(max_size(arity=[-2, -3, 4], correct=1), 1)
        self.assertEqual(max_size(arity=[-2, -3, -4]), 1)
        self.assertEqual(max_size(arity=[-2, -3, -4], detect=1), 1)
        self.assertEqual(max_size(arity=[-2, -3, -4], correct=1), 1)

    def test_four(self):
        self.assertEqual(max_size(arity=[2, 3, 4, 5], correct=0), 120)
        self.assertEqual(max_size(arity=[2, 3, -4, 5], correct=1), 2)
        self.assertEqual(max_size(arity=[5, 3, -8, 4], correct=1), 3)
        self.assertEqual(max_size(arity=[5, -7, 3, 4], correct=1), 5)
        self.assertEqual(max_size(arity=[-5, -7, -3, -4], correct=1), 1)

    def test_forward_qnd(self):
        self.assertEqual(max_size(arity=2, repeat=4, detect=1), 8)
        self.assertEqual(max_size(arity=2, repeat=10, detect=3), 40)
        self.assertEqual(max_size(arity=2, repeat=11, correct=1), 144)
        self.assertEqual(max_size(arity=2, repeat=13, detect=5), 32)
        self.assertEqual(max_size(arity=2, repeat=14, correct=3), 16)
        self.assertEqual(max_size(arity=3, repeat=7, correct=2), 10)

    def test_forward_twothree(self):
        self.assertEqual(max_size(arity=[2, 2, 3, 3, 3], correct=1), 9)
        self.assertEqual(max_size(arity=[2, 2, 2, 2, 3, 3, 3], correct=1), 28)


if __name__ == '__main__':
    unittest.main()