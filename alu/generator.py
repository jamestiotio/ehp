# Define helper functions to auto-generate the testing scripts for the auto_tester


def instantiate_states(num_of_states):
    whitespace_begin = "      "
    tests = ""

    for i in range(num_of_states):
        tests += f", TEST_{i}"

    return whitespace_begin + "fsm autostate = {STANDBY" + tests + "};"


def instantiate_tester(test_num, input_x, input_y, opcode, expected_output):
    whitespace_begin = "      "
    return whitespace_begin + f"statement_tester test_{test_num} (#INPUT_X(16h{input_x}), #INPUT_Y(16h{input_y}), #OPCODE(6b{opcode}), #EXPECTED_OUTPUT(16h{expected_output}));"


def test_case_state(state_num, is_final):
    whitespace_begin = "      "
    whitespace_interval = "  "
    output = ""
    output += whitespace_begin + f"autostate.TEST_{state_num}:\n"
    output += (
        whitespace_begin + whitespace_interval + f"io_seg = test_{state_num}.io_seg;\n"
    )
    output += (
        whitespace_begin + whitespace_interval + f"io_sel = test_{state_num}.io_sel;\n"
    )
    output += (
        whitespace_begin
        + whitespace_interval
        + f"opcode_led = test_{state_num}.opcode_led;\n"
    )
    output += whitespace_begin + whitespace_interval + f"test_{state_num}.start = 1;\n"
    output += (
        whitespace_begin + whitespace_interval + f"if (test_{state_num}.done) " + "{\n"
    )

    if is_final:
        output += (
            whitespace_begin
            + (2 * whitespace_interval)
            + f"autostate.d = autostate.STANDBY;\n"
        )
    else:
        output += (
            whitespace_begin
            + (2 * whitespace_interval)
            + f"autostate.d = autostate.TEST_{state_num + 1};\n"
        )

    output += whitespace_begin + whitespace_interval + "}"

    return output


# Define test cases in the format of (input_x, input_y, opcode, expected_output)

test_cases = [
    ("abcd", "ef42", "000000", "9b0f"), # ADD
    ("0369", "0369", "000000", "06d2"), # ADD
    ("0369", "0000", "000001", "0369"), # SUB
    ("abcd", "abcd", "000001", "0000"), # SUB
    ("7fff", "7fff", "000100", "0001"), # MUL
    ("7fff", "0000", "000100", "0000"), # MUL
    ("0420", "0069", "000101", "000a"), # DIV
    ("0069", "0000", "000101", "0069"), # DIV
    ("0420", "0069", "000111", "0006"), # MODULO
    ("0069", "0000", "000111", "0069"), # MODULO
    ("1970", "ffff", "001000", "1971"), # INCREMENT X
    ("ffff", "abab", "001000", "0000"), # INCREMENT X
    ("1970", "ffff", "001001", "0000"), # INCREMENT Y
    ("ffff", "abab", "001001", "abac"), # INCREMENT Y
    ("1970", "0000", "001100", "196f"), # DECREMENT X
    ("0000", "abab", "001100", "ffff"), # DECREMENT X
    ("1970", "0000", "001101", "ffff"), # DECREMENT Y
    ("0000", "abab", "001101", "abaa"), # DECREMENT Y
    ("abcd", "dede", "010000", "0000"), # ZERO
    ("2f2f", "0101", "010000", "0000"), # ZERO
    ("2af0", "afe0", "010001", "500f"), # NOR
    ("ff00", "00ff", "010001", "0000"), # NOR
    ("3636", "2035", "010010", "0001"), # NOT CONVERSE
    ("ffff", "eeee", "010010", "0000"), # NOT CONVERSE
    ("2140", "f0f0", "010011", "debf"), # NOT X
    ("8c67", "0f0f", "010011", "7398"), # NOT X
    ("2345", "6789", "010100", "0044"), # NOT IMPLY
    ("1357", "2468", "010100", "1317"), # NOT IMPLY
    ("f0f0", "2140", "010101", "debf"), # NOT Y
    ("0f0f", "8c67", "010101", "7398"), # NOT Y
    ("ffff", "ffff", "010110", "0000"), # XOR
    ("ffff", "0000", "010110", "ffff"), # XOR
    ("2af0", "afe0", "010111", "d51f"), # NAND
    ("ff00", "00ff", "010111", "ffff"), # NAND
    ("0000", "ffff", "011000", "0000"), # AND
    ("ffff", "ffff", "011000", "ffff"), # AND
    ("2af0", "afe0", "011001", "7aef"), # XNOR
    ("ff00", "00ff", "011001", "0000"), # XNOR
    ("2121", "4242", "011010", "2121"), # X
    ("4242", "4242", "011010", "4242"), # X
    ("58ae", "e249", "011011", "e759"), # IMPLY
    ("10cf", "79a5", "011011", "ffb5"), # IMPLY
    ("4242", "2121", "011100", "2121"), # Y
    ("4242", "4242", "011100", "4242"), # Y
    ("2979", "3945", "011101", "effb"), # CONVERSE
    ("fbfb", "acac", "011101", "fbfb"), # CONVERSE
    ("0000", "ffff", "011110", "ffff"), # OR
    ("0001", "0010", "011110", "0011"), # OR
    ("2e45", "1984", "011111", "1111"), # ONE
    ("adef", "2000", "011111", "1111"), # ONE
    ("ffff", "0001", "100000", "fffe"), # SHL
    ("ffff", "0008", "100000", "ff00"), # SHL
    ("ffff", "0001", "100001", "7fff"), # SHR
    ("ffff", "0008", "100001", "00ff"), # SHR
    ("ffff", "0001", "100011", "ffff"), # SRA
    ("3fff", "0008", "100011", "003f"), # SRA
    ("7fff", "7fff", "110010", "0001"), # CMPEQ
    ("7fff", "0000", "110010", "0000"), # CMPEQ
    ("7fff", "7fff", "110100", "0000"), # CMPLT
    ("0000", "7fff", "110100", "0001"), # CMPLT
    ("7fff", "0000", "110110", "0000"), # CMPLE
    ("2121", "2121", "110110", "0001"), # CMPLE
]

# Begin generating a list of states for auto_tester and instantiate the statement tester modules

l = len(test_cases)

print(instantiate_states(l))

for i in range(l):
    print(
        instantiate_tester(
            i, test_cases[i][0], test_cases[i][1], test_cases[i][2], test_cases[i][3]
        )
    )

print("") # Neat
print("--------------------------------------------") # Neat
print("") # Neat

for i in range(l):
    whitespace_begin = "    "
    print(whitespace_begin + f"test_{i}.start = 0;")

print("") # Neat
print("--------------------------------------------") # Neat
print("") # Neat

# Generate the states and state transitions for auto_tester

for i in range(l - 1):
    print(test_case_state(i, False))
    print("") # Neat

print(test_case_state(l - 1, True))
