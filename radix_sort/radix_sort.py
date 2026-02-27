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

def radix_sort_serial_prefix_scan(objects: list[utils.Object]):
    # scan 8 bits at a time, so we need 256 buckets
    buckets = [0 for _ in range(256)]
    max_key = max(obj.key for obj in objects)
    num_iterations = (max_key.bit_length() + 7) // 8

    temporary = [None] * len(objects)  # Temporary array to hold sorted objects for this iteration

    for i in range(num_iterations):
        # Clear buckets for the current iteration
        for j in range(len(buckets)):
            buckets[j] = 0

        # Place objects into the appropriate bucket based on the current 8-bit chunk
        for obj in objects:
            digit_value = (obj.key >> (i * 8)) & 0xFF
            buckets[digit_value] += 1
        
        # Compute prefix sums to determine the starting index for each bucket
        offset = 0
        for j in range(0, 256):
            temp = buckets[j]
            buckets[j] = offset
            offset += temp
        
        # Create a temporary array to hold the sorted objects for this iteration
        for obj in objects:
            digit_value = (obj.key >> (i * 8)) & 0xFF
            temporary[buckets[digit_value]] = obj               
            buckets[digit_value] += 1

        # Copy the sorted objects back to the original list
        for j in range(len(objects)):
            objects[j] = temporary[j]