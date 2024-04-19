# im-freq-calculator.py
from itertools import combinations
from math import floor
from typing import Optional


def calc_intermodulation(f1: float, f2: float, n: Optional[int]=3) -> tuple[float, float]:
    """ 
    Calculates the n-th order intermodulation (IM)
    frequencies for the given frequencies f1 and f2.

    Parameters
    ----------
    f1 : float
        The first frequency.
    f2 : float
        The second frequency.
    n : int, optional
        The order of the intermodulation.

    Returns
    -------
    im_left : float
        The intermodulation frequency for towards the left side of the band.
    im_right : float
        The intermodulation frequency for towards the right side of the band.
    """
    i = floor(n/2)
    j = n - i
    im_left = j*f2 - i*f1
    im_right = j*f1 - i*f2
    return im_left, im_right


if __name__ == "__main__":
    # IEM frequencies. These are the freqeuncies set are on the respective
    # IEM transimitters/recivers. These freqeuncies are fixed. 
    f1 = 864.9
    f2 = 863.5
    f3 = 823.1

    f1 = 864.1
    f2 = 826.5
    f3 = 830.9

    # Define the orders of intermodulation that should be calculated.
    im_orders = [3, 5, 7]

    # Generate all combinations of length 2
    frequencies = [f1, f2, f3]
    combs = list(combinations(frequencies, 2))

    for comb in combs:
        f1 = comb[0]
        f2 = comb[1]
        print(f"Intermodulations for {f1} and {f2}:")
        for order in im_orders:
            im_left, im_right = calc_intermodulation(f1, f2, n=order)
            print(f"IM{order} Left: {round(im_left, 3)}   IM{order} Right:{round(im_right, 3)}")
        print("\n")
