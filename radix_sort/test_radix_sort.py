import unittest
import radix_sort
import utils
import random
import time

class TestRadixSort(unittest.TestCase):
    
    def test_basic_sorting(self):
        """Test basic sorting with random numbers"""
        objects = [
            utils.Object(170, "a"),
            utils.Object(45, "b"),
            utils.Object(75, "c"),
            utils.Object(90, "d"),
            utils.Object(2, "e"),
            utils.Object(802, "f"),
            utils.Object(24, "g"),
            utils.Object(2, "h"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [2, 2, 24, 45, 75, 90, 170, 802])
    
    def test_single_element(self):
        """Test sorting with a single element"""
        objects = [utils.Object(42, "value")]
        radix_sort.radix_sort_serial(objects)
        self.assertEqual(objects[0].key, 42)
        self.assertEqual(objects[0].value, "value")
    
    def test_already_sorted(self):
        """Test sorting an already sorted list"""
        objects = [
            utils.Object(10, "a"),
            utils.Object(20, "b"),
            utils.Object(30, "c"),
            utils.Object(40, "d"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [10, 20, 30, 40])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list"""
        objects = [
            utils.Object(40, "d"),
            utils.Object(30, "c"),
            utils.Object(20, "b"),
            utils.Object(10, "a"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [10, 20, 30, 40])
    
    def test_all_same_keys(self):
        """Test sorting when all keys are the same"""
        objects = [
            utils.Object(5, "a"),
            utils.Object(5, "b"),
            utils.Object(5, "c"),
            utils.Object(5, "d"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [5, 5, 5, 5])
    
    def test_single_digit_numbers(self):
        """Test sorting single digit numbers"""
        objects = [
            utils.Object(7, "a"),
            utils.Object(2, "b"),
            utils.Object(9, "c"),
            utils.Object(1, "d"),
            utils.Object(5, "e"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [1, 2, 5, 7, 9])
    
    def test_two_digit_numbers(self):
        """Test sorting two digit numbers"""
        objects = [
            utils.Object(99, "a"),
            utils.Object(10, "b"),
            utils.Object(55, "c"),
            utils.Object(23, "d"),
            utils.Object(88, "e"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [10, 23, 55, 88, 99])
    
    def test_large_numbers(self):
        """Test sorting large multi-digit numbers"""
        objects = [
            utils.Object(9876543, "a"),
            utils.Object(123, "b"),
            utils.Object(654321, "c"),
            utils.Object(1, "d"),
            utils.Object(98765, "e"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [1, 123, 98765, 654321, 9876543])
    
    def test_values_preserved(self):
        """Test that object values are preserved during sorting"""
        objects = [
            utils.Object(30, "apple"),
            utils.Object(10, "banana"),
            utils.Object(20, "cherry"),
        ]
        radix_sort.radix_sort_serial(objects)
        self.assertEqual(objects[0].value, "banana")
        self.assertEqual(objects[1].value, "cherry")
        self.assertEqual(objects[2].value, "apple")
    
    def test_with_zero(self):
        """Test sorting when there's a zero"""
        objects = [
            utils.Object(0, "a"),
            utils.Object(100, "b"),
            utils.Object(50, "c"),
            utils.Object(1, "d"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [0, 1, 50, 100])
    
    def test_duplicate_keys(self):
        """Test sorting with many duplicate keys"""
        objects = [
            utils.Object(5, "a"),
            utils.Object(3, "b"),
            utils.Object(5, "c"),
            utils.Object(1, "d"),
            utils.Object(3, "e"),
            utils.Object(5, "f"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [1, 3, 3, 5, 5, 5])
    
    def test_stability(self):
        """Test if the sort maintains relative order of equal elements (stability)"""
        objects = [
            utils.Object(10, "first"),
            utils.Object(5, "a"),
            utils.Object(10, "second"),
            utils.Object(5, "b"),
        ]
        radix_sort.radix_sort_serial(objects)
        # Check that elements with key 5 appear before elements with key 10
        indices_5 = [i for i, obj in enumerate(objects) if obj.key == 5]
        indices_10 = [i for i, obj in enumerate(objects) if obj.key == 10]
        self.assertTrue(all(i < min(indices_10) for i in indices_5))
    
    def test_two_elements(self):
        """Test sorting with two elements"""
        objects = [
            utils.Object(50, "a"),
            utils.Object(20, "b"),
        ]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, [20, 50])
    
    def test_many_elements(self):
        """Test sorting a larger list of elements"""
        objects = [utils.Object(i, f"val_{i}") for i in [73, 12, 45, 9, 38, 56, 2, 91, 27, 64]]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, sorted(keys))
        self.assertEqual(keys, [2, 9, 12, 27, 38, 45, 56, 64, 73, 91])

    def test_random_large_list(self):
        """Test sorting a large list of random elements"""
        random.seed(0)  # for reproducibility

        num_elements = 10000
        objects = [utils.Object(random.randint(0, num_elements), f"val_{i}") for i in range(num_elements)]
        radix_sort.radix_sort_serial_prefix_scan(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, sorted(keys))

        objects = [utils.Object(random.randint(0, num_elements), f"val_{i}") for i in range(num_elements)]
        radix_sort.radix_sort_serial(objects)
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, sorted(keys))

    def test_timing_large_list(self):
        """Test timing of sorting a large list of random elements"""
        random.seed(0)  # for reproducibility

        num_elements = 1000000
        objects = [utils.Object(random.randint(0, num_elements), f"val_{i}") for i in range(num_elements)]
        
        start_time = time.time()
        radix_sort.radix_sort_serial_prefix_scan(objects)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nRadix sort (prefix scan) execution time for {num_elements} elements: {elapsed_time:.4f} seconds")
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, sorted(keys))

        start_time = time.time()
        radix_sort.radix_sort_serial(objects)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nRadix sort (serial) execution time for {num_elements} elements: {elapsed_time:.4f} seconds")
        keys = [obj.key for obj in objects]
        self.assertEqual(keys, sorted(keys))

if __name__ == '__main__':
    unittest.main()
