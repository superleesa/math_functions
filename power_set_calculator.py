def power_set(a_set, size=None):
    all_elements = []
    number_of_counter = 2**len(a_set)

    for counter in range(number_of_counter):
        binary_string = format(counter, "0{}b".format(len(a_set)))
        # print(binary_string)
        element = []
        for i in range(len(binary_string)):
            if binary_string[i] == "1":
                element.append(a_set[i])
        all_elements.append(element)

    return all_elements


set = [1, 2, 3]
print(power_set(set))
# output = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]