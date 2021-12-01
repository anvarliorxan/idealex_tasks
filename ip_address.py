def is_valid(ip):
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
            return False

    return True


def convert(s):
    sz = len(s)

    if sz > 12:
        return []
    snew = s
    l = []

    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)

                snew = s

    return l


# Examples
example1 = '25525511135'
example2 = '0000'
example3 = '1111'
example4 = '010010'
example5 = '101023'

print(convert(example1))
print(convert(example2))
print(convert(example3))
print(convert(example4))
print(convert(example5))
