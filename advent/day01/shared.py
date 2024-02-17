def extract_number(line):
    first = None
    last = None
    for char in line:
        if str.isdigit(char):
            if first:
                last = char
            else:
                first = char
    return join_digits(first, last)


def join_digits(first, last):
    if last:
        number = first + last
    else:
        number = first + first
    return int(number)
