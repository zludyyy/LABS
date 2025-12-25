def read_file(namefile, mode = 'all'):
    try:
        if mode == 'all':
            with open(namefile, 'r', encoding='utf-8') as file:
                content = file.read()
                return(content)
        elif mode == 'line':
            with open(namefile, 'r', encoding='utf-8') as file:
                for line in file:
                    return(line)
        else:
            print("Неизвестный тип чтения")
    except FileNotFoundError:
        print("Ошибка: файл не найден")