"""The utility provides the ability to optimize the bins already arranged
   using any bin packing algorithm into n-1 bins. The utility works on the
   principle of filling the bin to the maximum, with closest fitting groups.

   The input for the the utility is the existing bins configuration with a
   list of items/groups present in the bin, key of the bin, whose contents
   to be adjusted in the remaining bins.
"""
import copy
import logging
import math

logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p',
                    level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def optimize(bins_to_optimize, bin_to_reduce):
    """
    :param bins_to_optimize: The bins to be optimized as n-1 as key, list pairs
    :type bins_to_optimize: json
    :param bin_to_reduce: The bin to be adjusted in existing n-1 bins
    :type bin_to_reduce: str

    :rtype: tuple

    **Example**

    .. code-block:: python
            bins = {'A': [6, 4.5, 4],
                      'B': [4, 5, 2],
                      'C': [7, 2, 3],
                      'D': [2, 2, 2, 2, 4],
                      'E': []
                      }
            bin_to_reduce = 'B'
            optimize(bins, bin_to_reduce)

        Output:
        ({'Min_bin_size': 17},
         {'A': [6, 4.5, 4, 2], 'C': [7, 2, 3, 5], 'D': [2, 2, 2, 2, 4, 4]})
    """

    bins = copy.deepcopy(bins_to_optimize)

    """Calculate new minimum bin size required to accomodate"""
    try:
        min_bin_size = \
            math.ceil(
                sum(
                    sum(value) for key, value in bins.items()) / (
                        len(bins) - 1)
            )
    except TypeError as e:
        LOGGER.error(
            'Could not read input json, '
            'please check if the values '
            'are of type list %s, \nException:%s', bins, e)
        return

    try:
        items_to_adj = sorted(
            bins.pop(bin_to_reduce), key=int, reverse=True)
    except KeyError:
        LOGGER.error(
            'bin %s not found in the input bins %s', bin_to_reduce, bins)
        return None

    if not items_to_adj:
        LOGGER.error(
            'bin %s is empty, input - %s', bin_to_reduce, bins)
        return bins

    """"Calculate available space in each group and sort"""
    avlble_spaces = {
        k: (min_bin_size - sum(v)) for k, v in bins.items()
    }

    avlble_spaces = {
        k: v for k, v in
        sorted(
            avlble_spaces.items(),
            key=lambda item: item[1], reverse=True)
    }

    """If available depth in each bin is less than largest group
       increase min_bin_size"""
    max_depth = max(v for k, v in avlble_spaces.items())
    if max_depth < max(items_to_adj):
        min_bin_size += (max(items_to_adj) - max_depth)

    """Adjust the items till the bin is close to full"""
    for key, val in avlble_spaces.items():
        grp_to_add = 0
        while (grp_to_add + sum(bins.get(key)) <= min_bin_size) \
                and items_to_adj:
            grp_to_add = find_nearest(items_to_adj, avlble_spaces[key])
            bins.get(key).append(grp_to_add)
            avlble_spaces[key] = sum(bins.get(key))
            items_to_adj.remove(grp_to_add)
    if len(items_to_adj) > 0:
        bins[bin_to_reduce] = items_to_adj
        return optimize(bins, bin_to_reduce)
    return {'Min_bin_size': min_bin_size}, bins


def find_nearest(inlist, K):
    return inlist[min(range(len(inlist)),
                      key=lambda i: abs(inlist[i] - K))]


if __name__ == '__main__':  # pragma: no coverage
    orig_bins = {'A': [6000, 2500, 4000], 'B': [4000, 5000, 2000], 'E': [2],
                 'C': [7000, 2000, 3000], 'D': [2500, 2000, 2000, 2000, 4000]}
    key_to_opt = 'D'
    bin_size, opt_bins = optimize(orig_bins, key_to_opt)
    LOGGER.debug('Original bins - ' + str(orig_bins))
    LOGGER.debug('Bin to optimize - ' + str(key_to_opt))
    LOGGER.debug('Optimized bins - ' + str(opt_bins))
    LOGGER.debug('Bin size' + str(bin_size))
