from typing import List, Dict

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
    """Takes a string representation of word in morse code and parses it into human readable text
    
    Args:
        word: This is a string containing only dots and spaces.

    Returns:
        The human readable translated text. 

    Example: 
        >>> parse_word('... --- ...')
        'sos'
    """
    output = ''
    letters = word.split(' ')
    for letter in letters:
        a = reverse_alphabet.get(letter, '')
        
        if not a:
            raise ValueError('Invalid letter', letter)

        output += a
    return output

def parse(sentence: List[str]) -> str:
    """Takes a string representation of a morse code sentence and parses it into human readable text

    Args:
        sentence: This is a list of strings each representing a word in morse code

    Returns:
        A human readable sentence with spaces separating words
    
    Example:
        >>> parse(['.... . .-.. .-.. ---', '.-- --- .-. .-.. -..'])
        'hello world'
    """
    output = ''
    for word in sentence:
        output += ' ' + parse_word(word)
    return output.strip()
