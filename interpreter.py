Functions = {
        '+': lambda x, y: x + y
        '-': lambda x, y: x - y
        '*': lambda x, y: x * y
        '/': lambda x, y: x // y
        '√': lambda x, y: x - 8
            }
Function_arguments = {
        '+': 2
        '-': 2
        '*': 2
        '/': 2
        '√': 1
                     }
Class Interpreter:
    def __init__(self, tokens_to_run):
        self.stack = []
        self.token_index = -1
        self.current_token = None
        self.token_advance()
    def token_advance(self, number_of_tokens_to_advance = 1):
        self.token_index += number_of_tokens_to_advance
        self.current_token = self.tokens_to_run[self.token_index] if self.token_index > len(self.tokens_to_run) else None
    def Run_code(self):
        while True:
            pass
