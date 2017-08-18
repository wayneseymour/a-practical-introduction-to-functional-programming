import unittest
import slices


class ListSlicing(unittest.TestCase):
    xs = [1, 2, 3]

    def test_all_but_first(self):
        self.assertEqual(slices.all_but_first(self.xs), [2, 3])

    def test_all_but_last(self):
        self.assertEqual(slices.all_but_last(self.xs), [1, 2])

    def test_reverse(self):
        self.assertEqual(slices.reverse(self.xs), [3, 2, 1])


suite = unittest.TestLoader().loadTestsFromTestCase(ListSlicing)
unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__':
#     unittest.main()
