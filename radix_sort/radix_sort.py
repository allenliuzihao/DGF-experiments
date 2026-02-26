
import utils

def radix_sort_serial(objects: list[utils.Object]):
    # Find the maximum number to know the number of digits
    max_key = max(obj.key for obj in objects)
    num_digits = utils.get_num_digits(max_key)
    buckets = [[] for _ in range(10)]

    for digit in range(num_digits):
        # clear buckets for the current digit
        for bucket in buckets:
            bucket.clear()

        # Place objects into the appropriate bucket based on the current digit
        for obj in objects:
            digit_value = utils.get_digit(obj.key, digit)
            buckets[digit_value].append(obj)
        
        # Flatten the list of buckets back into the original list
        index = 0
        for bucket in buckets:
            for item in bucket:
                objects[index] = item
                index += 1
