from Rule import Rule
from State import State
from Operation import Operation
from TurringMachine import TurringMachine


def main():
    # tape = "#aaaaa#" # works
    # tape = "#bbbbbb#" # works
    # tape = "#bbaabab#" # works

    tape = "#abbaabab#"  # works

    q0 = State('q0', True, False)
    q1 = State('q1', False, False)
    q2 = State('q2', False, False)
    q3 = State('q3', False, False)
    q4 = State('q4', False, False)
    q5 = State('q5', False, False)
    q6 = State('q6', False, False)
    q7 = State('q7', False, False)
    qe = State('qe', False, True)

    rules = [
        Rule(q0, 'a', q0, 'a', Operation.R), Rule(q0, '#', q6, '#', Operation.L),
        Rule(q0, 'b', q1, '1', Operation.R), Rule(q1, 'a', q1, 'a', Operation.R),
        Rule(q1, '1', q1, '1', Operation.R), Rule(q1, '0', q1, '0', Operation.R),
        Rule(q1, 'b', q2, 'a', Operation.L), Rule(q1, '#', q5, '#', Operation.L),
        Rule(q2, 'a', q2, 'a', Operation.L), Rule(q2, '0', q3, '0', Operation.N),
        Rule(q2, '1', q3, '1', Operation.N), Rule(q3, '1', q3, '0', Operation.L),
        Rule(q3, '0', q1, '1', Operation.R), Rule(q3, '#', q4, '1', Operation.R),
        Rule(q3, 'a', q4, '1', Operation.R), Rule(q4, '1', q4, '0', Operation.R),
        Rule(q4, 'a', q1, 'a', Operation.N), Rule(q4, 'b', q1, 'b', Operation.N),
        Rule(q4, '0', q4, '0', Operation.R), Rule(q5, 'a', q5, '#', Operation.L),
        Rule(q5, '0', q5, '0', Operation.L), Rule(q5, '1', q5, '1', Operation.L),
        Rule(q5, '#', qe, '#', Operation.N), Rule(q6, 'a', q7, '0', Operation.L),
        Rule(q7, 'a', q7, '#', Operation.L), Rule(q7, '#', qe, '#', Operation.N)
    ]

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
