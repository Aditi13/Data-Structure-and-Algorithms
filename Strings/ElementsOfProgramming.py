'''
Created on Apr 20, 2016

@author: Aditi
'''

def strings_to_ints():
    """
    """
    pass

def replace_remve(input_string):
    """
    """
    write_ind = 0
    a_count = 0
    for ch in input_string:
        if ch != 'b':
            input_string[write_ind] = ch
            write_ind += 1
        if ch == 'a':
            a_count += 1
    return input_string

inputStr = ['a','b']
print (replace_remve(inputStr))
     

def test_palindromicity():
    pass

def reverse_all_words():
    pass

def compute_phone_nos():
    pass

def look_and_say():
    pass

def roman_to_decimals():
    pass

def compute_valid_IP():
    pass

def charac_length_encoding():
    pass