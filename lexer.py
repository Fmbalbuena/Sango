DIGITS = '0123456789'
CFS = '{[(' # Control Flow Start
CFE = ')]}' # Control Flow End
CF = CFS + ',' + CFE # Control Flow
class Tokens:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        if self.value:
            return f'{self.type_}: {self.value}'
        return self.type
class Lexer_:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    def Make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in DIGITS + '.':
                tokens.append(Tokens("Number", self.read_number()))
            elif self.current_char in CF:
                tokens.append(Tokens("Keyword", self.current_char))
            else:
                tokens.append(Tokens("Function", self.current_char))
                self.advance()
        return tokens
    def read_number(self):
        num_str = ""
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    return num_str
                num_str += "."
                dot_count += 1
            else:
                num_str += self.current_char
            self.advance()
        return num_str
def Get_tokens(text):
    Lexer = Lexer_(text)
    tokens = Lexer.Make_tokens()
    return tokens
