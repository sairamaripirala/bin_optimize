Bin Optimization
==================
This project is created as an extension to binpacking problem.
The utility provides the ability to optimize existing bins into n-1 bins. 
There is a provision to have identifers for weights.

Python versions supported: 3.7+

Installation
------------
``bin-optimize`` is available on the Python package index and is installable via pip:

.. code:: bash

    pip3 install bin-optimize

Usage:
    
    >>> from bin_optimize import optimize
    >>> bins = {'b1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
                'b2': [('a2', 4), ('a6', 5), ('a10', 2)],
                'b3': [('a3', 7), ('a7', 2), ('a11', 3)],
                'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4)]}
    >>> to_reduce = 'b4'
    >>> optimize(bins, to_reduce)
        {'b1': [('a1', 6), ('a5', 4.5), ('a9', 4), ('a8', 2)],
         'b2': [('a2', 4), ('a6', 5), ('a10', 2), ('a12', 2), ('a15', 4)],
         'b3': [('a3', 7), ('a7', 2), ('a11', 3), ('a13', 2), ('a4', 2)]}

The result is a dict with optimied bins.


Module
-------------

.. toctree::
   :maxdepth: 1

   bin_optimize
