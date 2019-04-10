def max_list_iter(int_list):
    if int_list == None:
        raise ValueError

    if len(int_list) == 0:
        return None

    else: # if int_list != None and len(int_list) > 0:
        biggest = int_list[0]
        for i in int_list:
            if i > biggest:
                biggest = i
        return biggest



def reverse_rec(int_list):
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return int_list
    else:
        temp = reverse_rec(int_list[1:])
        temp.append(int_list[0])
        return temp


def bin_search(target, low, high, int_list):
    if len(int_list) == 0:
        return None
    if int_list == None:
        raise ValueError
    if low > high:
        return None

    mid = (high + low) // 2
    if int_list[mid] == target:
        return mid
    if int_list[mid] > target:
        high = mid
    if int_list[mid] < target:
        low = mid

    temp = bin_search(target, low, high, int_list)

    return temp

# not completed, part 3 still does not work
