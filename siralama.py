def sorting(list_of_lists):
    for l in list_of_lists:
        if isinstance(l,list):
            l.reverse()
    list_of_lists.reverse()
    return list_of_lists



nested_list =[[1, 2], [3, 4], [5, 6, 7]]

print(sorting(nested_list))