def assemble_machine_code(rd, rs1, shamt):
    opcode = '0010011'  # opcode for srai
    func3 = '101'  # func3 for srai
    rd_binary = format(rd, '05b')
    rs1_binary = format(rs1, '05b')
    shamt_binary = format(shamt, '05b')
    machine_code = '0100000'+shamt_binary + rs1_binary + func3 + rd_binary + opcode
    return '0x' + format(int(machine_code, 2), '08x')

def main():
    # Get the number of lines of code
    num_lines = int(input())

    answers = []

    # Process each line of code
    for _ in range(num_lines):
        input_str = input()
        label, colon, opcode_str, rd_str, comma, rs1_str, comma, shamt_str = input_str.split()
        rd = int(rd_str[1:])  # Extract rd number, skipping 'x'
        rs1 = int(rs1_str[1:])  # Extract rs1 number, skipping 'x'
        shamt = int(shamt_str, 16)  # Convert hexadecimal shamt to integer
        machine_code = assemble_machine_code(rd, rs1, shamt)
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
