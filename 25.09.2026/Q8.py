'''A company receives a list of employee skill codes represented as strings.
 Employees having the same set of characters in their skill codes belong to
 the same skill category, even if the characters appear in a different order.
  The HR system needs to organize employees into appropriate skill groups.'''

strs = ["eat","tea","tan","ate","nat","bat"]

dict = {}

for word in strs:
    key = ""
    letters=sorted(word)
    for i in letters:
        key=key+i


    if key in dict:
        dict[key].append(word)
    else:
        dict[key]=[word]
print(list(dict.values()))
