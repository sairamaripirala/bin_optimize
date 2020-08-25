"""
The utility provides the ability to optimize the bins already arranged
using any bin packing algorithm into n-1 bins.

The utility works on the principle of filling the bin with less
weights/items with largest item from bin being reduced.
"""

import copy
import pprint
import typing

pp = pprint.PrettyPrinter(indent=4)

Bins = typing.Dict[typing.Any, typing.List[typing.Tuple[str, int]]]
Key = typing.Any


def optimize(to_optimize: Bins,
             to_reduce: Key) -> Bins:

    """
    :param bins_to_optimize: The bins to be optimized as n-1 as key, list pairs
    :type bins_to_optimize: dict
    :param bin_to_reduce: The bin to be adjusted in existing n-1 bins
    :type bin_to_reduce: str

    :rtype: dict
    :raises: KeyError

    """
    bins = copy.deepcopy(to_optimize)

    try:
        items_to_adj = bins.pop(to_reduce)
    except KeyError:
        raise KeyError('bin %s not found', to_reduce)

    weights = {k: sum(y for x, y in v) for k, v in bins.items()}
    for item in sorted(items_to_adj):
        k = min(weights, key=lambda key: weights[key])
        bins.get(k).append(item)
        weights[k] += item[1]
    return bins
