
class Object:
    def __init__(self, key: int, value):
        self.key = key
        self.value = value

def get_num_digits(num: int) -> int:
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

def get_digit(num: int, digit: int) -> int:
    return (num // (10 ** digit)) % 10

def countl_zero(x, bits=32):
    return bits - x.bit_length()