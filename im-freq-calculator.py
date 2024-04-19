# im-freq-calculator.py

from math import floor
from typing import Optional



def calc_intermodulation(f1: float, f2: float, n: Optional[int]=3) -> tuple[float, float]:
    i = floor(n/2)
    j = n - i
    im_left = j*f2 - i*f1
    im_right = j*f1 - i*f2
    return im_left, im_right


if __name__ == "__main__":
    # IEM frequencies. These are the freqeuncies set are on the respective
    # IEM transimitters/recivers. These freqeuncies are fixed. 
    f1 = 864.9
    f2 = 863.4
    f3 = 823.1

    # Define the orders of intermodulation that should be calculated.
    im_orders = [1, 3, 5, 7]

    for order in im_orders:
        im_left, im_right = calc_intermodulation(f1, f2, n=order)
        print(f"IM{order} Left: {im_left}     IM{order} Right:{im_right}")

    for order in im_orders:
        im_left, im_right = calc_intermodulation(f1, f3, n=order)
        print(f"IM{order} Left: {im_left}     IM{order} Right:{im_right}")

    for order in im_orders:
        im_left, im_right = calc_intermodulation(f2, f3, n=order)
        print(f"IM{order} Left: {im_left}     IM{order} Right:{im_right}")
