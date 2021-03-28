if __name__ == '__main__':
    filename = 'repo/pi_million_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''

    for line in lines:
        pi_string += line.strip()

    birthday = input("Podaj datę swoich urodzin (w formacie ddmmrr): ")

    if birthday in pi_string:
        print("Twoja data urodzin znajduje się w pierwszym milionie cyfr liczby PI!")
    else:
        print("Twoja data urodzin nie znajduje się w pierwszym milionie cyfr liczby PI. :(")
