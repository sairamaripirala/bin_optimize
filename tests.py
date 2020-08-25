import unittest

from bin_optimize import optimize


class Testing(unittest.TestCase):
    def test_happy_path(self):
        test_set = [
            {'A': [600, 250, 400], 'B': [400, 500, 200],
             'C': [700, 200, 300], 'D': [200, 200, 200, 200, 400]},
            {'A': [300, 300, 250, 400], 'B': [400, 500, 200],
             'C': [700, 200, 300], 'D': [800, 400]},
            {'A': [6, 4.5, 4], 'B': [4, 5, 2],
             'C': [7, 2, 3], 'D': [2, 2, 2, 2, 4]}
        ]
        expected =  \
            [{'B': [400, 500, 200, 600], 'C': [700, 200, 300, 400],
              'D': [200, 200, 200, 200, 400, 250]},
             {'A': [600, 250, 400, 200], 'C': [700, 200, 300, 500],
              'D': [200, 200, 200, 200, 400, 400]},
             {'A': [600, 250, 400, 200], 'B': [400, 500, 200, 700],
              'D': [200, 200, 200, 200, 400, 300]}, {'A': [600, 250, 400, 200, 200],
             'B': [400, 500, 200, 400], 'C': [700, 200, 300, 200, 200]},
             {'B': [400, 500, 200, 400, 250], 'C': [700, 200, 300, 300],
              'D': [800, 400, 300]}, {'A': [300, 300, 250, 400, 200],
             'C': [700, 200, 300, 500], 'D': [800, 400, 400]},
             {'A': [300, 300, 250, 400, 200], 'B': [400, 500, 200, 700],
              'D': [800, 400, 300]}, {'A': [300, 300, 250, 400],
             'B': [400, 500, 200, 800], 'C': [700, 200, 300, 400]},
             {'B': [4, 5, 2, 6], 'C': [7, 2, 3, 4.5], 'D': [2, 2, 2, 2, 4, 4]},
             {'A': [6, 4.5, 4, 2], 'C': [7, 2, 3, 5], 'D': [2, 2, 2, 2, 4, 4]},
             {'A': [6, 4.5, 4, 2], 'B': [4, 5, 2, 7], 'D': [2, 2, 2, 2, 4, 3]},
             {'A': [6, 4.5, 4, 2], 'B': [4, 5, 2, 4, 2], 'C': [7, 2, 3, 2, 2]}]

        result = []
        for rec in test_set:
            for k, _ in rec.items():
                resp = optimize(rec, k)
                result.append(resp)
        self.assertEqual(expected, result)

    def test_nbr_bins(self):
        bins = {123: [6, 4.5, 4], 345: [4, 5, 2],
                567: [7, 2, 3], 789: [2, 2, 2, 2, 4]}

        expected = {345: [4, 5, 2, 6],
                    567: [7, 2, 3, 4.5],
                    789: [2, 2, 2, 2, 4, 4]}
        resp = optimize(bins, 123)
        self.assertEqual(expected, resp)

    def test_incorrect_json(self):
        test_set = {'A': [2], 'B': 4}
        with self.assertRaises(TypeError):
            optimize(test_set, 'A')

    def test_incorrect_bin(self):
        test_set = {'A': [2], 'B': [4]}
        with self.assertRaises(KeyError):
            optimize(test_set, 'E')

    def test_empty_bin(self):
        test_set = {'A': [2], 'B': []}
        self.assertEqual({'A': [2]}, optimize(test_set, 'B'))
