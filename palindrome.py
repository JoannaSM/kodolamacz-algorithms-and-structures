def main():
    print("\nPalindrom")
    dalej = True
    while dalej:
        text = input("podaj tekst do zbadania: ")
        if isPalindrome(text):
            print('Palindrom!!!')
        else:
            print('Niestety nie :(')

        answer = input("\nChcesz sprawdzić inny tekst? [t/N]")
        if answer != 't':
            dalej = False


def isPalindrome(text):
    number = len(text)
    half = int(number/2)
    text = text.lower()
    for index in range(1,half):
        if text[index-1] !=  text[-index]:
            return False
    else:
        return True


if __name__ == "__main__":
    main()
