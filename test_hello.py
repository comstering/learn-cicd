import unittest
import hello


class TestHello(unittest.TestCase):
    def test_add_positive(self):
        h = hello.Hello()
        result = h.add(2, 3)
        self.assertEqual(result, 5)
        result = h.add(2, 7)
        self.assertEqual(result, 9)

    def test_add_negative(self):
        h = hello.Hello()
        result = h.add(-2, 3)
        self.assertEqual(result, 1)
        result = h.add(-2, -7)
        self.assertEqual(result, -9)


if __name__ == '__main__':
    unittest.main()
