from Rule import Rule
from State import State
from Operation import Operation
from TurringMachine import TurringMachine


def main():
    #tape = "#101001#1101#"
    #tape = "#1101#1101#"
    tape = "#10#1101#"

    q0 = State('q0', True, False)
    q1 = State('q1', True, False)
    q2 = State('q2', False, False)
    q3 = State('q3', False, False)
    q4 = State('q4', False, False)
    q5 = State('q5', False, False)
    q6 = State('q6', False, False)
    q7 = State('q7', False, False)
    q8 = State('q8', False, False)
    q9 = State('q9', False, False)
    q10 = State('q10', False, False)
    q11 = State('q11', False, False)
    q12 = State('q12', False, False)
    qf = State('qf', False, True)

    # Rule(q0, 'a', q0, 'a', Operation.R), Rule(q0, '#', q6, '#', Operation.L)

    rules = [Rule(q0, '0', q0, '0', Operation.R), Rule(q0, '1', q0, '1', Operation.R),
             Rule(q0, '#', q1, '#', Operation.L), Rule(q1, '0', q1, '0', Operation.L),
             Rule(q1, '1', q2, '0', Operation.R), Rule(q1, '#', q8, '#', Operation.N),
             Rule(q2, '0', q2, '1', Operation.R), Rule(q2, '#', q3, '#', Operation.R),
             Rule(q3, '1', q3, '1', Operation.R), Rule(q3, '0', q3, '0', Operation.R),
             Rule(q3, '#', q4, '#', Operation.L), Rule(q4, '0', q4, '0', Operation.L),
             Rule(q4, '1', q5, '0', Operation.R), Rule(q4, '#', q9, '0', Operation.L),
             Rule(q5, '0', q5, '1', Operation.R), Rule(q5, '#', q6, '#', Operation.L),
             Rule(q6, '1', q6, '1', Operation.L), Rule(q6, '0', q6, '0', Operation.L),
             Rule(q6, '#', q7, '#', Operation.L), Rule(q7, '#', q0, '#', Operation.R),
             Rule(q7, '1', q7, '1', Operation.L), Rule(q7, '0', q7, '0', Operation.L),
             Rule(q8, '#', q10, '1', Operation.R), Rule(q10, '0', q10, '#', Operation.R),
             Rule(q10, '1', q10, '#', Operation.R), Rule(q10, '#', q11, '#', Operation.R),
             Rule(q11, '1', q11, '#', Operation.R), Rule(q11, '0', q11, '#', Operation.R),
             Rule(q11, '#', qf, '#', Operation.N), Rule(q9, '#', q12, '0', Operation.R),
             Rule(q9, '0', q9, '0', Operation.L), Rule(q9, '1', q9, '1', Operation.L),
             Rule(q12, '1', q12, '#', Operation.R), Rule(q12, '0', q12, '#', Operation.R),
             Rule(q12, '#', qf, '#', Operation.N)
             ]

    turr = TurringMachine(q0, tape, rules, head=1)

    print('Input: {}'.format(turr.tape))
    print('Turing machine steps:')
    while turr.finished is False:
        #print("  state: '{}' head: {} tape: {}".format(turr.current_state.name, turr.head, turr.tape))
        turr.step()
    print('Finished')
    print('Machine stopped after: {} steps'.format(turr.number_of_steps))
    print('Machine used maximum of: {} boxes on the tape'.format(turr.max_used_tape_length))
    print('Output: {}'.format(turr.tape))


if __name__ == '__main__':
    main()
