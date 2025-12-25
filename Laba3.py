def read_file(filename, mode='all'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if mode == 'all':
                content = file.read()
                return content
            elif mode == 'line':
                strings = [line for line in file]
                return strings
            else:
                return "Ошибка: неизвестный режим чтения"
    except FileNotFoundError:
        return f"Файл '{filename}' не найден. Проверьте имя файла"

result = read_file('example.txt', 'line')

if type(result) == list:
    for line in result:
        print(line)
else:
    print(result)



def file_write(filename, mode='w'):
    text = input("Введите текст для записи в файл: ")
    with open(filename, mode, encoding='utf-8') as file:
        file.write(text)
    return f"Текст записан в файл '{filename}'!"

print(file_write('user_input.txt', 'w'))
print(file_write('user_input.txt', 'a'))
