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
    alpha_list = list(alpha)
    string_list = []

    for i in range(len(alpha_list)):
        j = 0
        while j < length:
            current_word = alpha_list[j]*length
            
            
    



print(all_strings({0, 1}, 3))
'''['000', '001', '010', '011', '100', '101', '110', '111']'''

#print(all_strings({'a', 'b'}, 2))
'''['aa', 'ab', 'ba', 'bb']'''

#print(all_strings({'a', 'b', 'c'}, 2))
'''9'''