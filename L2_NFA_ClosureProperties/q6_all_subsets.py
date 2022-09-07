def all_subsets(s):
    '''
    Returns a list containing all subsets of the given set s in no particular order.
    '''
    s = list(s)
    powerset = []
    #powerset = [s[j] for i in range(1 << len(s)) for j in range(len(s)) if (i & (1 << j))]
    #powerset = [{}] + [set(s[j : i]) for i in range(len(s) + 1) for j in range(i)]
    x = len(s)
    for i in range(1 << x):
        powerset.append(set([s[j] for j in range(x) if (i & (1 << j))]))

    return powerset

print(sorted(map(sorted, all_subsets({0, 1, 2}))))
#[[], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]]

print(sorted(map(sorted, all_subsets({'a', 'b'}))))
#[[], ['a'], ['a', 'b'], ['b']]

print({1} in all_subsets({0, 1, 2}))
#True

print(sorted(map(sorted, all_subsets({'9'}))))
#[[], ['9']]

print(sorted(map(sorted, all_subsets(set()))))
#[[]]

print(sorted(map(sorted, all_subsets({7, 5, 3, 1}))))
#[[], [1], [1, 3], [1, 3, 5], [1, 3, 5, 7], [1, 3, 7], [1, 5], [1, 5, 7], [1, 7], [3], [3, 5], [3, 5, 7], [3, 7], [5], [5, 7], [7]]

print(sorted(map(sorted, all_subsets({'s', 'q', 'z', 'a', 'h', 'n'}))))
#[[], ['a'], ['a', 'h'], ['a', 'h', 'n'], ['a', 'h', 'n', 'q'], ['a', 'h', 'n', 'q', 's'], ['a', 'h', 'n', 'q', 's', 'z'], ['a', 'h', 'n', 'q', 'z'], ['a', 'h', 'n', 's'], ['a', 'h', 'n', 's', 'z'], ['a', 'h', 'n', 'z'], ['a', 'h', 'q'], ['a', 'h', 'q', 's'], ['a', 'h', 'q', 's', 'z'], ['a', 'h', 'q', 'z'], ['a', 'h', 's'], ['a', 'h', 's', 'z'], ['a', 'h', 'z'], ['a', 'n'], ['a', 'n', 'q'], ['a', 'n', 'q', 's'], ['a', 'n', 'q', 's', 'z'], ['a', 'n', 'q', 'z'], ['a', 'n', 's'], ['a', 'n', 's', 'z'], ['a', 'n', 'z'], ['a', 'q'], ['a', 'q', 's'], ['a', 'q', 's', 'z'], ['a', 'q', 'z'], ['a', 's'], ['a', 's', 'z'], ['a', 'z'], ['h'], ['h', 'n'], ['h', 'n', 'q'], ['h', 'n', 'q', 's'], ['h', 'n', 'q', 's', 'z'], ['h', 'n', 'q', 'z'], ['h', 'n', 's'], ['h', 'n', 's', 'z'], ['h', 'n', 'z'], ['h', 'q'], ['h', 'q', 's'], ['h', 'q', 's', 'z'], ['h', 'q', 'z'], ['h', 's'], ['h', 's', 'z'], ['h', 'z'], ['n'], ['n', 'q'], ['n', 'q', 's'], ['n', 'q', 's', 'z'], ['n', 'q', 'z'], ['n', 's'], ['n', 's', 'z'], ['n', 'z'], ['q'], ['q', 's'], ['q', 's', 'z'], ['q', 'z'], ['s'], ['s', 'z'], ['z']]

print(sorted(map(sorted, all_subsets({'s', 'q', 'z', 'a', 'n'}))))
#[[], ['a'], ['a', 'n'], ['a', 'n', 'q'], ['a', 'n', 'q', 's'], ['a', 'n', 'q', 's', 'z'], ['a', 'n', 'q', 'z'], ['a', 'n', 's'], ['a', 'n', 's', 'z'], ['a', 'n', 'z'], ['a', 'q'], ['a', 'q', 's'], ['a', 'q', 's', 'z'], ['a', 'q', 'z'], ['a', 's'], ['a', 's', 'z'], ['a', 'z'], ['n'], ['n', 'q'], ['n', 'q', 's'], ['n', 'q', 's', 'z'], ['n', 'q', 'z'], ['n', 's'], ['n', 's', 'z'], ['n', 'z'], ['q'], ['q', 's'], ['q', 's', 'z'], ['q', 'z'], ['s'], ['s', 'z'], ['z']]

print(len(all_subsets({1, 2, 3, 4, 5, 6, 7})))
#128