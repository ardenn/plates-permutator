import string
import operator
import functools


def compare_letters(letter_list, max_letter, min_letter):
    """
    A function that given two letters and a list of letters counts the number of elements in between them in the list in a strictly circular manner.
    """
    if max_letter > min_letter:
        possible_values = letter_list.index(
            max_letter) - letter_list.index(min_letter)+1
    elif max_letter < min_letter:
        possible_values = len(
            letter_list) + letter_list.index(max_letter) - letter_list.index(min_letter)+1
    else:
        possible_values = 1  # only one possible values since both characters are equal
    return possible_values


def compare_numbers(number_list, max_num, min_num):
    """
    A function that given two numbers and a list of numbers counts the number of elements in between them in the list in a strictly circular manner.
    """
    if max_num > min_num:
        possible_values = number_list.index(
            max_num) - number_list.index(min_num)+1
    elif max_num < min_num:
        possible_values = len(
            number_list) + number_list.index(max_num) - number_list.index(min_num)+1
    else:
        possible_values = 1  # only one possible values since both characters are equal
    return possible_values


def plate_counter(plate1, plate2):
    """
    A function that given two Kenyan number plates and calculates the number of plates in between
    - plate1: this is the first number plate
    - plate2: this is the second number plate
    Kenyan number plates are of the format LLLNNNL where L is a letter excluding 'I' and 'O' and N is a digit
    """

    # Create a list of all possible values of L
    letters_list = list(string.ascii_uppercase)
    letters_list.pop(letters_list.index("I"))
    letters_list.pop(letters_list.index("O"))

    # create an empty list to keep track of the number of possibilities for each position
    position_counts = []

    # Create a list of all possible values of N
    numbers_list = list(string.digits)

    # Determine the bigger(later) plate and the smaller(earlier) plate
    # Split the plates into a list to allow comparison by sections
    [max_plate, min_plate] = [list(max(plate1.upper(), plate2.upper())), list(
        min(plate1.upper(), plate2.upper()))]

    # While comparing each positional character in max_plate and min_plate lets get the number of possible values that could occupy that position

    # For section one i.e "LLL"
    # Skip the first character since its always a K
    for min_char, max_char in zip(min_plate[1:3], max_plate[1:3]):
        position_counts.append(compare_letters(
            letters_list, max_char, min_char))

    # For section two i.e "NNN"
    for min_char, max_char in zip(min_plate[3:6], max_plate[3:6]):
        position_counts.append(compare_numbers(
            numbers_list, max_char, min_char))

    # For the last section i.e "L"
    position_counts.append(compare_letters(
        letters_list, max_plate[-1], min_plate[-1]))
    # Multiply the postion_counts values and return the result
    return functools.reduce(operator.mul, position_counts)


if __name__ == "__main__":
    print(plate_counter("KCR101A", "KCR101A"))
    print(plate_counter("KBR101A", "KCR101Z"))
    print(plate_counter("KCR101A", "KCR101Z"))
    print(plate_counter("KAR101A", "KDD282D"))
