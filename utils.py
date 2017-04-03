

def precision(number):
    """
    :return: small number rounded to readable format
    """
    if number >= 1:
        return number
    amount = 0
    for n in str(number):
        if n == '0':
            amount += 1
        elif n == '.':
            continue
        else:
            break
    return '.{}f'.format(amount + 1)


def newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return float(n) / k * newton(n - 1, k - 1)


