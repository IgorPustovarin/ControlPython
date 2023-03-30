import view
import model


def start():
    choise = ''
    while choise != 7:
        choise = view.main_menu()
        
        match choise:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:            
                view.show_notes(model.get_zametki())
            case 4:
                new_notes = list(view.create_new_notes())
                model.add_new_notes(new_notes)
            case 5:
                del_name = view.select_notes('Введите заголовок удаляемой заметки: ')
                notes = model.get_notes(del_name)
                if notes:
                    confirm = view.delete_confirm(notes)
                    if confirm:
                        model.delete_notes(notes[0][0])
                elif notes == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 6:
                name = view.select_notes('Введите заголовок изменяемой заметки: ')
                notes = model.get_notes(name)
                if notes:                   
                    changed_notes = view.change_notes()
                    model.change_notes(notes[0][1], list(changed_notes))
                elif notes == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 7:
                view.end_program()
            