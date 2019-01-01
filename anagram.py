def main():
    print("\nAnagram")
    next_try = True
    while next_try:
        source = input("podaj pierwszy tekst do zbadania: ")
        text = input("podaj drugi tekst do zbadania: ")
        if isAnagram(source, text):
            print(f"{text} jest anagramem {source}")
        else:
            print('Niestety nie :(')

        answer = input("\nChcesz sprawdzić inny tekst? [t/N]")
        if answer != 't':
            next_try = False


def isAnagram(source, text):
    source = source.lower()
    text = text.lower()
    for letter in text:
        if letter not in source:
            return False
    else:
        return True


def smartPower(base, index):
    if index>2:
        rest = index % 2
        index = int(index / 2)
        return smartPower(base, index) * smartPower(base, index) * base ** rest
    else:
        return base**index


if __name__ == "__main__":
    main()
