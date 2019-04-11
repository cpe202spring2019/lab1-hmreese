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
    if int_list == None:                                                        
        raise ValueError
    if len(int_list) == 0:
        return None
    else:
        if high > low:
            mid = (high + low) // 2
            if int_list[mid] == target:
                return mid
            elif int_list[mid] > target:
                return bin_search(target, low, mid, int_list)
            elif int_list[mid] < target:
                return bin_search(target, mid + 1, high, int_list)
        else:
            return None


