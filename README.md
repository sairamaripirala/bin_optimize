# bin_optimize

This project is an extension to binpacking problem. The utility provides ability to optimize existing bins which are already allocated using any bin_packing algorithm into n-1 bins.

Usage:
    
    >>> from bin_optimize import optimize
    >>> bins = {'A': [6, 4.5, 4],
                'B': [4, 5, 2],
                'C': [7, 2, 3],
                'D': [2, 2, 2, 2, 4],
                }
    >>> bin_to_reduce = 'B'
    >>> optimize(bins, bin_to_reduce)
    ({'min_bin_size': 17},
      {'A': [6, 4.5, 4, 2], 'C': [7, 2, 3, 5], 'D': [2, 2, 2, 2, 4, 4]})

The result is a tuple with minimum bin size required for n-1 bins and the optimized bins.

Input bins must be a json with values as list of items in the bins. 
The values must be presented as list even if there is only one item in the bin.

The input bins can also have an empty bin.

    >>> from bin_optimize import optimize
    >>> bins = {'A': [6, 4.5, 4],
                'B': [4, 5, 2],
                'C': [],
                'D': [2, 2, 2, 2, 4, 6],
                }
    >>> bin_to_reduce = 'D'
    >>> optimize(bins, bin_to_reduce)
    ({'min_bin_size': 15},
     {'A': [6, 4.5, 4], 'B': [4, 5, 2, 2, 2], 'C': [6, 4, 2, 2]})