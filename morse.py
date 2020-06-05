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
And in fact different
operators would transmit at different speed. An amateur person may need a few seconds to
transmit a single character, a skilled professional can transmit 60 words per minute,
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by the hardware
that checks the line periodically, and if the line is connected (the key at the remote
station is down), 1 is recorded, and if the line is not connected (remote key is up),
0 is recorded. After the message is fully received, it gets to you for decoding as a
string containing only symbols 0 and 1.
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


# def decodeMorse(morse_code):
#     alfa_sentence = []
#     morse_words = morse_code.split('   ')
#     for word in morse_words:
#         for letter in word.split():
#             alfa_sentence.append(MORSE_CODE.get(letter))
#         alfa_sentence.append(' ')
#     print(''.join(alfa_sentence).strip())


def decodeMorse(morse_code):
    alfa_sentence = []
    morse_words = morse_code.split('  ')
    for word in morse_words:
        letters = word.split()
        alfa_sentence.append(
            ''.join([MORSE_CODE.get(letter) for letter in letters]))
    print(' '.join(alfa_sentence).strip())


# decodeMorse('.... . -.--   .--- ..- -.. .')
test = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
test2 = '1010101000'
test3 = '111000111000111000111000000000'
test4 = '1110111'
test5 = '01'


def decode_bits(bits):
    a = bits.find('1')  # 0
    b = bits.find('0')  # 2
    if '0' in bits and a == 0:
        print(str(bits.replace('111'*b, '-').replace('000'*b, ' ')
                  .replace('1'*b, '.').replace('0'*b, '').replace('0000000'*b, '   ')))
    else:
        print(str(bits.replace('1', '.').replace('111', '-').replace('0', '')))
    #     return str(bits.replace('111', '-').replace('000', ' ')
    #                .replace('1', '.').replace('0', '').replace('0000000', '   '))

    # c = bits.slice[a:b]  # 11
    #     l = bits.split('00')
    # l = bits.split('0')
    # print(l)
    # for i, s in enumerate(l):

    #     if s == '':
    #         m.append('')
    # '1' or '11':
    #     m.append('.')
    # elif s == '111' or '111111':
    #     m.append('-')
    # elif s == '1' or '11':
    #     m.append('.')
    # '':
    #     m.append('')


decode_bits(test)
decode_bits(test2)
decode_bits(test3)
decode_bits(test4)
decode_bits(test5)


def find_mult(bits):
    """Finds least amount of occurrences of 0 or 1"""
    # raise NotImplementedError("Please implement this")
    pass


def decodeBits(bits):
    """Translate a string of 1's & 0's to dots and dashes"""
    # raise NotImplementedError("Please implement this")
    pass


def decodeMorse(morse_code):
    """Translates a string of dots and dashes to human readable text"""
    # raise NotImplementedError("Please implement this")
    pass
