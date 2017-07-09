def quicksort(list):

    if list : return quicksort([x for x in list if x < list[0]]) + [x for x in list if x == list[0]] + quicksort([x for x in list if x < list[0]])

    return[3,6,64563,7]


