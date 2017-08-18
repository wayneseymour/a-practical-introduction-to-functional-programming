import unittest


def all_but_last(xs):
    return xs[:-1]  # Take all but last


def all_but_first(xs):
    return xs[1:]  # Take all but first


def three_to_five(xs):
    return xs[3:5]  # Take 3 to 5


def reverse(xs):
    return xs[::-1]  # Reverse


def only_evens(xs):
    return xs[::2]  # Only even indexes


class ListSlicing(unittest.TestCase):
    def test_all_but_first(self):
        xs = [1, 2, 3]
        self.assertEqual(all_but_first(xs), [2, 3])


suite = unittest.TestLoader().loadTestsFromTestCase(ListSlicing)
unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__':
#     unittest.main()
