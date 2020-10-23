class ManagerSort:
    @staticmethod
    def selection_sort(trees, quantity_swap_selection, quantity_compare_selection):

        for iterator in range(len(trees) - 1):
            max_price_index = iterator

            for max_price_iterator in range(iterator + 1, len(trees)):
                if trees[max_price_index].price < trees[max_price_iterator].price:
                    max_price_index = max_price_iterator

                quantity_compare_selection += 1

            trees[iterator], trees[max_price_index] = trees[max_price_index], trees[iterator]

            quantity_swap_selection += 1

        return quantity_swap_selection, quantity_compare_selection

    @staticmethod
    def merge_sort(trees, quantity_swap_merge, quantity_compare_merge):
        if len(trees) <= 1:
            return 0, 0

        array_middle = len(trees) // 2
        left_array = trees[:array_middle]
        right_array = trees[array_middle:]

        quantity_swap_merge_temp, quantity_compare_merge_temp = ManagerSort.merge_sort(left_array, quantity_swap_merge,
                                                                                       quantity_compare_merge)
        quantity_swap_merge += quantity_swap_merge_temp
        quantity_compare_merge += quantity_compare_merge_temp

        quantity_swap_merge_temp, quantity_compare_merge_temp = ManagerSort.merge_sort(right_array, quantity_swap_merge,
                                                                                       quantity_compare_merge)
        quantity_swap_merge += quantity_swap_merge_temp
        quantity_compare_merge += quantity_compare_merge_temp

        left_iterator = right_iterator = general_iterator = 0

        while left_iterator < len(left_array) and right_iterator < len(right_array):
            if left_array[left_iterator].height_in_sm < right_array[right_iterator].height_in_sm:
                trees[general_iterator] = left_array[left_iterator]
                left_iterator += 1
            else:
                trees[general_iterator] = right_array[right_iterator]
                right_iterator += 1

            quantity_compare_merge += 1
            quantity_swap_merge += 1

            general_iterator += 1

        while left_iterator < len(left_array):
            trees[general_iterator] = left_array[left_iterator]
            left_iterator += 1
            general_iterator += 1

            quantity_swap_merge += 1

        while right_iterator < len(right_array):
            trees[general_iterator] = right_array[right_iterator]
            right_iterator += 1
            general_iterator += 1

            quantity_swap_merge += 1

        return quantity_swap_merge, quantity_compare_merge
