class TurringMachine:
    def __init__(self, first_state, tape, rules, head=0, empty_symbol='#'):
        self.tape = tape
        self.rules = rules
        self.head = head
        self.finished = False
        self.current_state = first_state
        self.empty_symbol = empty_symbol
        self.number_of_steps = 0
        self.max_used_tape_length = len(self.tape)

    def find_rule(self, symbol):
        for e in self.rules:
            if e.current_state.name == self.current_state.name and e.current_symbol == symbol:
                return e
        raise Exception('Unable to find rule')

    def stylize_tape(self):
        if self.tape[0] != self.empty_symbol:
            self.tape = self.empty_symbol + self.tape
            self.head = self.head + 1

    def step(self):
        self.number_of_steps += 1
        symbol = self.tape[self.head]

        try:
            rule = self.find_rule(symbol)
        except Exception:
            if (self.current_state.end is True):
                self.finished = True
            else: print('Unable to find rule')
            return

        self.tape = self.tape[0:self.head] + rule.next_symbol + self.tape[self.head+1:]
        self.head = self.head + int(rule.operation)

        # Make sure tape starts and ends with empty symbol
        self.stylize_tape()

        if self.head < 0:
            self.tape = self.empty_symbol + self.tape
            self.head = 0
        elif self.head > len(self.tape):
            self.tape += self.empty_symbol

        if self.current_state.end:
            self.finished = True
        self.current_state = rule.next_state

        if self.max_used_tape_length < self.head + 1:
            self.max_used_tape_length = self.head + 1