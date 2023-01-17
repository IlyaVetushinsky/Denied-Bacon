import random


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # check it in input
open_text = 'MEPHI'


def create_key_map():
    letter_keys = list(range(0, 26))
    random.shuffle(letter_keys)
    counter = 0
    _key_map = {}
    for letter in letters:
        elem = ['0'] * 5
        letter_key = format(letter_keys[counter], 'b')
        pos = 4
        for n in reversed(letter_key):
            elem[pos] = n
            pos = pos - 1
        elem = "".join(elem)
        _key_map[letter] = elem
        counter = counter + 1
    return _key_map


def create_original_key():
    orig_key = {}
    counter = 1
    for letter in letters:
        orig_key[letter] = '0' if counter < 14 else '1'
        counter = counter + 1
    return orig_key


def encrypt_text_1_step(text, _key_map):
    res = []
    for letter in text:
        res += _key_map[letter]
    res = "".join(res)
    return res


def encrypt_text_2_step(text, _original_key):
    res = ""
    for number in text:
        letter = random.choice(letters)
        while _original_key[letter] != number:
            letter = random.choice(letters)
        res += letter
    return res


def decrypt_text_1_step(text, key):
    res = ""
    for letter in text:
        res += key[letter]
    return res


def decrypt_text_2_step(text, _key_map):
    res = ""
    left = 0
    right = 5
    while right <= len(text):
        seq = text[left:right]
        for letter in _key_map:
            if _key_map[letter] == seq:
                res += letter
        left = left + 5
        right = right + 5
    return res


def get_word(num, f):
    f.seek(get_word.position)
    word = f.readline()
    word = word[:-1]

    while word:
        word = word[:-1]
        if len(word) == num and word.isalpha():  # and word == "dog":
            break
        word = f.readline()
    else:
        get_word.position = 0
        return ""
    get_word.position = f.tell()
    return word.upper()


get_word.position = 0


def generate_fake_key_and_text(text, _key_map):
    is_correct = False
    _fake_key = {}
    _fake_text = ""
    encrypted_fake_text_1 = ""
    f = open('words.txt', 'r')
    while not is_correct:
        _fake_text = get_word(len(text) / 5, f)
        if _fake_text == "":
            f.close()
            return {}, "", ""
        _fake_key = {}
        encrypted_fake_text_1 = encrypt_text_1_step(_fake_text, _key_map)

        counter = 0
        flag = True
        for letter in text:
            if letter in _fake_key:
                if _fake_key[letter] != encrypted_fake_text_1[counter]:
                    flag = False
                    break
            _fake_key[letter] = encrypted_fake_text_1[counter]
            counter = counter + 1

        if flag:
            is_correct = True

    # adding for full key
    for letter in letters:
        if letter not in _fake_key:
            _fake_key[letter] = str(random.randint(0, 1))

    f.close()
    return _fake_key, _fake_text, encrypted_fake_text_1


'''
key_map = create_key_map()
print(key_map)
original_key = create_original_key()
print(original_key)

closed_text_1 = encrypt_text_1_step(open_text, key_map)
print(closed_text_1)

closed_text_2 = encrypt_text_2_step(closed_text_1, original_key)
print(closed_text_2)

decrypt_text_1 = decrypt_text_1_step(closed_text_2, original_key)
print(decrypt_text_1)

decrypt_text_2 = decrypt_text_2_step(decrypt_text_1, key_map)
print(decrypt_text_2)

fake_key, fake_text, closed_fake_text_1 = generate_fake_key_and_text(closed_text_2, key_map)
print('')
print(sorted(fake_key.items(), key=lambda x: x[0]))
print(fake_text)
print(closed_fake_text_1)

'''
