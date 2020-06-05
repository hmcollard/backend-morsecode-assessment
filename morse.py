#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Morse code decoder

https://www.codewars.com/kata/decode-the-morse-code/python
https://www.codewars.com/kata/decode-the-morse-code-advanced/python


When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is.
And in fact different operators would transmit at different speed.
An amateur person may need a few seconds to transmit a single character,
a skilled professional can transmit 60 words per minute,
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by
the hardware that checks the line periodically, and if the line is connected
(the key at the remote station is down), 1 is recorded, and if the line is
not connected (remote key is up), 0 is recorded. After the message is fully
received, it gets to you for decoding as a string containing only
symbols 0 and 1.
"""

# This dictionary is supplied within the Codewars test suite.
# MORSE_CODE = {
#     '.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B',
#     '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
#     '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K',
#     '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M',
#     '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
#     '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q',
#     '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
#     '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"',
#     '-.--.': '(', '---..': '8', '...--': '3'
# }

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9',
              '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
              '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
              '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
              '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
              '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

#  my own work with help on line 63 from Daniel:


def decode_morse(morse_code):
    alfa_sentence = []
    morse_words = morse_code.split('   ')
    for word in morse_words:
        for letter in word.split():
            alfa_sentence.append(MORSE_CODE.get(letter))
        alfa_sentence.append(' ')
    print(''.join(alfa_sentence).strip())
#
# class group colaberation: but creating new string objects is not good

# def decodeMorse(morse_code):
#     morse_words = morse_code.split('   ')
#     decoded_words = ''
#     for morse_word in morse_words:
#         for morse_char in morse_word.split():
#             decoded_words += MORSE_CODE[morse_char]
#         decoded_words += ' '
#     return decoded_words.strip()

#  Daniel help refactor my code with list comprehentions:
# def decodeMorse(morse_code):
#     alfa_sentence = []
#     morse_words = morse_code.split('  ')
#     for word in morse_words:
#         letters = word.split()
#         alfa_sentence.append(
#             ''.join([MORSE_CODE.get(letter) for letter in letters]))
#     print(' '.join(alfa_sentence).strip())


# decodeMorse('.... . -.--   .--- ..- -.. .')


test = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
test2 = '1010101000'
test3 = '111000111000111000111000000000'
test4 = '1110111'
test5 = '01'
test6 = '1111111'
test7 = '0000000011110000000'


def find_mult(bits):
    """Finds least amount of occurrences of 0 or 1"""
    smallest_zeros = len(min([bit for bit in bits.split('1') if bit != '']))
    smallest_ones = len(min([bit for bit in bits.split('0') if bit != '']))
    return min(smallest_zeros, smallest_ones)


def decode_bits(bits):
    """Translate a string of 1's & 0's to dots and dashes"""
    bits = bits.strip('0')
    if '0' not in bits:
        t = len(bits)
    else:
        t = find_mult(bits)
    return str(bits.replace('111'*t, '-').replace('000'*t, ' ').replace('1' * t, '.').replace('0'*t, '').replace('0000000'*t, '   '))


decode_morse(decode_bits(test))
decode_morse(decode_bits(test2))
decode_morse(decode_bits(test3))
decode_morse(decode_bits(test4))
decode_morse(decode_bits(test5))
decode_morse(decode_bits(test6))
decode_morse(decode_bits(test7))
