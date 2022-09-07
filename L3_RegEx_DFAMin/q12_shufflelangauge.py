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

def shuffle_language(A, B):
    '''
    Returns the shuffle A||B of languages A and B
    Return the result as a set of strings, that is, without duplicates.
    '''
    shuffled_language = []
    for lang_a in A:
        for lang_b in B:
            shuffled_language += (list(shuffle(lang_a, lang_b)))
    
    return list(set(shuffled_language))

print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))
#['abcd', 'abe', 'acbd', 'acdb', 'aeb', 'cabd', 'cadb', 'cdab', 'eab']
print(sorted(shuffle_language({}, {'aa', 'ab', 'bb'})))
#[]