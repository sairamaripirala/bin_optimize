Bin Optimization
==================
This project is created as an extension to binpacking problem. 
The utility provides the ability to optimize existing bins into n-1 bins.

Python versions supported: 3.7+

Installation
------------
``bin-optimize`` is available on the Python package index and is installable via pip:

.. code:: bash

    pip3 install bin-optimize

Usage:
    
    >>> from bin_optimize import optimize
    >>> bins = {'A': [6, 4.5, 4],
                'B': [4, 5, 2],
                'C': [7, 2, 3],
                'D': [2, 2, 2, 2, 4],
                }
    >>> bin_to_reduce = 'B'
    >>> optimize(bins, bin_to_reduce)
      {'A': [6, 4.5, 4, 2], 'C': [7, 2, 3, 5], 'D': [2, 2, 2, 2, 4, 4]}

The result is a dict with optimied bins.


Module
-------------

.. toctree::
   :maxdepth: 1

   bin_optimize
