import config
from Rule import Rule
from State import State
from Operation import Operation
from TurringMachine import TurringMachine


def find_rule(rules, i):
    for e in rules:
        print("{} {} {} {} {}".format(e[0].current_state.name, e[0].current_symbol, e[0].next_state.name, e[0].next_symbol, e[0].operation))



def main():
    tape = ["#02123301121023#", "###"]  # works

    print(len(tape))

    rules = config.rules

    turr = TurringMachine(config.q0, tape, rules, head=[1, 1])


    print('Input: {}'.format(turr.tape))
    print('Turing machine steps:')
    while turr.finished is False:
        print("  state: '{}' head: {} \n tapes: {}".format(turr.current_state.name, turr.head, turr.tape))
        turr.step()
    print('Finished')
    print('Machine stopped after: {} steps'.format(turr.number_of_steps))
    print('Machine used maximum of: {} boxes on the tape'.format(turr.max_used_tape_length))
    print('Output: {}'.format(turr.tape[1]))


if __name__ == '__main__':
    main()