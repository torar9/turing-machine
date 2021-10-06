import string


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

    def find_rule(self, symbol):
        for rules in self.rules:
            result = rules
            found = False
            for j, rule in enumerate(rules):
                if self.current_state is rule.current_state and symbol[j] is rule.current_symbol:
                    found = True
                else:
                    found = False
                    break
            if found is True:
                return result

        raise Exception('Unable to find rule')

    def stylize_tape(self):
        for i in range(len(self.tape)):
            if self.tape[i][0] is not self.empty_symbol:
                self.tape[i] = self.empty_symbol + self.tape
                self.head = self.head + 1
            if self.tape[i][len(self.tape[i]) - 1] is not self.empty_symbol:
                self.tape[i] = self.tape[i] + self.empty_symbol

    def find_symbols(self):
        result = ['0'] * len(self.head)
        for i in range(len(self.head)):
            result[i] = self.tape[i][self.head[i]]
        return result

    def step(self):
        self.number_of_steps += 1
        symbol = self.find_symbols()
        for i in range(len(self.head)):
            #symbol[i] = self.tape[i][self.head[i]]

            try:
                rule = self.find_rule(symbol)[i]
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

            if self.max_used_tape_length < self.head[i] + 1:
                self.max_used_tape_length = self.head[i] + 1

            if i is len(self.head) - 1:
                self.current_state = rule.next_state