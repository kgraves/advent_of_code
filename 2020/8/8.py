import re
import sys


LINE_RE = re.compile('(nop|acc|jmp)\ ([+-]\d+)')


def run_program(program):
    accum = 0
    pc = 0
    curr = program[pc]

    while curr[2] == False:
        program[pc] = (curr[0], curr[1], True)

        if curr[0] == 'acc':
            accum += curr[1]
            pc += 1
        elif curr[0] == 'jmp':
            pc += curr[1]
        else:  # 'nop'
            pc += 1

        if pc == len(program):
            return True, accum

        curr = program[pc]

    return False, accum


def part_one(lines):
    program = []

    for l in lines:
        instr, num = LINE_RE.match(l).groups()
        program.append( (instr, int(num), False) )

    _, accum = run_program(program)

    print(accum)


def part_two(lines):
    program = []
    for l in lines:
        instr, num = LINE_RE.match(l).groups()
        program.append( (instr, int(num), False) )

    def gen_swapped_programs(program):
        for i, line in enumerate(program):
            if line[0] in ['nop', 'jmp']:
                op = 'nop' if line[0] == 'jmp' else 'jmp'
                yield program[:i] + [(op, line[1], line[2])] + program[i+1:]

    for prog in gen_swapped_programs(program):
        hit_end, accum = run_program(prog)
        if hit_end:
            print(accum)
            break


def main():
    lines = []
    with open('2020/8/input.txt', 'r') as f:
        for line in f:
            lines.append(line)

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
