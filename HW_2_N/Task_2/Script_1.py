list_1 = ["apple", "orange", 1, None, ["dog", "cat"], "book", "car", True, "False"]


# example 1
def example_1():
    print('Example 1')
    list_2 = []
    for element in list_1:
        if isinstance(element, str):
            list_2.append(element)
    print(list_2)


# example 2
def example_2():
    print('Example 2')
    list_2 = []
    for element in list_1:
        if type(element) is str:
            list_2.append(element)
    print(list_2)


# example 3
def example_3():
    print('Example 3')
    list_2 = [x for x in list_1 if isinstance(x, str)]
    print(list_2)


example_1()
example_2()
example_3()
