DEC_TO_HEX = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def is_integer(number):
    try:
        int(number)
        return number
    except ValueError:
        return False


def dec_to_hex(number):
    number = int(number)
    if number == 0:
        return '0'
    is_negative = False
    if number < 0:
        number *= -1
        is_negative = True
    number_in_dex = []
    while number != 0:
        tmp = number // 16
        remainder = DEC_TO_HEX[number % 16]
        number = tmp
        number_in_dex.append(remainder)
    result = ''.join(reversed(number_in_dex))
    if is_negative:
        result = '-' + result
    return result
