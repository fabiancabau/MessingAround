from random import randrange

def _generate_unique_id():
    text = ""
    possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for i in range(0, 5):
        rand = randrange(0, len(possible))
        text += possible[rand]

    return text

def _remove_unique_id_on_list(lista, unique_id):
    return filter(lambda a: a != unique_id, lista)