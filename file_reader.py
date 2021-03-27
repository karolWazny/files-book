if __name__ == '__main__':
    with open('pliki_tekstowe/pi_digits.txt') as file_object:
        contents = file_object.read()
    print(contents.rstrip())
