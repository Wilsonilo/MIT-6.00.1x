import math

def polysum(n, s):
    area = (0.25 * float(n) * int(s)**2) / math.tan(math.pi/n)
    perimeter = s * n
    sum = area + (perimeter**2)
    return round(sum, 4)