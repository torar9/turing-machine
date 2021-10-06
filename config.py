from Rule import Rule
from State import State
from Operation import Operation

q0 = State('q0', True, False)
q1 = State('q1', False, False)
q2 = State('q2', False, False)
q3 = State('q3', False, False)
q4 = State('q4', False, False)
q5 = State('q5', False, False)
q6 = State('q6', False, False)
q7 = State('q7', False, False)
q8 = State('qc', False, False)
q9 = State('qc', False, False)
q10 = State('qc', False, False)
qe = State('qe', False, True)

rules = [
        [Rule(q0, '0', q1, '0', Operation.R), Rule(q0, '#', q1, '#', Operation.N)],
        [Rule(q1, '0', q0, '0', Operation.R), Rule(q1, '#', q0, '#', Operation.N)],
        [Rule(q1, '1', q0, '1', Operation.R), Rule(q1, '#', q0, '#', Operation.N)],
        [Rule(q1, '2', q0, '2', Operation.R), Rule(q1, '#', q0, '#', Operation.N)],
        [Rule(q1, '3', q8, '3', Operation.N), Rule(q1, '#', q8, '#', Operation.N)],
        [Rule(q8, '3', q0, '3', Operation.R), Rule(q8, '#', q0, '3', Operation.R)],
        [Rule(q0, '2', q1, '2', Operation.R), Rule(q0, '#', q1, '#', Operation.N)],
        [Rule(q0, '3', q1, '3', Operation.R), Rule(q0, '#', q1, '3', Operation.R)],
        [Rule(q0, '#', q2, '#', Operation.L), Rule(q0, '#', q2, '#', Operation.N)],
        [Rule(q0, '1', q1, '1', Operation.R), Rule(q0, '#', q1, '#', Operation.N)],
        [Rule(q1, '#', q2, '#', Operation.L), Rule(q1, '#', q2, '#', Operation.L)],
        [Rule(q2, '2', q3, '2', Operation.L), Rule(q2, '#', q3, '#', Operation.N)],
        [Rule(q3, '0', q2, '0', Operation.L), Rule(q3, '#', q2, '#', Operation.N)],
        [Rule(q3, '1', q2, '1', Operation.L), Rule(q3, '#', q2, '#', Operation.N)],
        [Rule(q3, '2', q2, '2', Operation.L), Rule(q3, '#', q2, '2', Operation.R)],
        [Rule(q3, '3', q2, '3', Operation.L), Rule(q3, '#', q2, '#', Operation.N)],
        [Rule(q3, '#', q4, '#', Operation.R), Rule(q3, '#', q4, '#', Operation.N)],
        [Rule(q2, '1', q3, '1', Operation.L), Rule(q2, '#', q3, '#', Operation.N)],
        [Rule(q2, '0', q3, '0', Operation.L), Rule(q2, '#', q3, '#', Operation.N)],
        [Rule(q2, '3', q3, '3', Operation.L), Rule(q2, '#', q3, '#', Operation.N)],
        [Rule(q2, '#', q4, '#', Operation.R), Rule(q2, '#', q4, '#', Operation.N)],
        [Rule(q4, '1', q5, '1', Operation.R), Rule(q4, '#', q5, '1', Operation.R)],
        [Rule(q5, '0', q4, '0', Operation.R), Rule(q5, '#', q4, '#', Operation.N)],
        [Rule(q5, '1', q9, '1', Operation.N), Rule(q5, '#', q9, '#', Operation.N)],
        [Rule(q9, '1', q4, '1', Operation.R), Rule(q9, '#', q4, '1', Operation.R)],
        [Rule(q5, '2', q4, '2', Operation.R), Rule(q5, '#', q4, '#', Operation.N)],
        [Rule(q5, '3', q4, '3', Operation.R), Rule(q5, '#', q4, '#', Operation.N)],
        [Rule(q4, '0', q5, '0', Operation.R), Rule(q4, '#', q5, '#', Operation.N)],
        [Rule(q4, '2', q5, '2', Operation.R), Rule(q4, '#', q5, '#', Operation.N)],
        [Rule(q4, '3', q5, '3', Operation.R), Rule(q4, '#', q5, '#', Operation.N)],
        [Rule(q4, '#', q6, '#', Operation.L), Rule(q4, '#', q6, '#', Operation.N)],
        [Rule(q5, '#', q6, '#', Operation.L), Rule(q5, '#', q6, '#', Operation.N)],
        [Rule(q6, '0', q7, '#', Operation.L), Rule(q6, '#', q7, '#', Operation.N)],
        [Rule(q7, '0', q6, '#', Operation.L), Rule(q7, '#', q6, '0', Operation.R)],
        [Rule(q7, '1', q6, '#', Operation.L), Rule(q7, '#', q6, '#', Operation.N)],
        [Rule(q7, '2', q6, '#', Operation.L), Rule(q7, '#', q6, '#', Operation.N)],
        [Rule(q7, '3', q6, '#', Operation.L), Rule(q7, '#', q6, '#', Operation.N)],
        [Rule(q7, '#', qe, '#', Operation.N), Rule(q7, '#', qe, '#', Operation.N)],
        [Rule(q6, '1', q7, '#', Operation.L), Rule(q6, '#', q7, '#', Operation.N)],
        [Rule(q6, '2', q7, '#', Operation.L), Rule(q6, '#', q7, '#', Operation.N)],
        [Rule(q6, '3', q7, '#', Operation.L), Rule(q6, '#', q7, '#', Operation.N)],
        [Rule(q6, '#', qe, '#', Operation.N), Rule(q6, '#', qe, '#', Operation.N)]
    ]