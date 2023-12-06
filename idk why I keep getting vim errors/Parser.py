from lexer import CF, DIGITS, CFS, CFE
class AST_TOKEN:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        return f'P·{self.type_}: {self.value}'
class Parser:
    def __init__(self, tokens_to_parse):
        self.token_stack = ("")
        self.token_index = 0
        self.ast = {}
        self.tokens_to_parse = tokens_to_parse
        self.start_brackets = []
    def advance(self, tokens_to_advance = 1):
        self.token_index += tokens_to_advance
        self.current_token = self.tokens_to_parse[self.token_index] if self.token_index < len(self.tokens_to_parse) else None
        self.token_stack = []
    def Parse(self):
        if self.current_token in CFE:
            start_brackets.append('c')
        else:pass

