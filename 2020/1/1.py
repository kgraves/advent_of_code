import sys


def find(nums, goal_sum):
    for n in nums:
        if (goal_sum - n) in nums:
            return n

def part_one(nums, goal_sum):
    solution = find(nums, goal_sum)
    print(solution * (goal_sum - solution))


def part_two(nums, goal_sum):
    for n in nums:
        solution = find(nums, (goal_sum - n))
        if solution:
            print(n * solution * (goal_sum - n - solution))
            return


def main():
    goal_sum = 2020
    nums = {}

    for n in sys.stdin:
        nums[int(n)] = 1

    part_one(nums, goal_sum)
    part_two(nums, goal_sum)


if __name__ == '__main__':
    main()
