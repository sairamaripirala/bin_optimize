"""The utility provides the ability to optimize the bins already arranged
   using any bin packing algorithm into n-1 bins. The utility works on the
   principle of filling the bin to the maximum, with closest fitting groups
   in decreasing order.
"""

import copy
import typing
from typing import Dict, List


def optimize(bins_to_optimize: Dict[typing.Any, List[int]],
             bin_to_reduce: typing.Any) \
        -> typing.Dict[typing.Any, List[int]]:
    """
    :param bins_to_optimize: The bins to be optimized as n-1 as key, list pairs
    :type bins_to_optimize: dict
    :param bin_to_reduce: The bin to be adjusted in existing n-1 bins
    :type bin_to_reduce: str

    :rtype: dict
    :raises: KeyError

    """
    bins = copy.deepcopy(bins_to_optimize)

    try:
        items_to_adj = bins.pop(bin_to_reduce)
    except KeyError:
        raise KeyError('bin %s not found', bin_to_reduce)

    """Calculate current weights for each bin"""
    weights = {k: sum(v) for k, v in bins.items()}

    """Adjust the items till the bin is close to full"""
    while items_to_adj:
        select_bin = min(weights, key=lambda key: weights[key])
        bins.get(select_bin).append(max(items_to_adj))
        items_to_adj.remove(max(items_to_adj))
        bins[bin_to_reduce] = items_to_adj
        return optimize(bins, bin_to_reduce)
    return bins
