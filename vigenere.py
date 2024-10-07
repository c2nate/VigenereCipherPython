import sys  # Import sys module to handle command-line arguments and exit behavior

def vigenere_encrypt(key, plaintext):
    """
    Encrypts the plaintext using the Vigenère cipher algorithm.
    
    Parameters:
    key (str): The encryption key (alphabetic string).
    plaintext (str): The text to be encrypted.

    Returns:
    str: The encrypted text (ciphertext).
    
    The function works by shifting each character of the plaintext by an amount determined
    by the corresponding character in the key. Non-alphabetic characters are not altered.
    """
    ciphertext = []  # List to hold the encrypted characters
    key_length = len(key)  # Length of the key
    key_index = 0  # Index to track position in the key

    # Loop through each character in the plaintext
    for char in plaintext:
        if char.isalpha():  # Only process alphabetic characters
            # Get the current key character and convert it to lowercase
            key_char = key[key_index % key_length].lower()
            # Calculate the shift value based on the key character ('a' is 0, 'b' is 1, etc.)
            shift = ord(key_char) - ord('a')

            # Normalize the plaintext character to lowercase
            normalized_char = char.lower()
            # Encrypt the character using the Vigenère shift formula
            encrypted_char = chr(((ord(normalized_char) - ord('a') + shift) % 26) + ord('a'))
            # Append the encrypted character to the ciphertext list
            ciphertext.append(encrypted_char)
            key_index += 1  # Move to the next key character
        else:
            # If the character is not alphabetic, append it unchanged
            ciphertext.append(char)

    # Join the list of characters into a single string and return it
    return ''.join(ciphertext)

def vigenere_decrypt(key, ciphertext):
    """
    Decrypts the ciphertext using the Vigenère cipher algorithm.
    
    Parameters:
    key (str): The decryption key (alphabetic string).
    ciphertext (str): The text to be decrypted.

    Returns:
    str: The decrypted text (original plaintext).
    
    The function works by shifting each character of the ciphertext backwards
    by an amount determined by the corresponding character in the key.
    Non-alphabetic characters are not altered.
    """
    decrypted_text = []  # List to hold the decrypted characters
    key_length = len(key)  # Length of the key
    key_index = 0  # Index to track position in the key

    # Loop through each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():  # Only process alphabetic characters
            # Get the current key character and convert it to lowercase
            key_char = key[key_index % key_length].lower()
            # Calculate the shift value based on the key character ('a' is 0, 'b' is 1, etc.)
            shift = ord(key_char) - ord('a')

            # Normalize the ciphertext character to lowercase
            normalized_char = char.lower()
            # Decrypt the character using the reverse Vigenère shift formula
            decrypted_char = chr(((ord(normalized_char) - ord('a') - shift + 26) % 26) + ord('a'))
            # Append the decrypted character to the decrypted_text list
            decrypted_text.append(decrypted_char)
            key_index += 1  # Move to the next key character
        else:
            # If the character is not alphabetic, append it unchanged
            decrypted_text.append(char)

    # Join the list of characters into a single string and return it
    return ''.join(decrypted_text)

# Main entry point for the program
if __name__ == "__main__":
    """
    Main function to handle command-line input and output.
    
    Expects two command-line arguments:
    1. key: The encryption key (alphabetic string).
    2. plaintext: The text to be encrypted.

    The program encrypts the plaintext using the Vigenère cipher and prints the ciphertext.
    It then decrypts the ciphertext using the same key and prints the decrypted text.
    """
    if len(sys.argv) != 3:  # Check if the correct number of arguments is provided
        print("Usage: python vigenere.py <key> <plaintext>")
        sys.exit(1)  # Exit with an error if the number of arguments is incorrect

    key = sys.argv[1]  # First argument is the encryption key
    plaintext = sys.argv[2]  # Second argument is the plaintext to encrypt

    # Ensure the key contains only alphabetic characters (no spaces or numbers)
    if not key.isalpha():
        print("Key can only contain English alphabetical letters with no whitespace.")
        sys.exit(1)  # Exit with an error if the key is invalid

    # Encrypt the plaintext and print the result
    ciphertext = vigenere_encrypt(key, plaintext)
    print("CipherText: ", ciphertext)

    # Decrypt the ciphertext and print the result
    decrypted_text = vigenere_decrypt(key, ciphertext)
    print("Decrypted text: ", decrypted_text)
