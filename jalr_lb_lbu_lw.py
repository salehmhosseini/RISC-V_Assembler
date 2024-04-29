def assemble_opcode(opcode_str):
    if opcode_str == "jalr":
        return '1100111'
    elif opcode_str == "lb" or opcode_str == "lbu" or opcode_str == "lw":
        return '0000011'
    else:
        raise ValueError("Unsupported opcode")

def assemble_func3(opcode_str):
    if opcode_str == "jalr":
        return '000'
    elif opcode_str == "lb":
        return '000'
    elif opcode_str == "lbu":
        return '100'
    elif opcode_str == "lw":
        return '010'
    else:
        raise ValueError("Unsupported opcode")

def assemble_machine_code(opcode, rd, func3, rs1, imm):
    opcode_binary = format(int(opcode, 2), '07b')
    rd_binary = format(rd, '05b')
    func3_binary = format(int(func3, 2), '03b')
    rs1_binary = format(rs1, '05b')
    imm_binary = format(imm, '012b')
    machine_code = imm_binary[-12:] + rs1_binary + func3_binary + rd_binary + opcode_binary
    return '0x' + format(int(machine_code, 2), '08x')

def main():
    # Get the number of lines of code
    num_lines = int(input())

    answers = []

    # Process each line of code
    for _ in range(num_lines):
        input_str = input()
        label, colon, opcode_str, rd_str, comma, imm_str , open_parantese , rs_1 , close_parantese = input_str.split()
        rd = int(rd_str[1:])  # Extract rd number, skipping 'x'
        imm = int(imm_str.split('(')[0], 16)  # Convert hexadecimal immediate to integer
        rs1 = int(rs_1[1:])  # Extract rs1 number, skipping 'x'
        opcode = assemble_opcode(opcode_str)
        func3 = assemble_func3(opcode_str)
        machine_code = assemble_machine_code(opcode, rd, func3, rs1, imm)
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()  