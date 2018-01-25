from stack import Stack
from grammer import PARSER_TABEL, TERMINALS, NON_TERMINALS, GRAMMER
from scanner import Scanner


class Parser(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.stack = Stack()
        self.stack.push("EOF")
        self.stack.push("Source")
        self.parser_table = PARSER_TABEL
        self.scanner = Scanner(file_name)
        self.next_token = self.scanner.get_next_token()[0].value
        self.top_stack = self.stack.top()
        self.rule_number = None
        self.rule = ""
        self.grammer = GRAMMER

    def run(self):
        while True:
            if self.top_stack == 'EOF':
                return
            self.top_stack = self.stack.top()
            print(self.stack, self.next_token, self.top_stack)
            if self.top_stack in TERMINALS:
                print("find terminal")
                if self.next_token == self.top_stack:
                    print("match terminal")
                    if self.next_token == 'EOF':
                        break
                    self.stack.pop()
                    self.next_token = self.scanner.get_next_token()[0].value

                else:
                    print("see error")
                    return

            elif self.top_stack in NON_TERMINALS:
                print("find non terminal")
                if self.next_token in self.parser_table[self.top_stack]:
                    print("match non terminal")
                    self.push_rule_to_stack(self.parser_table[self.top_stack][self.next_token])
                else:
                    print("error")
                    return
                self.top_stack = self.stack.top()

    def push_rule_to_stack(self, rule_number):
        self.rule_number = rule_number
        self.rule = self.grammer[self.rule_number]
        rules = self.rule.split(" ")
        self.stack.pop()
        print('***** ' + str(rules))
        for action in reversed(rules):
            self.stack.push(action)
        self.stack.pop()


P = Parser('test4.java').run()