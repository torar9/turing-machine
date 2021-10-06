import string


class TurringMachine:
    def __init__(self, first_state, tapes, rules, heads=[0], empty_symbol='#'):
        self.tapes = tapes
        self.rules = rules
        self.heads = heads
        self.finished = False
        self.current_state = first_state
        self.empty_symbol = empty_symbol
        self.number_of_steps = 0
        self.max_tape_length = [len(self.tapes)] * len(self.heads)

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
        for i in range(len(self.tapes)):
            if self.tapes[i][0] is not self.empty_symbol:
                self.tapes[i] = self.empty_symbol + self.tapes
                self.heads = self.heads + 1
            if self.tapes[i][len(self.tapes[i]) - 1] is not self.empty_symbol:
                self.tapes[i] = self.tapes[i] + self.empty_symbol

    def find_symbols(self):
        result = ['0'] * len(self.heads)
        for i in range(len(self.heads)):
            result[i] = self.tapes[i][self.heads[i]]
        return result

    def step(self):
        self.number_of_steps += 1
        symbol = self.find_symbols()
        for i in range(len(self.heads)):
            try:
                rule = self.find_rule(symbol)[i]
            except Exception:
                if (self.current_state.end is True):
                    self.finished = True
                else:
                    print('Unable to find rule')
                return

            self.tapes[i] = self.tapes[i][0:self.heads[i]] + rule.next_symbol + self.tapes[i][self.heads[i] + 1:]

            self.heads[i] = self.heads[i] + int(rule.operation)

            # Make sure tape starts and ends with empty symbol
            self.stylize_tape()

            if self.heads[i] < 0:
                self.tapes[i] = self.empty_symbol + self.tapes[i]
                self.heads[i] = 0
            elif self.heads[i] > len(self.tapes[i]):
                self.tapes[i] += self.empty_symbol

            if self.current_state.end:
                self.finished = True

            if self.max_tape_length[i] < self.heads[i] + 1:
                self.max_tape_length[i] = self.heads[i] + 1

            if i is len(self.heads) - 1:
                self.current_state = rule.next_state