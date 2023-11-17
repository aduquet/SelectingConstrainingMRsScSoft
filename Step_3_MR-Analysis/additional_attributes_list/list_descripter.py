import numpy as np

class ListDescripter():

    def __init__(self, data_list: list):
        self.data_list = data_list

    def get_length(self):
        return len(self.data_list)

    def has_zero(self):
        return 0 in self.data_list
    
    def cnt_zeros(self):
        return sum(1 for num in self.data_list if num == 0)

    def cnt_positive_numbers(self):
        return sum(1 for num in self.data_list if num > 0)

    def cnt_negative_numbers(self):
        return sum(1 for num in self.data_list if num < 0)

    def get_minimum(self):
        return min(self.data_list)

    def get_maximum(self):
        return max(self.data_list)

    def get_sum(self):
        return sum(self.data_list)

    def get_mean(self):
        return np.mean(self.data_list)

    def get_median(self):
        return np.median(self.data_list)

    def get_range(self):
        return max(self.data_list) - min(self.data_list)

    def has_duplicates(self):
        return len(self.data_list) != len(set(self.data_list))

    def is_sorted(self):
        return self.data_list == sorted(self.data_list)

    def count_distinct_values(self):
        return len(set(self.data_list))

    def contains_even_numbers(self):
        return any(num % 2 == 0 for num in self.data_list)

    def contains_odd_numbers(self):
        return any(num % 2 != 0 for num in self.data_list)

    def contains_integers(self):
        return all(isinstance(num, int) for num in self.data_list)
    
    def pp_numbers(self):
        return sum(num for num in self.data_list if num > 0) / len(self.data_list)

    def pn_numbers(self):
        return sum(num for num in self.data_list if num < 0) / len(self.data_list)

        
