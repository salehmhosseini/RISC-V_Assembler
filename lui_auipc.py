def assemble_opcode(opcode_str):
    if opcode_str == "lui":
        return '0110111'
    elif opcode_str == "auipc":
        return '0010111'
    else:
        raise ValueError("Unsupported opcode")

def assemble_machine_code(opcode, rd, imm):
    rd_binary = format(rd, '05b')
    imm_binary = format(imm, '020b')
    machine_code = imm_binary + rd_binary + opcode
    return '0x' + format(int(machine_code, 2), '08x')

def main():
    # Get the number of lines of code
    num_lines = int(input())

    answers = []

    # Process each line of code
    for _ in range(num_lines):
        input_str = input()
        label, colon, opcode_str, rd_str, comma, imm_str = input_str.split()
        rd = int(rd_str[1:])  # Extract rd number, skipping 'x'
        imm = int(imm_str, 16)  # Convert hexadecimal immediate to integer
        opcode = assemble_opcode(opcode_str)
        machine_code = assemble_machine_code(opcode, rd, imm)
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
