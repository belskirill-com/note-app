import os


def build_note(note_text, note_name):
    try:
        try:
            with open(f'list_note/{note_name}.txt', 'r+', encoding='utf-8') as file:
                file.write(note_text)
                print('Такая заметка уже существует!')
        except IOError:
            with open(f'list_note/{note_name}.txt', 'w+', encoding='utf-8') as file:
                file.write(note_text)
                print('Заметка создана')
    except Exception:
        print('Что то пошло не так! Попробуйте еще раз!')


def create_note():
    try:
        note_text = input('Введите текст заметки: ')
        note_name = input('Введите название заметки')
        build_note(note_text, note_name)
    except ValueError:
        print('Ошибка, попробуйте еще раз!')


def read_note():
    try:
        note_name_search = input('Введите название заметки которую хотите посмотреть!')
        if os.path.isfile(f'list_note/{note_name_search}.txt'):
            try:
                with open(f'list_note/{note_name_search}.txt', 'r', encoding='utf-8') as file:
                    for el in file:
                        print(el)
            except Exception:
                print('Произошла ошибка, попробуйте еще раз!')

        elif not os.path.isfile(f'list_note/{note_name_search}'):
            print('Заметка не найдена')
    except Exception:
        print('Произошла ошибка! Поробуйте еще раз!')


def edit_note():
    try:
        note_name_edit = input('Введите название заметки которую хотите редактировать')
        if os.path.isfile(f'list_note/{note_name_edit}.txt'):
            try:
                with open(f'list_note/{note_name_edit}.txt', 'r', encoding='utf-8') as file:
                    files = file.read()
                    print(files)
                try:
                    print('Что хотите сделать с заметкой?\n1.Добавить текст в конец\n2.Добавить полностью новый текст')
                    choice = int(input('Ваш выбор: '))
                    if choice == 1:
                        try:
                            text = input('Введите текст: ')
                            with open(f'list_note/{note_name_edit}.txt', 'a', encoding='utf-8') as file:
                                file.write(text)
                                print('Заметка обновлена')
                        except ValueError:
                            print('Ошибка!')

                    elif choice == 2:
                        try:
                            text = input('Введите текст: ')
                            with open(f'list_note/{note_name_edit}.txt', 'w', encoding='utf-8') as file:
                                file.write(text)
                                print('Заметка обновлена')
                        except ValueError:
                            print('Ошибка!')
                except Exception:
                    print('Произошла ошибка! Попробуйте еще раз!')
            except Exception:
                print('Произошла ошибка! Попробуйте еще раз!')
    except Exception:
        print('Произошла ошибка! Попробуйте еще раз!')


def delete_note():
    try:
        name_delete_note: str = input('\nВведите название заметки: ')
        if os.path.isfile(f'list_note/{name_delete_note}.txt'):
            try:
                os.remove(f'list_note/{name_delete_note}.txt')
                print(f'\nЗаметка "{name_delete_note}", удалена!\n')
            except Exception:
                print('Произошла ошибка!')
        elif not os.path.isfile(f'list_note/{name_delete_note}.txt'):
            print('\nТакой заметки не существует\n')
    except Exception:
        print('Произошла ошибка, попробуйте еще раз!')


def display_notes():
    if os.listdir('list_note/'):
        try:
            note = [note for note in os.listdir('list_note/') if note.endswith('.txt')]
            print(note)
        except Exception:
            print('Ошибка, попробуйте еще раз!')
    else:
        print('Список пуст')


def display_sorted_notes():
    try:
        note_sorted = [note for note in os.listdir('list_note/') if note.endswith('.txt')]
        sorted_list = sorted(note_sorted, key=len)
        print('Отсортированный список заметок \n', sorted_list)
    except Exception:
        print('Произошла ошибка!')


def main():
    while True:
        print(
            'Выберите действие:\n\n1.Добавить заметку\n2.Удалить заметку\n3.Посмотреть заметку\n'
            '4.Редактировать заметку\n5.Посмотреть все заметки\n6.Посмотреть заметки в отсортированном виде\n'
        )
        try:
            choice = int(input('Что хотите сделать?: '))
            if choice == 1:
                create_note()

            elif choice == 2:
                delete_note()

            elif choice == 3:
                read_note()

            elif choice == 4:
                edit_note()

            elif choice == 5:
                display_notes()

            elif choice == 6:
                display_sorted_notes()
            else:
                print('\nТакого варианта не существует\n')
        except ValueError:
            print('\nОшибка, попробуйте еще раз!\n')

        print("Чтобы продолжить работать с заметками, нажмите y/n")

        answer = input().lower()
        if answer != "y":
            break


main()
