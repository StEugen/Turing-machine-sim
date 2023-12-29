

class TuringMachine:

    def __init__(self, states, input_alphabet, tape_alphabet, transitions, start_state, accept_states, reject_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.reject_states = reject_states

    def run(self, input_string):
        tape = list(input_string)
        head = 0
        state = self.start_state

        while state not in self.accept_states and state not in self.reject_states:
            symbol = tape[head]

            if (state, symbol) not in self.transitions:
                print("No transition found for state {} and symbol {}".format(state, symbol))
                break

            new_state, new_symbol, move = self.transitions[(state, symbol)]
            tape[head] = new_symbol

            if move == 'R':
                head += 1
            elif move == 'L':
                head -= 1

            state = new_state

            if head == len(tape):
                tape.append('_')
            elif head == -1:
                tape.insert(0, '_')

            print("State: {}, Tape: {}".format(state, ''.join(tape)))

        if state in self.accept_states:
            print("Accepted")
        else:
            print("Rejected")


states = {'q0', 'q1', 'q2'}
input_alphabet = {'0', '1'}
tape_alphabet = {'0', '1', '_'}
transitions = {('q0', '0'): ('q1', '1', 'R'),
               ('q0', '1'): ('q1', '0', 'R'),
               ('q1', '0'): ('q2', '1', 'L'),
               ('q1', '1'): ('q2', '0', 'L')}

start_state = 'q0'
accept_states = {'q2'}
reject_states = {}

tm = TuringMachine(states, input_alphabet, tape_alphabet, transitions, start_state, accept_states, reject_states)
tm.run('0110')
