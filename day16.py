import math


def convert_hex_to_binary(string):
    output = ''
    lookup = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    for ch in string:
        output += lookup[ch]
    return output


def binary_to_int(start, length):
    return int("".join(string[start:start+length]), 2)


def read_literal_value_5bits_chunks(i):
    construction_bits = []
    while True:
        construction_bits.append(string[i+1])
        construction_bits.append(string[i+2])
        construction_bits.append(string[i+3])
        construction_bits.append(string[i+4])
        i += 5
        if string[i-5] == '0':
            break
    return int("".join(construction_bits), 2), i


def read_packet_header(i):
    return binary_to_int(i, 3), binary_to_int(i+3, 3), i+6


def operator_sum(operands):
    return sum(operands)


def operator_mul(operands):
    return math.prod(operands)


def operator_min(operands):
    return min(operands)


def operator_max(operands):
    return max(operands)


def operator_greater(operands):
    if operands[0] > operands[1]:
        return 1
    return 0


def operator_less(operands):
    if operands[0] < operands[1]:
        return 1
    return 0


def operator_equal(operands):
    if operands[0] == operands[1]:
        return 1
    return 0


operator_dict = {
    0: operator_sum,
    1: operator_mul,
    2: operator_min,
    3: operator_max,
    5: operator_greater,
    6: operator_less,
    7: operator_equal
}


def read_operator_packet(operator, i):
    operand_stack = []
    if string[i] == '0':
        packet_length = binary_to_int(i + 1, 15)
        i += 16
        stop_at = i + packet_length
        while i < stop_at:
            ret, i = read_packet(i)
            operand_stack.append(ret)
    else:
        num_packets = binary_to_int(i + 1, 11)
        i += 12
        for _ in range(num_packets):
            ret, i = read_packet(i)
            operand_stack.append(ret)

    return operator_dict[operator](operand_stack), i


def read_packet(i):
    version, type_id, i = read_packet_header(i)
    version_numbers.append(version)
    if type_id == 4:
        result, i = read_literal_value_5bits_chunks(i)
    else:
        result, i = read_operator_packet(type_id, i)
    return result, i


filename = "input/day16input.txt"
file = open(filename, "r")
file = file.readlines()
string = file[0].replace('\n', '')
string = (convert_hex_to_binary(string))

version_numbers = []
total, i = read_packet(0)
print(f'Answer to part 1: {sum(version_numbers)}')
print(f'Answer to part 2: {total}')
