import lexer
from Parser import AST_TOKEN

while True:
    line = input("> ")
    _tokens_ = lexer.Get_tokens(line)
    print(_tokens_)
    _parse_ = {"Tree": [AST_TOKEN("Number", "23"), AST_TOKEN("Number", "3"), AST_TOKEN("Function", "+")]}
    print(_parse_)
