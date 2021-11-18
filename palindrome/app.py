def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]

def run():
    palindrome = input("Type a word to verify if is palindrome: ")
    if is_palindrome(palindrome):
        print(palindrome + " is palindrome.")
    else:
        print(palindrome + " isn't palindrome.")

if __name__ == "__main__":
    run()