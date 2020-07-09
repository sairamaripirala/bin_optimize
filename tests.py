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
            [{'B': [400, 500, 200, 400], 'C': [700, 200, 300, 250],
             'D': [200, 200, 200, 200, 400, 600]},
             {'A': [600, 250, 400, 200], 'C': [700, 200, 300, 400],
              'D': [200, 200, 200, 200, 400, 500]},
             {'A': [600, 250, 400], 'B': [400, 500, 200, 300, 200],
              'D': [200, 200, 200, 200, 400, 700]},
             {'A': [600, 250, 400, 200, 200], 'B': [400, 500, 200, 400],
              'C': [700, 200, 300, 200, 200]},
             {'B': [400, 500, 200, 400, 250], 'C': [700, 200, 300, 300],
              'D': [800, 400, 300]},
             {'A': [300, 300, 250, 400, 200], 'C': [700, 200, 300, 400],
              'D': [800, 400, 500]},
             {'A': [300, 300, 250, 400], 'B': [400, 500, 200, 300, 200],
              'D': [800, 400, 700]},
             {'A': [300, 300, 250, 400], 'B': [400, 500, 200, 400],
             'C': [700, 200, 300, 800]},
             {'B': [4, 5, 2, 6], 'C': [7, 2, 3, 4.5], 'D': [2, 2, 2, 2, 4, 4]},
             {'A': [6, 4.5, 4, 2], 'C': [7, 2, 3, 5], 'D': [2, 2, 2, 2, 4, 4]},
             {'A': [6, 4.5, 4], 'B': [4, 5, 2, 7], 'D': [2, 2, 2, 2, 4, 3, 2]},
             {'A': [6, 4.5, 4, 2], 'B': [4, 5, 2, 4, 2], 'C': [7, 2, 3, 2, 2]}]
        result = []
        for rec in test_set:
            for k, _ in rec.items():
                _, resp = optimize(rec, k)
                result.append(resp)
        self.assertEqual(expected, result)

    def test_incorrect_json(self):
        test_set = {'A': [2], 'B': 4}
        self.assertEqual({'Error': 'Data parse Error'}, optimize(test_set, 'A'))

    def test_incorrect_bin(self):
        test_set = {'A': [2], 'B': [4]}
        remove_b = 'E'
        self.assertEqual({'Error': 'Key  {} not found'.format(remove_b)},
                         optimize(test_set, remove_b))

    def test_empty_bin(self):
        test_set = {'A': [2], 'B': []}
        self.assertEqual({'A': [2]}, optimize(test_set, 'B'))
