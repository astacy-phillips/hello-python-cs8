def count_to_one_hundred():
    for x in range(1, 101):
        print(x)


def stub_function():
    pass


def multiply_two_numbers(x, y):
    return x * y


def main():
    """
    This is where we put long comments that document the purpose of this
    class or function or method or whatever it is that we feel the need
    to document with a novel.
    etc.
    etc.
    """

    # count_to_one_hundred()
    value = multiply_two_numbers(6, 7)
    print(value)


if __name__ == "__main__":
    main()

# print("Hello world")

# a = 1
# b = "this is a string"
# c = [1, 2, 3, 4]  # This is a list, it looks like an array in JS
# d = (5, 6, 7, 8)  # This is a tuple, an immutable object, a permanent array
# e = {'name': 'Amanda', 'number': 1}  # dict, like a JS object

# print(a)
# print(b)
# print(c)
# print(d)

# print(len(c))
# c.append(42)
# print(c)
# c.append('will this work?')
# print(c)

# print(e)
# print(e['name'])
# e['number'] += 9000
# print(e['number'])

# for number in c:
#     for m in d:
#         print(number * m)
