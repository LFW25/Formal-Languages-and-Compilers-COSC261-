'''
Define a Python 3 function all_strings(alpha, length)
that returns a list containing all strings of the given
length over the alphabet alpha in no particular order.
The alphabet alpha is a non-empty set of symbols, each of
which is a single-digit number or a single-character string,
and length is a non-negative integer. Items in the
resulting list are Python strings.
'''

def all_strings(alpha, length):
    n = len(alpha)
    alpha_list = list(alpha)
    return all_strings_recursive(alpha_list, "", n, length, [])


def all_strings_recursive(alpha, word, n, length, slist = []):

    if length == 0:
        slist.append(word)
    
    else:    
        for i in range(n):
            new_word = word + str(alpha[i])
            all_strings_recursive(alpha, new_word, n, length - 1, slist)
    
    return slist
    



print(all_strings({0, 1}, 3))
'''['000', '001', '010', '011', '100', '101', '110', '111']'''

print(all_strings({'a', 'b'}, 2))
'''['aa', 'ab', 'ba', 'bb']'''

print(all_strings({'a', 'b', 'c'}, 2))
'''9'''