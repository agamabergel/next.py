import functools

def double_letter(my_str):
    """double each letter with one-line method
    Args:
        my_str (str): a string
    """
    return functools.reduce(lambda a, b: a + b, list(map(lambda x: x*2, list(my_str))))



if __name__ == "__main__":
    print(double_letter("python"))
    print(double_letter("we are the champions!"))
