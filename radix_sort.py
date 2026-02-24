
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

def radix_sort(objects: list[Object]):
    # Find the maximum number to know the number of digits
    max_key = max(obj.key for obj in objects)
    num_digits = get_num_digits(max_key)
    buckets = [[] for _ in range(10)]

    for digit in range(num_digits):
        # clear buckets for the current digit
        for bucket in buckets:
            bucket.clear()

        # Place objects into the appropriate bucket based on the current digit
        for obj in objects:
            digit_value = get_digit(obj.key, digit)
            buckets[digit_value].append(obj)
        
        # Flatten the list of buckets back into the original list
        index = 0
        for bucket in buckets:
            for item in bucket:
                objects[index] = item
                index += 1

if __name__ == "__main__":

    # test 1
    objects = [
        Object(170, "value1"),
        Object(45, "value2"),
        Object(75, "value3"),
        Object(90, "value4"),
        Object(2, "value5"),
        Object(802, "value6"),
        Object(24, "value7"),
        Object(100, "value8")
    ]
    radix_sort(objects)
    for obj in objects:
        print(f"Key: {obj.key}, Value: {obj.value}")

    # test 2
    objects = [Object(i, f"value{i}") for i in range(1000, 0, -1)]
    radix_sort(objects)
    for obj in objects:
        print(f"Key: {obj.key}, Value: {obj.value}")