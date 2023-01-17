from tkinter import *
from bacon import *
import re

key_map = {}
original_key = {}
closed_text = ""


# Создаем главный объект (по сути окно приложения)
root = Tk()


# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    # Получаем данные от пользователя
    # city = cityField.get()
    info['text'] = "Ты нажал кнопку"

    # Полученные данные добавляем в текстовую надпись для отображения пользователю
    #info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


def autogen():
    global key_map
    global original_key
    global key_map_fields
    global orig_key_fields
    key_map = create_key_map()
    original_key = create_original_key()

    counter = 0
    for bincode in key_map:
        key_map_fields[counter].delete(0, 'end')
        key_map_fields[counter].insert(0, key_map[bincode])
        counter = counter + 1

    counter = 0
    for letter in original_key:
        orig_key_fields[counter].delete(0, 'end')
        orig_key_fields[counter].insert(0, original_key[letter])
        counter = counter + 1


def encrypt():
    global key_map
    global original_key
    global key_map_fields
    global orig_key_fields

    counter = 0
    for field in key_map_fields:
        # проверка на 10011 if field.get()
        if len(field.get()) != 5 or not re.fullmatch(r'[0-1]+', field.get()):
            print("nm")
            return
        key_map[letters[counter]] = field.get()
        counter = counter + 1

    counter = 0
    for field in orig_key_fields:
        # проверка на 1 if field.get()
        if len(field.get()) != 1 or not re.fullmatch(r'[0-1]', field.get()):
            print("nm")
            return
        original_key[letters[counter]] = field.get()
        counter = counter + 1

    text = openTextField.get()
    if text is None or not text.isalpha():
        print("nm")
        return

    closed_text_1 = encrypt_text_1_step(text, key_map)
    closed_text_2 = encrypt_text_2_step(closed_text_1, original_key)

    global closed_text
    closed_text = closed_text_2

    cryptogram.delete(0, 'end')
    cryptogram.insert(0, closed_text_2)


def decrypt():
    global key_map
    global original_key
    global key_map_fields
    global orig_key_fields

    counter = 0
    for field in key_map_fields:
        # проверка на 10011 if field.get()
        if len(field.get()) != 5 or not re.fullmatch(r'[0-1]+', field.get()):
            print("nm")
            return
        key_map[letters[counter]] = field.get()
        counter = counter + 1

    counter = 0
    for field in orig_key_fields:
        # проверка на 1 if field.get()
        if len(field.get()) != 1 or not re.fullmatch(r'[0-1]', field.get()):
            print("nm")
            return
        original_key[letters[counter]] = field.get()
        counter = counter + 1

    text = encrTextField.get()
    if text is None or not text.isalpha() or not len(text) % 5 == 0:
        print("nm")
        return

    decrypt_text_1 = decrypt_text_1_step(text, original_key)
    decrypt_text_2 = decrypt_text_2_step(decrypt_text_1, key_map)

    source_text.delete(0, 'end')
    source_text.insert(0, decrypt_text_2)


def fake_mes():
    global key_map
    global original_key
    global key_map_fields
    global orig_key_fields

    counter = 0
    for field in key_map_fields:
        # проверка на 10011 if field.get()
        if len(field.get()) != 5 or not re.fullmatch(r'[0-1]+', field.get()):
            print("nm")
            return
        key_map[letters[counter]] = field.get()
        counter = counter + 1

    counter = 0
    for field in orig_key_fields:
        # проверка на 1 if field.get()
        if len(field.get()) != 1 or not re.fullmatch(r'[0-1]', field.get()):
            print("nm")
            return
        original_key[letters[counter]] = field.get()
        counter = counter + 1

    if closed_text == "":
        print("nm")
        return

    _fake_key, _fake_text, closed_fake_text_1 = generate_fake_key_and_text(closed_text, key_map)

    fake_text.delete(0, 'end')
    fake_text.insert(0, _fake_text)

    fake_encr.delete(0, 'end')
    fake_encr.insert(0, closed_fake_text_1)

    cryptogram2.delete(0, 'end')
    cryptogram2.insert(0, closed_text)

    counter = 0
    for letter in _fake_key:
        fake_key_fields[counter].delete(0, 'end')
        fake_key_fields[counter].insert(0, _fake_key[letter])
        counter = counter + 1


# Настройки главного окна

# Указываем фоновый цвет
root['bg'] = '#e7e7e4'
# Указываем название окна
root.title('Программная реализация шифра Бэкона в режиме отрицаемого шифрования')
# Указываем размеры окна
root.geometry('1000x650')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка


frame_letter_key = Frame(root, bg='#8ccb5e', bd=5)
# Также указываем его расположение
frame_letter_key.place(relx=0.05, rely=0.02, relwidth=0.07, relheight=0.05)
info = Label(frame_letter_key, text='BinCode', bg='#8ccb5e', font=20)
info.pack()

frame = Frame(root, bg='#8ccb5e', bd=5)
# Также указываем его расположение
frame.place(relx=0.13, rely=0.02, relwidth=0.04, relheight=0.05)
info = Label(frame, text='Key', bg='#8ccb5e', font=20)
info.pack()

key_map_fields = []
orig_key_fields = []
ry = 0.08
for i in range(13):
    frame_letter = Frame(root, bg='#8ccb5e', bd=5)
    # Также указываем его расположение
    frame_letter.place(relx=0.01, rely=ry, relwidth=0.03, relheight=0.05)
    info = Label(frame_letter, text=letters[i], bg='#8ccb5e', font=40)
    info.pack()

    frame_letter_key = Frame(root, bg='#8ccb5e', bd=5)
    # Также указываем его расположение
    frame_letter_key.place(relx=0.05, rely=ry, relwidth=0.07, relheight=0.05)
    # Создаем текстовое поле для получения данных от пользователя
    letterKeyField = Entry(frame_letter_key, bg='white', font=30)
    letterKeyField.pack()  # Размещение этого объекта, всегда нужно прописывать
    key_map_fields.append(letterKeyField)

    frame = Frame(root, bg='#8ccb5e', bd=5)
    # Также указываем его расположение
    frame.place(relx=0.13, rely=ry, relwidth=0.04, relheight=0.05)
    # Создаем текстовое поле для получения данных от пользователя
    origKeyField = Entry(frame, bg='white', font=30)
    origKeyField.pack()  # Размещение этого объекта, всегда нужно прописывать
    orig_key_fields.append(origKeyField)

    ry = ry + 0.06

frame_letter_key = Frame(root, bg='#8ccb5e', bd=5)
# Также указываем его расположение
frame_letter_key.place(relx=0.23, rely=0.02, relwidth=0.07, relheight=0.05)
info = Label(frame_letter_key, text='BinCode', bg='#8ccb5e', font=20)
info.pack()

frame = Frame(root, bg='#8ccb5e', bd=5)
# Также указываем его расположение
frame.place(relx=0.31, rely=0.02, relwidth=0.04, relheight=0.05)
info = Label(frame, text='Key', bg='#8ccb5e', font=20)
info.pack()

ry = 0.08
for i in range(13):
    frame_letter = Frame(root, bg='#8ccb5e', bd=5)
    # Также указываем его расположение
    frame_letter.place(relx=0.19, rely=ry, relwidth=0.03, relheight=0.05)
    info = Label(frame_letter, text=letters[i+13], bg='#8ccb5e', font=40)
    info.pack()

    frame_letter_key = Frame(root, bg='#8ccb5e', bd=5)
    # Также указываем его расположение
    frame_letter_key.place(relx=0.23, rely=ry, relwidth=0.07, relheight=0.05)
    # Создаем текстовое поле для получения данных от пользователя
    letterKeyField = Entry(frame_letter_key, bg='white', font=30)
    letterKeyField.pack()  # Размещение этого объекта, всегда нужно прописывать
    key_map_fields.append(letterKeyField)

    frame = Frame(root, bg='#8ccb5e', bd=5)
    # Также указываем его расположение
    frame.place(relx=0.31, rely=ry, relwidth=0.04, relheight=0.05)
    # Создаем текстовое поле для получения данных от пользователя
    origKeyField = Entry(frame, bg='white', font=30)
    origKeyField.pack()  # Размещение этого объекта, всегда нужно прописывать
    orig_key_fields.append(origKeyField)

    ry = ry + 0.06

# Создаем кнопку и при нажатии будет срабатывать метод "autogen"
frame = Frame(root, bg='#8ccb5e', bd=5)
frame.place(relx=0.05, rely=ry, relwidth=0.25, relheight=0.05)
btn = Button(frame, text='Сгенерировать автоматически', command=autogen)
btn.pack()

# Создаем поле для ввода открытого текста
frame_letter_key = Frame(root, bg='#8ccb5e', bd=5)
frame_letter_key.place(relx=0.4, rely=0.15, relwidth=0.09, relheight=0.05)
info = Label(frame_letter_key, text='Исх. текст', bg='#8ccb5e', font=20)
info.pack()

frame = Frame(root, bg='#8ccb5e', bd=5)
frame.place(relx=0.5, rely=0.15, relwidth=0.2, relheight=0.05)
openTextField = Entry(frame, bg='white', font=30)
openTextField.pack()

# Создаем кнопку зашифрования
frame = Frame(root, bg='#8ccb5e', bd=5)
frame.place(relx=0.5, rely=0.21, relwidth=0.1, relheight=0.05)
btn = Button(frame, text='Зашифровать', command=encrypt)
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться криптограмма
frame = Frame(root, bg='#8ccb5e', bd=5)
frame.place(relx=0.4, rely=0.27, relwidth=0.09, relheight=0.05)
info = Label(frame, text='Шифртекст', bg='#8ccb5e', font=40)
info.pack()

frame = Frame(root, bg='#8ccb5e', bd=5)
frame.place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.05)
cryptogram = Entry(frame, bg='white', font=30)
cryptogram.pack()

# Создаем поле для ввода шифртекста
frame_letter_key = Frame(root, bg='#f0a74f', bd=5)
frame_letter_key.place(relx=0.4, rely=0.33, relwidth=0.09, relheight=0.05)
info = Label(frame_letter_key, text='Шифртекст', bg='#f0a74f', font=20)
info.pack()

frame = Frame(root, bg='#f0a74f', bd=5)
frame.place(relx=0.5, rely=0.33, relwidth=0.2, relheight=0.05)
encrTextField = Entry(frame, bg='white', font=30)
encrTextField.pack()

# Создаем кнопку расшифрования
frame = Frame(root, bg='#f0a74f', bd=5)
frame.place(relx=0.5, rely=0.39, relwidth=0.1, relheight=0.05)
btn = Button(frame, text='Расшифровать', command=decrypt)
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться исходный текст
frame = Frame(root, bg='#f0a74f', bd=5)
frame.place(relx=0.4, rely=0.45, relwidth=0.09, relheight=0.05)
info = Label(frame, text='Исх. текст', bg='#f0a74f', font=40)
info.pack()

frame = Frame(root, bg='#f0a74f', bd=5)
frame.place(relx=0.5, rely=0.45, relwidth=0.2, relheight=0.05)
source_text = Entry(frame, bg='white', font=30)
source_text.pack()

# Создаем кнопку создания ложного сообщения
frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.45, rely=0.65, relwidth=0.2, relheight=0.05)
btn = Button(frame, text='Сгенерировать ложный текст', command=fake_mes)
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться ложный текст
frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.4, rely=0.71, relwidth=0.09, relheight=0.05)
info = Label(frame, text='Лож. текст', bg='#ff7a5c', font=40)
info.pack()

frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.5, rely=0.71, relwidth=0.2, relheight=0.05)
fake_text = Entry(frame, bg='white', font=30)
fake_text.pack()

# Создаем текстовую надпись, в которую будет выводиться зашифрованный на 1 этапе ложный текст
frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.4, rely=0.77, relwidth=0.09, relheight=0.05)
info = Label(frame, text='Лож. шифр', bg='#ff7a5c', font=40)
info.pack()

frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.5, rely=0.77, relwidth=0.2, relheight=0.05)
fake_encr = Entry(frame, bg='white', font=30)
fake_encr.pack()

# Создаем текстовую надпись, в которую будет выводиться криптограмма 2
frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.4, rely=0.83, relwidth=0.09, relheight=0.05)
info = Label(frame, text='Шифртекст', bg='#ff7a5c', font=40)
info.pack()

frame = Frame(root, bg='#ff7a5c', bd=5)
frame.place(relx=0.5, rely=0.83, relwidth=0.2, relheight=0.05)
cryptogram2 = Entry(frame, bg='white', font=30)
cryptogram2.pack()

fake_key_fields = []
ry = 0.08
for i in range(13):
    frame_letter = Frame(root, bg='#ff7a5c', bd=5)
    # Также указываем его расположение
    frame_letter.place(relx=0.8, rely=ry, relwidth=0.03, relheight=0.05)
    info = Label(frame_letter, text=letters[i], bg='#ff7a5c', font=40)
    info.pack()

    frame = Frame(root, bg='#ff7a5c', bd=5)
    # Также указываем его расположение
    frame.place(relx=0.84, rely=ry, relwidth=0.04, relheight=0.05)
    # Создаем текстовое поле для получения данных от пользователя
    fakeKeyField = Entry(frame, bg='white', font=30)
    fakeKeyField.pack()  # Размещение этого объекта, всегда нужно прописывать
    fake_key_fields.append(fakeKeyField)

    ry = ry + 0.06

frame = Frame(root, bg='#ff7a5c', bd=5)
# Также указываем его расположение
frame.place(relx=0.84, rely=0.02, relwidth=0.04, relheight=0.05)
info = Label(frame, text='FK', bg='#ff7a5c', font=20)
info.pack()

ry = 0.08
for i in range(13):
    frame_letter = Frame(root, bg='#ff7a5c', bd=5)
    # Также указываем его расположение
    frame_letter.place(relx=0.89, rely=ry, relwidth=0.03, relheight=0.05)
    info = Label(frame_letter, text=letters[i+13], bg='#ff7a5c', font=40)
    info.pack()

    frame = Frame(root, bg='#ff7a5c', bd=5)
    # Также указываем его расположение
    frame.place(relx=0.93, rely=ry, relwidth=0.04, relheight=0.05)
    # Создаем текстовое поле для получения данных от пользователя
    fakeKeyField = Entry(frame, bg='white', font=30)
    fakeKeyField.pack()  # Размещение этого объекта, всегда нужно прописывать
    fake_key_fields.append(fakeKeyField)

    ry = ry + 0.06

frame = Frame(root, bg='#ff7a5c', bd=5)
# Также указываем его расположение
frame.place(relx=0.93, rely=0.02, relwidth=0.04, relheight=0.05)
info = Label(frame, text='FK', bg='#ff7a5c', font=20)
info.pack()



# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()
