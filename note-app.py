import os

def build_note(note_text, note_name):
    with open(f'list_note/{note_name}.txt', 'w', encoding='utf-8') as file:
        file.write(note_text)
        print('Заметка ссздана')


def create_note():
    note_text = input('Введите текст заметки: ')
    note_name = input('Введите название заметки')
    build_note(note_text, note_name)


def read_note(note_name_search):

    if os.path.isfile(f'list_note/{note_name_search}') == True:
        with open(f'list_note/{note_name_search}.txt', 'r', encoding='utf-8') as file:
            for el in file:
                print(el)

    elif os.path.isfile(f'list_note/{note_name_search}') == False:
        print('Заметка не найдена')


def edit_note(note_name_edit):
    if os.path.isfile(f'list_note/{note_name_edit}') == True:
        with open(f'list_note/{note_name_edit}.txt', 'r', encoding='utf-8') as file:
            for el in file:
                print(el)
                # добавить возможность редактировать существующий текст например добавление в конец и тд
                # а так же полностью новый текст


def delete_note(name_delete_note):
    if os.path.isfile(f'list_note/{name_delete_note}') == True:
        os.remove(f'list_note/{name_delete_note}')
    elif os.path.isfile(f'list_note/{name_delete_note}') == False:
        print('Заметка не существует')
