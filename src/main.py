import random
import string
from typing import List, Optional
import nltk
nltk.download('words')


def generate_pin(length: int) -> str:
    """
    Generate a numeric pin code.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def generate_random_password(length: int, include_num: bool, include_sym: bool) -> str:
    """
    Generate a random password.
    """
    if not include_num and not include_sym:
        reference = string.ascii_letters
    elif not include_num and include_sym:
        reference = string.punctuation + string.ascii_letters
    elif include_num and not include_sym:
        reference = string.ascii_letters + string.digits
    else:
        reference = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(random.choice(reference) for _ in range(length))


def generate_memorable_password(
    num_of_words: int,
    separator: str,
    capitalize: bool,
    vocabulary: Optional[list] = None
    ) -> str:
    """
        Generate a memorable password from a list of vocabulary words.
    """ 
    if vocabulary == None:
        reference = nltk.corpus.words.words() # edit this to any vocabulary list you want
    else:
        reference = vocabulary
     
    return separator.join(random.choice(reference).capitalize() if capitalize else random.choice(reference)
    for _ in range(num_of_words))


def test_random_password_generator():
    password = generate_random_password(10, True, True)
    print(password)
    assert len(password) == 10
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)


def test_memorable_password_generator():
    password = generate_memorable_password(4, '-', True)
    print(password)
    assert len(password.split('-')) == 4
    assert all(word[0].isupper() for word in password.split('-'))


def test_pin_generator():
    pin = generate_pin(4)
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def main():
    print("Testing Random Password Generator:")
    test_random_password_generator()
    print("Testing Memorable Password Generator:")
    test_memorable_password_generator()
    print("Testing Pincode Generator:")
    test_pin_generator()


if __name__ == "__main__":
    main()

