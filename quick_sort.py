
def sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    return sort(left) + center + sort(right)
print(sort([6,6,3,2,7,12,54,1,9,0]))