"""morse_converter.py

module responsible for converting between plain text and morse
"""

TEXT_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

MORSE_TO_TEXT = new_dict = dict(zip(TEXT_TO_MORSE.values(), TEXT_TO_MORSE.keys()))


def encrypt(message: str) -> str:
    """Encrypts a given string to morse code

    :param message: Text to be encrypted as morse code
    :return: Message encrypted as morse code
    """
    if not isinstance(message, str):
        raise ValueError(f"Message must be of type str. Type {type(message)} given.")

    encrypted_message = ""
    for word in message.split(" "):
        for letter in word.upper():
            try:
                encrypted_message += TEXT_TO_MORSE[letter]
            except KeyError as exc:
                raise KeyError(f"Character {letter} cannot be encrypted.") from exc
            encrypted_message += "   "
        encrypted_message += "    "
    return encrypted_message[:-7]


def decrypt(encrypted_message: str) -> str:
    """Decrypts a message from morse code

    :param encrypted_message: Morse code message to decrypt
    :return: Morse code message decrypted to plain text
    """
    if not isinstance(encrypted_message, str):
        raise ValueError(f"Message must be of type str. Type {type(encrypted_message)} given.")

    decrypted_message = ""
    for word in encrypted_message.split("       "):
        for letter in word.split("   "):
            try:
                decrypted_message += MORSE_TO_TEXT[letter]
            except KeyError as exc:
                raise KeyError(f"Value {letter} cannot be decrypted.") from exc
        decrypted_message += " "
    return decrypted_message[:-1].lower()
