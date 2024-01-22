#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                try:
                    div = a / b
                    result_list.append(div)
                except ValueError:
                    div = 0
                    result_list.append(div)

                except TypeError:
                    print("wrong type")
                    result_list.append(0)

        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)

        except IndexError:
            print("out of range")
            result_list.append(0)

        except TypeError:
            print("wrong type")
            result_list.append(0)

        finally:
            pass
    return result_list
