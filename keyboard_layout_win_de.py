# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


from adafruit_hid.keyboard_layout_base import KeyboardLayoutBase
class KeyboardLayout(KeyboardLayoutBase):
    ASCII_TO_KEYCODE = (
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2a'  # BACKSPACE
        b'\x2b'  # '\t'
        b'\x28'  # '\n'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x29'  # ESC
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2c'  # ' '
        b'\x9e'  # '!'
        b'\x9f'  # '"'
        b'\x31'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\xb1'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\xb0'  # '*'
        b'\x30'  # '+'
        b'\x36'  # ','
        b'\x38'  # '-'
        b'\x37'  # '.'
        b'\xa4'  # '/'
        b'\x27'  # '0'
        b'\x1e'  # '1'
        b'\x1f'  # '2'
        b'\x20'  # '3'
        b'\x21'  # '4'
        b'\x22'  # '5'
        b'\x23'  # '6'
        b'\x24'  # '7'
        b'\x25'  # '8'
        b'\x26'  # '9'
        b'\xb7'  # ':'
        b'\xb6'  # ';'
        b'\x64'  # '<'
        b'\xa7'  # '='
        b'\xe4'  # '>'
        b'\xad'  # '?'
        b'\x14'  # '@'
        b'\x84'  # 'A'
        b'\x85'  # 'B'
        b'\x86'  # 'C'
        b'\x87'  # 'D'
        b'\x88'  # 'E'
        b'\x89'  # 'F'
        b'\x8a'  # 'G'
        b'\x8b'  # 'H'
        b'\x8c'  # 'I'
        b'\x8d'  # 'J'
        b'\x8e'  # 'K'
        b'\x8f'  # 'L'
        b'\x90'  # 'M'
        b'\x91'  # 'N'
        b'\x92'  # 'O'
        b'\x93'  # 'P'
        b'\x94'  # 'Q'
        b'\x95'  # 'R'
        b'\x96'  # 'S'
        b'\x97'  # 'T'
        b'\x98'  # 'U'
        b'\x99'  # 'V'
        b'\x9a'  # 'W'
        b'\x9b'  # 'X'
        b'\x9d'  # 'Y'
        b'\x9c'  # 'Z'
        b'\x25'  # '['
        b'\x2d'  # '\\'
        b'\x26'  # ']'
        b'\x00'
        b'\xb8'  # '_'
        b'\x00'
        b'\x04'  # 'a'
        b'\x05'  # 'b'
        b'\x06'  # 'c'
        b'\x07'  # 'd'
        b'\x08'  # 'e'
        b'\x09'  # 'f'
        b'\x0a'  # 'g'
        b'\x0b'  # 'h'
        b'\x0c'  # 'i'
        b'\x0d'  # 'j'
        b'\x0e'  # 'k'
        b'\x0f'  # 'l'
        b'\x10'  # 'm'
        b'\x11'  # 'n'
        b'\x12'  # 'o'
        b'\x13'  # 'p'
        b'\x14'  # 'q'
        b'\x15'  # 'r'
        b'\x16'  # 's'
        b'\x17'  # 't'
        b'\x18'  # 'u'
        b'\x19'  # 'v'
        b'\x1a'  # 'w'
        b'\x1b'  # 'x'
        b'\x1d'  # 'y'
        b'\x1c'  # 'z'
        b'\x24'  # '{'
        b'\x64'  # '|'
        b'\x27'  # '}'
        b'\x30'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '@[\\]{|}~²³µ€'
    HIGHER_ASCII = {
        0xb2: 0x1f,  # '²'
        0xa7: 0xa0,  # '§'
        0xb3: 0x20,  # '³'
        0xdf: 0x2d,  # 'ß'
        0x20ac: 0x08,  # '€'
        0xfc: 0x2f,  # 'ü'
        0xdc: 0xaf,  # 'Ü'
        0xf6: 0x33,  # 'ö'
        0xd6: 0xb3,  # 'Ö'
        0xe4: 0x34,  # 'ä'
        0xc4: 0xb4,  # 'Ä'
        0xb0: 0xb5,  # '°'
        0xb5: 0x10,  # 'µ'
    }
    COMBINED_KEYS = {
        0xe1: 0x2e61,  # 'á'
        0xe9: 0x2e65,  # 'é'
        0xed: 0x2e69,  # 'í'
        0xf3: 0x2e6f,  # 'ó'
        0xfa: 0x2e75,  # 'ú'
        0xfd: 0x2e79,  # 'ý'
        0xc1: 0x2e41,  # 'Á'
        0xc9: 0x2e45,  # 'É'
        0xcd: 0x2e49,  # 'Í'
        0xd3: 0x2e4f,  # 'Ó'
        0xda: 0x2e55,  # 'Ú'
        0xdd: 0x2e59,  # 'Ý'
        0xb4: 0x2e20,  # '´'
        0xe0: 0xae61,  # 'à'
        0xe8: 0xae65,  # 'è'
        0xec: 0xae69,  # 'ì'
        0xf2: 0xae6f,  # 'ò'
        0xf9: 0xae75,  # 'ù'
        0xc0: 0xae41,  # 'À'
        0xc8: 0xae45,  # 'È'
        0xcc: 0xae49,  # 'Ì'
        0xd2: 0xae4f,  # 'Ò'
        0xd9: 0xae55,  # 'Ù'
        0x60: 0xae20,  # '`'
        0xe2: 0x3561,  # 'â'
        0xea: 0x3565,  # 'ê'
        0xee: 0x3569,  # 'î'
        0xf4: 0x356f,  # 'ô'
        0xfb: 0x3575,  # 'û'
        0xc2: 0x3541,  # 'Â'
        0xca: 0x3545,  # 'Ê'
        0xce: 0x3549,  # 'Î'
        0xd4: 0x354f,  # 'Ô'
        0xdb: 0x3555,  # 'Û'
        0x5e: 0x3520,  # '^'
    }