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

    turr = TurringMachine(config.q0, tape, rules, heads=[1, 1])


    print('Input: {}'.format(turr.tapes))
    while turr.finished is False:
        turr.step()
    print('Machine stopped after: {} steps'.format(turr.number_of_steps))
    print('Machine used maximum of: {} boxes on both tapes'.format(turr.max_tape_length[0] + turr.max_tape_length[1]))
    print('Output tape: {}'.format(turr.tapes[1]))
    print('Printing all tapes: {}'.format(turr.tapes))


if __name__ == '__main__':
    main()