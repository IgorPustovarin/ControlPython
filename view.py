import datetime

commands =['Открыть файл',
           'Сохранить файл',
           'Показать заметки',
           'Создать заметку',
           'Удалить заметку',
           'Изменить заметку',
           'Выход из программы']

def main_menu():
    print('Главное меню:')
    for i, item in enumerate(commands,1):
        print(f'\t{i}. {item}')
    while True:
        try:
            choise = int(input('Выберите пункт меню: '))
            if 0 < choise < 8:
                return choise
            else:
                print('Введите значение от 1 до 7 ')
        except ValueError:
            print('Введите корректный пункт меню: ')

def show_notes(notes_list: list):
    if len(notes_list) < 1:
        print('Заметок нет или не открыт файл')
    else:
        print('__________________________________________________________________')
        for i, notes in enumerate(notes_list, 1):
            print(f'\t{i}. {notes[0]} {notes[1]} {notes[2]} {notes[3]}')
        print('__________________________________________________________________')

def input_error():
    print('Ошибка ввода. Введите корректный пункт меню.')

def empty_request():
    print('Заметка не найдена ')

def many_request():
    print('Найдено много заметок, нужно уточнение ')

def create_new_notes():
    id = input('Введите ID заметки: ')
    head = input('Введите заголовок заметки: ')
    body = input('Введите основной текст заметки: ')
    t = datetime.datetime.now()
    time = str(t)
    return id, head, body, time

def end_program():
    print('The End')

def select_notes(message: str):
    notes = input(message)
    return notes

def delete_confirm(notes: str):
    result = input(f'Подтвердите удаление {notes}? (y/n)').lower()
    if result == 'y':
        return True
    else:
        return False
    
def change_notes():
    print('Введите новые данные, если оставить данные нажмите Enter ')
    id = input('Введите ID заметки: ')
    head = input('Введите заголовок заметки: ')
    body = input('Введите основной текст заметки: ')
    t = datetime.datetime.now()
    time = str(t)
    return id, head, body, time