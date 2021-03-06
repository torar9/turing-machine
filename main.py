from Rule import Rule
from State import State
from Operation import Operation
from TurringMachine import TurringMachine


def main():
    # tape = "#aaaaa#" # works

    tape = "##"  # works

    q0 = State('q0', True, False)

    # Rule(q0, 'a', q0, 'a', Operation.R), Rule(q0, '#', q6, '#', Operation.L)
    rules = []

    turr = TurringMachine(q0, tape, rules, head=1)

    print('Input: {}'.format(turr.tape))
    print('Turing machine steps:')
    while turr.finished is False:
        print("  state: '{}' head: {} tape: {}".format(turr.current_state.name, turr.head, turr.tape))
        turr.step()
    print('Finished')
    print('Machine stopped after: {} steps'.format(turr.number_of_steps))
    print('Machine used maximum of: {} boxes on the tape'.format(turr.max_used_tape_length))
    print('Output: {}'.format(turr.tape))


if __name__ == '__main__':
    main()
