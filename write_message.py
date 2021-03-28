if __name__ == '__main__':
    filename = 'programming.txt'

    with open(filename, 'w') as file_object:
        file_object.write("Uwielbiam programować.\n")
        file_object.write("Uwielbiam tworzyć nowe gry.\n")