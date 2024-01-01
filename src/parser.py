from lexer import CF, DIGITS, CFS, CFE, Tokens
"""
class AST_TOKEN:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        return f'P·{self.type_}: {self.value}'
"""
class Parser:
    def __init__(self, tokens_to_parse):
        self.token_stack = []
        self.token_index = -1
        self.ast = {}
        self.tokens_to_parse = tokens_to_parse
        self.token_memory = []
        self.current_token_type = None
        """
        self.start_brackets = []
        self.stack_with_brackets = []
        self.token_substack = []
        self.advance()
        """
    def advance(self, tokens_to_advance = 1):
        self.previous_token_type = self.current_token_type
        self.token_index += tokens_to_advance
        self.current_token = self.tokens_to_parse[self.token_index] if self.token_index < len(self.tokens_to_parse) else None
        self.current_token_value = Tokens.get_value(self.current_token)
        self.current_token_type = Tokens.get_type(self.current_token)
    def Parse(self):
        while self.current_token == None:
            if self.previous_token_type == "Op":
                if self.current_token_type == "Op":
                    self.token_memory += self.current_token_value
                    continue
                self.token_stack.append(["Function", {"Op", self.token_memory, "Func", self.current_token_value}])
            if self.current_token_value in CFS:
                self.token_stack.append(["CF", self.current_token_value])
            elif self.current_token_type == "Op":
                self.token_memory += self.current_token_value
                self.advance()
                continue
            else:
                self.token_stack.append(["Function", self.current_token_value])
            self.advance()
        """
        while self.current_token != None:
            if self.current_token_value in CFS:
                self.start_brackets.append(Tokens.get_value(self.current_token))
                self.substack.extend([self.current_token_value, ""])
                self.stack_with_brackets
            elif self.current_token_value in CFE:
                if len(self.start_brackets) == 1:
                    self.token_stack.append(None)
                    self.start_brackets.pop()
                else:
                    self.token_substack.append({["CF", self.start_brackets[-1]]: self.substack[-1][1]})
                    self.start_brackets.pop()
            else:
                if len(self.start_brackets) >= 1:
                    self.stack_with_brackets.append(self.current_token)
                    self.
                else:
                    if self.bracket_check:
                        self.token_stack.append()
                    
                    self.token_stack.append(self.current_token)
            self.advance()
        """
        return {"tree": self.token_stack}
def Parse_tokens(tokenlist):
    _Parser_ = Parser(tokenlist)
    _ParseTokens_ = _Parser_.Parse()
    return _ParseTokens_