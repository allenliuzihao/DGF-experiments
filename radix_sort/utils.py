from multiprocessing.pool import Pool

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

def count_digits_chunk(chunk, i):
    """Count digit occurrences in a chunk of objects"""
    local_buckets = [0] * 256
    for obj in chunk:
        digit_value = (obj.key >> (i * 8)) & 0xFF
        local_buckets[digit_value] += 1
    return local_buckets

def add_hist(a, b):
    return [x+y for x, y in zip(a, b)]

def merge_all(histograms):
    while len(histograms) > 1:
        pairs = [(histograms[i], histograms[i+1]) for i in range(0, len(histograms)-1, 2)]
        with Pool() as pool:
            histograms = pool.starmap(add_hist, pairs) + \
                         (histograms[-1:] if len(histograms) % 2 == 1 else [])
    return histograms[0]