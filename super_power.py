def main():
    print("Sprytne obliczanie potęgi")
    base = 2
    index = 9
    wynik = smartPower(base, index)
    print(f"{base}^{index} = {wynik} ")
    print("------------------------------")


def smartPower(base, index):
    if index>2:
        rest = index % 2
        index = index // 2
        return smartPower(base, index) * smartPower(base, index) * base ** rest
    else:
        return base**index


if __name__ == "__main__":
    main()
