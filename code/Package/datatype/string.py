def validate_email(s):
    if '@' not in s or '.' not in s:
        return False

    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

    x = s.split("@")
    if len(x) != 2:
        return False

    y = x[1].split(".")
    if len(y) != 2:
        return False

    for i in x[0]:
        if i not in allowed_characters:
            return False

    if y[0].isalnum() and y[1].isalpha() and len(y[1]) == 3:
        return True
    else:
        return False
