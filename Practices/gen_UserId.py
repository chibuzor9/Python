import random


def gen_userId(username: str) -> str:
    username_id = ""

    for chars in username:
        if chars in dict_map.keys():
            username_id += str(dict_map[chars])

    return username_id


char_array = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890&é#'(-è_çà)=+}]@^\r|[{~$*ù%!:;/.}]"
dict_map = {x: random.randint(0, 9) for x in char_array}

print(gen_userId('chibuzor9'))
