#Caesar cipher 

This module demonstrates the Caesar cipher and a simple statistical method for cracking it.

There are three main methods and a few helpers

    def encrypt(k, message):
    """
    Input: message, a message to encrypt, and k, the number of letters to shift
    the message by
    Output: the ciphertext of the message, where each letter is shifted by the
    key k letters.
    """

    def decrypt(k, ciphertext):
    """
    Input: A ciphertext of a Caesar cipher-encrypted message and k, the number
    of letters the message was shifted by
    Output: the original message
    """

    def attack(ciphertext):
    """
    Input: The ciphertext of a Caesar cipher-encrypted message
    The function uses a statistical method to attack the ciphertext and predict
    what the original message was. 
    Output: A tuple: (the predicted value of the shift, the guess for the
    original message on which the ciphertext was based)
    """




