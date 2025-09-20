def append(list1, list2):
    result = []
    for item in list1:
        result += [item]       
    for item in list2:
        result += [item]        
    return result


def concat(lists):
    result = []
    for item in lists:
        result += item               
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result

def foldl(function, list, initial):
    akkumulator = initial
    for item in list:
        akkumulator = function(akkumulator, item)
    return akkumulator


def foldr(function, list, initial):
    akkumulator = initial
    for item in reversed(list):
        akkumulator = function(akkumulator, item)
    return akkumulator


def reverse(list):
    reverse_list = []
    for item in list:
        reverse_list = [item] + reverse_list        
    return reverse_list
