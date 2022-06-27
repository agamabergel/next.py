import functools

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(functools.reduce(lambda x, y: x + y, [chr(ord(letter) + 2) if letter.isalpha() else letter for letter in password]))


def check_win(secret_word, old_letters_guessed):
    return functools.reduce(lambda f, t: f and t, [False if letter not in old_letters_guessed else True for letter in secret_word])


    flag = True
    for i in secret_word:
        if i not in old_letters_guessed:
            flag = False

    return flag

if __name__ == "__main__":
    print(check_win('',['q']))
    print(check_win('typewriter',['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o']))
    print(check_win('typewriter',['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']))