def distance(s1, s2):
    ''' 
    distance(string, string) -> integer
    
    Keyword arguments:
    s1 -- string one
    s2 -- string two

    Return levenshtein distance between two strings
    '''

    if len(s1) < len(s2):
        return distance(s2, s1)
    if not s1:
        return len(s2)
 
    row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current = [i + 1]

        for j, c2 in enumerate(s2):
            # find the min cost of deletion, insertion and substitution
            current.append(min(row[j+1]+1, current[j]+1, row[j]+(c1 != c2)))

        row = current
 
    return row[-1]


print distance("hello", "bleh")     # -> 4
print distance("hello", "hello")    # -> 0
print distance("abc", "abd")        # -> 1
