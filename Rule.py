class Rule:
    def __init__(self, current_state, current_symbol, next_state, next_symbol, operation):
        self.current_state = current_state
        self.current_symbol = current_symbol
        self.next_state = next_state
        self.next_symbol = next_symbol
        self.operation = operation

    def __str__(self) -> str:
        return "" + self.current_state + " " + self.current_symbol + " " + self.next_state + " " + self.next_symbol + " " + self.operation

