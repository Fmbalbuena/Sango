import string

# This file is taken from the old Vyxal 2 interpreter

codepage = "\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t"
codepage += "\t" * 15 + " "
codepage += "!\"#$%&'()*+,-./01"
codepage += "23456789:;<=>?@A"
codepage += "BCDEFGHIJKLMNOPQ"
codepage += "RSTUVWXYZ[\\]^_`abc"
codepage += "defghijklmnopqrs"
codepage += "tuvwxyz{|}~     "
codepage += " " * 16
codepage += " " * 16
codepage += " " * 16
codepage += " " * 16
codepage += " " * 16
codepage += " " * 16
codepage += " " * 16
codepage += " " * 16

assert len(codepage) == 256


def sango_to_utf8(code: list[int]) -> str:
    """Turn characters on Sango codepage into actual UTF-8 characters"""
    # Taken from the old 05AB1E interpreter
    processed_code = ""
    for char in code:
        processed_code += codepage[char]

    return processed_code


def utf8_to_sango(code: str) -> str:
    """Turn UTF-8 characters into bytes according to the codepage"""
    # Taken from the old 05AB1E interpreter
    processed_code = ""
    for char in code:
        processed_code += chr(codepage.index(char))

    return processed_code
