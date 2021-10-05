class TurringMachine:
    def __init__(self, first_state, tape, rules, head=[0], empty_symbol='#'):
        self.tape = tape
        self.rules = rules
        self.head = head
        self.finished = False
        self.current_state = first_state
        self.empty_symbol = empty_symbol
        self.number_of_steps = 0
        self.max_used_tape_length = len(self.tape)

    def find_rule(self, symbol, i):
        for e in self.rules:
            if e[i].current_state.name == self.current_state.name and e[i].current_symbol == symbol:
                return e[i]
        raise Exception('Unable to find rule')

    def stylize_tape(self):
        for i in range(len(self.tape)):
            if self.tape[i][0] != self.empty_symbol:
                self.tape[i] = self.empty_symbol + self.tape[i]
                self.head[i] = self.head[i] + 1

    def step(self):
        self.number_of_steps += 1
        for i in range(len(self.head)):
            symbol = self.tape[i][self.head[i]]

            try:
                rule = self.find_rule(symbol, i)
            except Exception:
                if (self.current_state.end is True):
                    self.finished = True
                else:
                    print('Unable to find rule')
                return

            self.tape[i] = self.tape[i][0:self.head[i]] + rule.next_symbol + self.tape[i][self.head[i] + 1:]
            self.head[i] = self.head[i] + int(rule.operation)

            # Make sure tape starts and ends with empty symbol
            self.stylize_tape()

            if self.head[i] < 0:
                self.tape[i] = self.empty_symbol + self.tape[i]
                self.head[i] = 0
            elif self.head[i] > len(self.tape[i]):
                self.tape[i] += self.empty_symbol

            if self.current_state.end:
                self.finished = True
            self.current_state = rule.next_state

            if self.max_used_tape_length < self.head[i] + 1:
                self.max_used_tape_length = self.head[i] + 1