#usr/bin/python3

from lexer import Tokens, Get_tokens
from parser import Parse_tokens

while True:
    line = input("> ")
    _tokens_ = Get_tokens(line)
    print(_tokens_)
    _parse_ = Parse_tokens(_tokens_)
    print(_parse_)
