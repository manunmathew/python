# Create a module String
# str_even()

def str_even(s):
    even = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
    return even


# str_rev()
def str_rev(s):
    rev = s[::-1]
    return rev
# str_palindrome() return True or False

def str_palindrome(s):
    if str_rev(s) == s:
        return True
    else:
        return False

# str_space_remover()
def str_space_remover(s):
    return s.replace(" ", "")
