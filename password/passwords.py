import os

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "~"]

# File names
Dictionary_file = "wordlist.txt"
Top_passwords_file = "toppasswords.txt"

# The main function
def main():
    """
    This function is to continuesly get input from the user until they
    choose to quit.
    """

    print("---- HELLO!, Welcome To Your Password Strength Checker ----")

    while True:
        password = input("\nEnter your password (or type 'q' or 'Q' to quit): ")

        if password.lower() != 'q':
            strength = password_strength(password)
            print(f"Strength score: {strength}")

        else:
            print("Thank You and Goodbye!")
            break


def word_in_file(word, filename, case_sensitive=False):
    """
    This function is to check and read files to see if there are existing
    files or words within it
    """

    if not os.path.exists(filename):
        return False
    
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True
    return False

def word_has_character(word, character_list):
    """
    Checks if any character in the input word exists in the character_list.
    """

    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """
    Calculates the complexity of a word (0-4) based on character types.
    """

    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, Dictionary_file) or word_in_file(password, Top_passwords_file):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Strong length
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity. The password is strong.")
        return 5

    # Too short
    if len(password) < min_length:
        print("Password is too short and is insecure.")
        return 1

    # Complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity

    print(f"Password complexity score is {complexity}. Strength is {strength}.")
    return strength



# Call the main function to execute you program.
if __name__ == "__main__":
    main()