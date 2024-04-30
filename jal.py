def calculate_immediate(current_label, to_go_label):
    # Calculate the distance between the current and to-go labels
    immediate = (to_go_label - current_label) * 2

    # Check if the immediate is negative
    if immediate < 0:
        immediate += 2**20  # Convert negative immediate to two's complement

    # Convert immediate to binary string and ensure it's 20 bits
    immediate_binary = format(immediate, '020b')
    return immediate_binary

def assemble_machine_code(opcode, rd, immediate):
    opcode_binary = format(int(opcode, 2), '07b')
    rd_binary = format(rd, '05b')
    machine_code = immediate[0] + immediate[10:] + immediate[9] + immediate[1:9] + rd_binary + opcode_binary
    return '0x' + format(int(machine_code, 2), '08x')

def main():
    # Get the number of lines of code
    num_lines = int(input())

    answers = []

    # Process each line of code
    for _ in range(num_lines):
        input_str = input()
        current_label, colon, opcode_str, rd_str, comma, to_go_label_str = input_str.split()
        rd = int(rd_str[1:])  # Extract rd number, skipping 'x'
        to_go_label = int(to_go_label_str[1:])  # Extract to-go label number, skipping 'l'
        current_label = int(current_label[1:])

        # Calculate the immediate value
        immediate = calculate_immediate(current_label, to_go_label)

        # Update the current label
        current_label += 1

        # Assemble the machine code
        machine_code = assemble_machine_code('1101111', rd, immediate)

        # Append the machine code to the answers list
        answers.append(machine_code)

    # Print all answers in order
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
