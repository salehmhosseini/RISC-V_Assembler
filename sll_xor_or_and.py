def assemble_opcode(opcode_str):
    if opcode_str == "sll" or opcode_str == "xor" or opcode_str == "or" or opcode_str == "and":
        return '0110011'
    else:
        raise ValueError("Unsupported opcode")

def assemble_func3(opcode_str):
    if opcode_str == "sll":
        return '001'
    elif opcode_str == "xor":
        return '100'
    elif opcode_str == "or":
        return '110'
    elif opcode_str == "and":
        return '111'
    else:
        raise ValueError("Unsupported opcode")

def assemble_machine_code(opcode, func3, rd, rs1, rs2):
    opcode_binary = format(int(opcode, 2), '07b')
    func3_binary = format(int(func3, 2), '03b')
    rd_binary = format(rd, '05b')
    rs1_binary = format(rs1, '05b')
    rs2_binary = format(rs2, '05b')
    machine_code = '0000000' + rs2_binary + rs1_binary + func3_binary + rd_binary + opcode_binary
    return '0x' + format(int(machine_code, 2), '08x')

def main():
    # Get the number of lines of code
    num_lines = int(input())

    answers = []

    # Process each line of code
    for _ in range(num_lines):
        input_str = input()
        label, colon, opcode_str, rd_str, comma, rs1_str, comma, rs2_str = input_str.split()
        rd = int(rd_str[1:])  # Extract rd number, skipping 'x'
        rs1 = int(rs1_str[1:])  # Extract rs1 number, skipping 'x'
        rs2 = int(rs2_str[1:])  # Extract rs2 number, skipping 'x'
        opcode = assemble_opcode(opcode_str)
        func3 = assemble_func3(opcode_str)
        machine_code = assemble_machine_code(opcode, func3, rd, rs1, rs2)
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
