#########################################
# NAME: Maya Voloshin
# LOGIN: mayavolo
# ID: 322853680
# DESCRIPTION: ex7, different recursions
#########################################

def print_to_n(n):
    """
    This function prints all the numbers from 1 to n
    """
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


def digit_sum(n):
    """
    This function returns the digit sum of n
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    return digit_sum(n // 10) + n % 10


def is_prime(n):
    """
    This function returns if the number is prime
    :param n: number
    :return: bool True Or False
    """
    if n <= 1:
        return False
    return not has_divisor(n, 2)


def has_divisor(n, i):
    """
    This function checks if the given number has a divisor
    :param n: a number
    :param i: the minimal divisor (2)
    :return: bool True Or False
    """
    if i >= n:
        return False
    if n % i == 0:
        return True
    return has_divisor(n, i + 1)


def play_hanoi(hanoi, n, src, dst, temp):
    """
    This function solves the hanoi game
    """
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
        return

    play_hanoi(hanoi, n - 1, src, temp, dst)
    hanoi.move(src, dst)
    play_hanoi(hanoi, n - 1, temp, dst, src)


def combinations(chosen_string, entire_list, max_length, repetitions=True):
    """
    This function finds all the possible combinations from the given chars
    according to the given length and constrains
    """
    if len(chosen_string) >= max_length:
        print(chosen_string)
        return
    for element in entire_list:
        new_string = chosen_string + element
        if not repetitions:
            altered_list = [char for char in entire_list if char != element]
            combinations(new_string, altered_list, max_length, repetitions)
        else:
            combinations(new_string, entire_list, max_length, repetitions)


def print_sequences(char_list, n):
    """
    This function prints all the possible sequences from the char list in the length n
    """
    combinations('', char_list, n)


def print_no_repetition_sequences(char_list, n):
    """
   This function prints all the possible sequences from the char list in the length n
   with no repetitions of the same char
    """
    combinations('', char_list, n, False)


def parentheses(n):
    """ This function returns a list of all of the possible parentheses combinations"""
    return parentheses_generating_func(n, n, '')


def parentheses_generating_func(num_open, num_closed, current_string):
    """ This function makes a list of all of the possible parentheses combinations"""
    is_leaf = True
    current_parentheses_list = []
    if num_open > 0:
        is_leaf = False
        current_parentheses_list += parentheses_generating_func(num_open - 1, num_closed, current_string + "(")
    if num_closed > 0 and num_open < num_closed:
        is_leaf = False
        current_parentheses_list += parentheses_generating_func(num_open, num_closed - 1, current_string + ")")
    if not is_leaf:
        return current_parentheses_list
    else:
        return [current_string]


def flood_fill(image, start):
    """ This function tries to fill the array in every possible way according to the rules"""
    if image[start[0]][start[1]] == "*":
        return

    image[start[0]][start[1]] = "*"
    flood_fill(image, (start[0] + 1, start[1]))
    flood_fill(image, (start[0] - 1, start[1]))
    flood_fill(image, (start[0], start[1] + 1))
    flood_fill(image, (start[0], start[1] - 1))

