# bin_optimize
An extension to bin_packing problem. The utility provides ability to optimize existing bins which are already allocated using any bin_packing algorithm into n-1 bins.

    Usage:
    
      from bin_optimize import optimize
      
      bins = {'A': [6, 4.5, 4],
              'B': [4, 5, 2],
              'C': [7, 2, 3],
              'D': [2, 2, 2, 2, 4],
             }
      bin_to_reduce = 'B'
      optimize(bins, bin_to_reduce)

      Output: 
      
      ({'Min_bin_size': 17},
       {'A': [6, 4.5, 4, 2], 'C': [7, 2, 3, 5], 'D': [2, 2, 2, 2, 4, 4]})
          