
def find_orig_strand(num,sorted_list):

    """
    Returns the biggest number in the sorted list that is smaller than the given number.
    If the given number is bigger than all the numbers in the list, return the last number in the list.
    """
    if num > sorted_list[-1]:
        return sorted_list[-1]
    for i in range(len(sorted_list)-1):
        if num > sorted_list[i] and num < sorted_list[i+1]:
            return sorted_list[i]



def exists_in_dict(dict,list):
    """
        this function takes a dictionary and a list of numbers
        iterates over the list and checks if the current number is a key in
        the dictionary and if so deletes the number from the list.
    """
    for num in list:
        for key in dict.keys():
            if num in dict[key]:
                list.remove(num)



def diff_lists(list1, list2):
    """
        returns a list of the elements that are contained in list 2 but not in list 1
    """
    return list(set(list2) - set(list1))



def create_dict(lst, n):
    # Create an empty dictionary to store the results
    result = {}

    # Iterate through the list of numbers
    for i in range(len(lst) - 1):
        # Create an empty list to store the values for this key
        values = []

        # Iterate through the numbers between this key and the next key
        for j in range(lst[i] + 1, lst[i + 1]):
            # Add the number to the list of values for this key
            values.append(j)

        # Add the key-value pair to the result dictionary
        result[lst[i]] = values

    # For the last key-value pair, include all numbers between the last key and n (including n)
    values = []
    for j in range(lst[-1] + 1, n + 1):
        values.append(j)
    result[lst[-1]] = values

    # Return the final dictionary
    return result





def diff_dicts(dict1, dict2, key):
    """
    This function takes two dictionaries as input, checks for a key if it's present in both dictionaries, and returns a list containing the elements that are present in the value of the key in dict2 but not in the value of the key in dict1.

    Args:
    - dict1 (dict): A dictionary object.
    - dict2 (dict): Another dictionary object.
    - key (str): A key that is present in both dictionaries.

    Returns:
    - A list containing the elements that are present in the value of the key in dict2 but not in the value of the key in dict1.
    """
    if key in dict1 and key in dict2:  # Check if the key is present in both dictionaries
        return list(set(dict2[key]) - set(dict1[key]))
    else:
        return []

def diff_dicts_list(dict1, dict2, keys):
    """
    This function takes two dictionaries and a list of keys as input, and runs the diff_dicts() function for every key in the list.

    Args:
    - dict1 (dict): A dictionary object.
    - dict2 (dict): Another dictionary object.
    - keys (list): A list of keys that are present in both dictionaries.

    Returns:
    - A dictionary object that contains the result of running the diff_dicts() function for every key in the list.
    """
    result = {}
    for key in keys:
        result[key] = diff_dicts(dict1, dict2, key)
    return result


def switch_dict_key_value(my_dict, num_list):
    """
    This function takes a dictionary and a list of numbers as input,
    and switches the key that each number is in its value to the number.
    """
    for num in num_list:
        # Find the key that has the value of the given number
        for key, value in my_dict.items():
            if num in value:
                # Switch the key and value
                my_dict[num] = my_dict[key]
                del my_dict[key]
                # Replace the value of the new key with the original key
                my_dict[num].remove(num)
                my_dict[num].append(key)
                break
    return my_dict


