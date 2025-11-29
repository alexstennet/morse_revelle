from typing import List, Dict

dot = 1
dash = 3

sub_letter_space = 1
letter_space = 3
word_space = 7

alphabet: Dict[str, str] = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '...-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

reverse_alphabet = {value: key for key, value in alphabet.items()}

def parse_word(word: str) -> str:
    """Takes a string representation of morse code and parses it into human readable text
    
    Args:
        code: This is a string containing only dots and spaces. Ex: '... --- ...'

    Returns:
        The human readable translated text. Ex: 'sos'
    """
    output = ''
    letters = word.split(' ')
    for letter in letters:
        a = reverse_alphabet.get(letter, '')
        
        if not a:
            raise ValueError('Invalid letter')

        output += a
    return output

