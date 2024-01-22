def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 4):
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
    except Exception:
        result = a + b
    return result