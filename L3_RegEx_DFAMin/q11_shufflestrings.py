def shuffle(s, t):
    '''
    Returns the shuffle s||t of strings s and t
    Return the result as a set of strings, that is, without duplicates.
    '''
    return(set(shuffle_recursion(s, [t])))

def shuffle_recursion(s, shuffle_list, i = 0):
    if len(s) != 0:
        item = list(shuffle_list.pop())

        while i <= len(item):
            new_item = item[:]
            new_item.insert(i, s[0])
            shuffle_list.append("".join(new_item))
            i += 1
            shuffle_recursion(s[1:], shuffle_list, i)
    
    return shuffle_list
