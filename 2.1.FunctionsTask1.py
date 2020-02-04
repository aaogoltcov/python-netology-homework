documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "9999", "name": ""},
    {"type": "passport", "number": "7777"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
# Задача №2:
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

def person_name_show(command_line):

    # Команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    document_number = str(input("Введите номер документа: "))
    if not document_number:
        print('Вы ввели пустое значение...')
    else:
        document_found = 0
        for document in documents:
            for key, value in document.items():
                if document_number == value:

                    # Исключение для document['name']
                    try:
                        if document['name'] != "":
                            print(document['name'])
                        else:
                            print('У документа поле "name" - пустое ...')
                    except KeyError:
                        print('У документа отсуствует поле "name" ...')

                    document_found = 1
        if document_found == 0:
            print('К сожалению, такого документа нет...')

def documents_show(command_line):

    # Команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    for document in documents:

        # Исключение для document['name']
        try:
            if document['name'] != "":
                print(document['number'], document['name'])
            else:
                print(f"{document['number']} - у документа поле 'name' пустое")
        except KeyError:
            print(f"{document['number']} - у документа отсуствует поле 'name'")


def shelf_number(command_line):

    # Команда, которая спросит номер документа и выведет номер полки, на которой он находится
    document_number = str(input("Введите номер документа: "))
    if not document_number:
        print('Вы ввели пустое значение...')
    else:
        for key, value in directories.items():
            shelf_get_key = 0
            for numbers in value:
                if document_number in value:
                    print('Номер полки: ', key)
                    shelf_get_key = 1
                    break
            if shelf_get_key == 1:
                break
        if shelf_get_key == 0:
                print('Извините, такого документа нет...')

def new_document(command_line):

    # Команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
    document_type = str(input("Введите тип документа: "))
    document_number = str(input("Введите номер документа: "))
    person_name = str(input("Введите ФИО на кого зарегестрирован документ: "))
    shelf_number = str(input("Введите номер полки для хранения (числом): "))

    if not document_type or not document_number or not person_name or not shelf_number:
        print('Вы ввели пустое значение...')
    else:
        # Проверка наличия полки и запись новых данных
        shelf_exist = 0
        for key in directories.keys():
            if shelf_number in key:
                shelf_exist = 1

        if shelf_exist == 1:
            for key, value in directories.items():
                if key == shelf_number:
                    value.append(document_number)
            documents.append({"type": document_type, "number": document_number, "name": person_name})
            print('Спасибо, данные обновлены')
        else:
            print('Извините, такой полки не существует, сначала создайте полку...')

def document_delete(command_line):

    # Команда, которая спросит номер документа и удалит его из каталога и из перечня полок
    document_number = str(input("Введите номер документа: "))
    if not document_number:
        print('Вы ввели пустое значение...')
    else:
        for directory in documents:
            for key, value in directory.items():
                if value == document_number:
                    directory.clear()
                    documents.remove({})
                    break
        for key, value in directories.items():
            if document_number in value:
                value.remove(document_number)
        print("Документ удален из документов и с полки")

def document_move(command_line):

    # Команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
    document_number = str(input("Введите номер документа для переноса: "))
    shelf_number = str(input("Введите номер полки куда перенести документ (числом): "))
    if not document_number or not shelf_number:
        print('Вы ввели пустое значение...')
    else:

        # Проверка наличия документа
        document_exist = 0
        for key, value in directories.items():
            if document_number in value:
                document_exist = 1
        if document_exist == 0:
            print('Указанный документ не существует...')

        # Удаление документа
        if document_exist == 1:
            for key, value in directories.items():
                if document_number in value:
                    value.remove(document_number)

        # Проверка наличия полки и запись новых данных
        shelf_exist = 0
        for key in directories.keys():
            if shelf_number in key:
                shelf_exist = 1

        # Перенос документа на полку
        if shelf_exist == 1 and document_exist == 1:
            for key, value in directories.items():
                if key == shelf_number:
                    value.append(document_number)
            print('Спасибо, данные обновлены')
        elif shelf_exist == 0:
            print('Извините, такой полки не существует, сначала создайте полку...')

def shelf_new(command_line):

    # Команда, которая спросит номер новой полки и добавит ее в перечень
    shelf_number = str(input("Введите номер новой полки (числом): "))
    if not shelf_number:
        print('Вы ввели пустое значение...')
    else:
        shelf_exist = 0
        for key in directories.keys():
            if shelf_number in key:
                shelf_exist = 1
        if shelf_exist == 1:
            print('Такая полка уже существует, попробуйте еще раз...')
        else:
            directories.update({shelf_number: []})
            print('Спасибо, данные обновлены')


def main():

    # Главная функция выхова программы
    command_line = str()
    while command_line != 'q':
        command_line = str(input("Вы работаете с каталогом документов, введите пожалуйста команду (для выхода нажмите q): "))
        if command_line == 'p':
            person_name_show(command_line)
        elif command_line == 'l':
            documents_show(command_line)
        elif command_line == 's':
            shelf_number(command_line)
        elif command_line == 'a':
            new_document(command_line)
        elif command_line == 'd':
            document_delete(command_line)
        elif command_line == 'm':
            document_move(command_line)
        elif command_line == 'as':
            shelf_new(command_line)
        elif command_line == 'q':
            print('Выхожу из программы!')
            break

main()

