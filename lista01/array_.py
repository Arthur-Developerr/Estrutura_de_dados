def array_invert(array):
    length = len(array) - 1
    i = 0
    array_y = [int] * len(array)
    while length >= 0:
        array_y[i] = array[length]
        length -= 1
        i += 1
    return array_y
        


def array_sum(array):
    sum = array[0]
    for i in range(1,len(array)):
        sum += array[i]
    return sum


def array_multi(array):
    multi = array[0]
    for i in range(1, len(array)):
        multi = multi * array[i]
    return multi


def array_numbers_squared(array):
    array_squared = [int] * len(array)
    for i in range(len(array)):
        array_squared[i] = array[i] ** 2
        
    return array_squared


def sum_two_index_array(array, x, y):
    if x < len(array) and y < len(array):
        return array[x] + array[y]
    else:
        raise IndexError
    
def avarage_array(array):
    sum_items = sum(array)
    avarage = sum_items / len(array)
    if type(avarage) == float:
        return float(f"{avarage:.1f}")
    else:
        return avarage


def smaller_array(array):
    smaller = array[0]
    for i in range(1,len(array)):
        if array[i] < smaller:
            smaller = array[i]
    if type(smaller) == float:
        return float(f"{smaller:.2f}")
    else:
        return smaller



def greatest_array(array):
    greatest = array[0]
    for i in range(1,len(array)):
        if array[i] > greatest:
            greatest = array[i]
    if type(greatest) == float:
        return float(f"{greatest:.2f}")
    else:
        return greatest


