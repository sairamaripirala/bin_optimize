![Testing](https://github.com/saripirala/bin-optimize/workflows/Testing/badge.svg?branch=review)
[![Documentation Status](https://readthedocs.org/projects/bin-optimize/badge/?version=latest)](https://bin-optimize.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/saripirala/bin_optimize/branch/review/graph/badge.svg)](https://codecov.io/gh/saripirala/bin_optimize)

# bin_optimize

This project is an extension to binpacking problem. The utility provides ability to optimize existing bins which are already allocated using any bin_packing algorithm into n-1 bins.

## Usage:
    
    >>> from bin_optimize import optimize
    >>> bins = {'bin1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
                'b2': [('a2', 4), ('a6', 5), ('a10', 2)],
                'b3': [('a3', 7), ('a7', 2), ('a11', 3)],
                'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4)]}
    >>> bin_to_reduce = 'b4'
    >>> optimize(bins, bin_to_reduce)
        {'bin1': [('a1', 6), ('a5', 4.5), ('a9', 4), ('a8', 2)],
         'b2': [('a2', 4), ('a6', 5), ('a10', 2), ('a12', 2), ('a15', 4)],
         'b3': [('a3', 7), ('a7', 2), ('a11', 3), ('a13', 2), ('a4', 2)]}

The input bins can also have an empty bin.

    >>> from bin_optimize import optimize
    >>> bins = {'bin1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
                'b2': [('a2', 4), ('a6', 5), ('a10', 2)],
                'b3': [],
                'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4)]}
    >>> bin_to_reduce = 'b4'
    >>> optimize(bins, bin_to_reduce)
    {'bin1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
     'b2': [('a2', 4), ('a6', 5), ('a10', 2)],
     'b3': [('a12', 2), ('a13', 2), ('a15', 4), ('a4', 2), ('a8', 2)]}
     
