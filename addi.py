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
        label, colon, opcode_str, rd_str, comma, rs1_str, comma, imm_str = input_str.split()
        rd = int(rd_str[1:])  # Extract rd number, skipping 'x'
        rs1 = int(rs1_str[1:])  # Extract rs1 number, skipping 'x'
        imm = int(imm_str, 16)  # Convert hexadecimal immediate to integer
        opcode = "0010011"
        func3 = "000"
        machine_code = assemble_machine_code(opcode, rd, func3, rs1, imm)
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
