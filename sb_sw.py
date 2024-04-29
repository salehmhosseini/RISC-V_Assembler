def assemble_opcode(opcode_str):
    if opcode_str == "sb":
        return '0100011'
    elif opcode_str == "sw":
        return '0100011'
    else:
        raise ValueError("Unsupported opcode")

def assemble_func3(opcode_str):
    if opcode_str == "sb":
        return '000'
    elif opcode_str == "sw":
        return '010'
    else:
        raise ValueError("Unsupported opcode")

def assemble_machine_code(opcode, func3, rs1, rs2, imm):
    opcode_binary = format(int(opcode, 2), '07b')
    func3_binary = format(int(func3, 2), '03b')
    rs1_binary = format(rs1, '05b')
    rs2_binary = format(rs2, '05b')
    imm_binary = format(imm, '012b')
    machine_code = imm_binary[5:12] + rs2_binary + rs1_binary + func3_binary + imm_binary[0:5] + opcode_binary
    print(imm_binary , imm_binary[5:12] , rs2_binary , rs1_binary ,func3_binary , imm_binary[0:5], opcode_binary )
    return '0x' + format(int(machine_code, 2), '08x')

def main():
    # Get the number of lines of code
    num_lines = int(input())

    answers = []

    # Process each line of code
    for _ in range(num_lines):
        input_str = input()
        label, colon, opcode_str, rs2_str, comma, imm_str, open_parantese , rs1_str , close_parantese= input_str.split()
        rs1 = int(rs1_str[1:])  # Extract rs1 number, skipping 'x'
        rs2 = int(rs2_str[1:])  # Extract rs2 number, skipping 'x'
        imm = int(imm_str.split('(')[0], 16)  # Convert hexadecimal immediate to integer
        opcode = assemble_opcode(opcode_str)
        func3 = assemble_func3(opcode_str)
        machine_code = assemble_machine_code(opcode, func3, rs1, rs2, imm)
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()

