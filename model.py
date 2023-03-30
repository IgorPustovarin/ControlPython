
zametki = []
path = 'zametki.txt'

def open_file():
    global zametki
    global path
    with open(path, 'r', encoding = 'UTF-8') as data:
        file = data.readlines()
    for notes in file:
        zametki.append(notes.strip().split(';'))
    # print(zametki)

def get_zametki():
    global zametki
    return zametki

def add_new_notes(new_notes: list):
    global zametki
    zametki.append(new_notes)

def save_file():
    global zametki
    global path
    zm_str = []
    for notes in zametki:
        zm_str.append(';'.join(notes))  
    with open(path, 'w', encoding = 'UTF-8') as data:
        data.write('\n'.join(zm_str))

def get_notes(text: str):
    global zametki
    result = []
    for i, notes in enumerate(zametki):
        for field in notes:
            if text in field:
                result.append((notes, i))
    if len(result) > 1:
        return False
    else:
        return result
    
def delete_notes(notes: list):
    global zametki
    zametki.remove(notes)

def change_notes(index: int, new: list):
    global zametki
    zametki[index][0] = new[0] if new[0] != '' else zametki[index][0]
    zametki[index][1] = new[1] if new[1] != '' else zametki[index][0]
    zametki[index][2] = new[2] if new[2] != '' else zametki[index][0]
    zametki[index][3] = new[3]