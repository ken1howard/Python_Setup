# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    for k in kwargs.keys():
        print(f"{k}:{kwargs[k]}")

name_args(name = "Randon", weather ="sunny", location ="park", time=3)

# all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

def all_true(iter):
    return all(iter)

print(all_true([True,True,True]))
print(all_true((True, False)))

# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(iter):
    return any(iter)

print(one_true([True,True,True]))
print(one_true([False, False, False]))
print(one_true((True, False)))

# recursive_factorial - Uses recursion to find the factorial of an integer.

def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(3))
print(recursive_factorial(6))

# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.

def recursive_deduplicate(my_str,i=0):
    if len(my_str) <= 1 or i == len(my_str)-1:
        return my_str
    else:
        if my_str[i] == my_str[i+1]:
            return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
        else:
            return recursive_deduplicate(my_str,i+1)
        
print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))

# recursive_reverse - Uses recursion to reverse a string.

def recursive_reverse(str, i=0):
    if len(str)==0:
        return ""
    elif i == len(str)-1:
        return str[0]
    else:
        return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))
