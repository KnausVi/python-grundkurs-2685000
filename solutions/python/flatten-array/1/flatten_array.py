def flatten(iterable):
    result_list = []
    for item in iterable:
        if isinstance(item, list):
            result_list.extend(flatten(item))          
        else:
            if item != None:
                result_list.append(item)
            
    return result_list