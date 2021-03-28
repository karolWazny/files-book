if __name__ == '__main__':
    filename = 'programming.txt'

    with open(filename, 'a') as file_object:
        file_object.write("uwielbiam przetwarzać ogromne zbiory danych.\n")
        file_object.write("Uwielbiam tworzyć aplikacje webowe.\n")