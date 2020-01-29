documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

def person_name_show(command_line):
    for document in documents:
        document_number = str(input("Введите номер документа (для выхода нажмите q): "))
        if document_number != "q":
            print(document['name'])
        else:
            break

def documents_show(command_line):
    for document in documents:
        print(document['number'], document['name'])

def shelf_number(command_line):
    document_number = str(input("Введите номер документа: "))
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
            print('Извините, такого документа нет')

def new_document(command_line):
    document_type = str(input("Введите тип документа: "))
    document_number = str(input("Введите номер документа: "))
    person_name = str(input("Введите ФИО на кого зарегестрирован документ: "))
    shelf_number = str(input("Введите номер полки для хранения (числом): "))
    documents.append({"type": document_type, "number": document_number, "name": person_name})
    for key, value in directories.items():
        if key == shelf_number:
            value.append(document_number)
    print(f'Спасибо, данные обновлены: \n {documents} \n {directories}')

def main():
    for document in documents:
        command_line = str(input("Вы работаете с каталогом документов, введите пожалуйста команду (для выхода нажмите q): "))
        if command_line == 'p':
            person_name_show(command_line)
        elif command_line == 'l':
            documents_show(command_line)
        elif command_line == 's':
            shelf_number(command_line)
        elif command_line == 'add':
            new_document(command_line)
        elif command_line == 'q':
            break
main()

