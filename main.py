import csv
import time

from manager.ManagerSort import ManagerSort
from models.ArtificialTree import ArtificialTree


def parse_csv(path):
    unsorted_trees = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for i in csv_reader:
            unsorted_trees.append(ArtificialTree(i[0], int(i[1]), int(i[2]), i[3]))
    return unsorted_trees


if __name__ == '__main__':
    unsorted_trees = parse_csv('trees_list.csv')

    quantity_swap_selection = 0
    quantity_compare_selection = 0
    quantity_swap_merge = 0
    quantity_compare_merge = 0

    start_time = time.time()

    quantity_swap_selection, quantity_compare_selection = ManagerSort.selection_sort(unsorted_trees,
                                                                                     quantity_swap_selection,
                                                                                     quantity_compare_selection)

    time_of_sorting = time.time() - start_time

    for i in unsorted_trees:
        print(i)

    print("Quantity swap selection = ", quantity_swap_selection)
    print("Quantity compare selection = ", quantity_compare_selection)

    print("Time = ", time_of_sorting)

    print('ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING \n'
          'ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING \n'
          'ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING ANOTHER SORTING \n')

    start_time = time.time()

    quantity_swap_merge, quantity_compare_merge = ManagerSort.merge_sort(unsorted_trees, quantity_swap_merge,
                                                                         quantity_compare_merge)

    time_of_sorting = time.time() - start_time

    for i in unsorted_trees:
        print(i)

    print("Quantity swap merge = ", quantity_swap_merge)
    print("Quantity compare merge = ", quantity_compare_merge)

    print("Time = ", time_of_sorting)
