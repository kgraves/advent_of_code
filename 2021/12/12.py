import collections


def part_one(graph):
    def dfs(v, graph, seen):
        count = 0

        if v == 'end':
            return 1
        if v.islower() and v in seen:
            return 0

        if v.islower():
            seen.add(v)

        for n in graph[v]:
            if n not in seen:
                count += dfs(n, graph, seen.copy())

        return count

    print(dfs('start', graph, set()))


def part_two(graph):
    def already_double_visit(v, seen):
        small_caves = {k: vv for k, vv in seen.items() if k.islower() and k not in ['start', 'end']}
        doubles = {k for k,vv in small_caves.items() if vv == 2}
        return v in small_caves and len(doubles) > 0

    def dfs(v, graph, seen, path):
        if v == 'end':
            return 1
        if v == 'start' and seen[v] >= 1:
            return 0
        if already_double_visit(v, seen):
            return 0

        if v.islower():
            seen[v] += 1

        count = 0
        for n in graph[v]:
            count += dfs(n, graph, seen.copy(), path + ',' + n)

        return count

    print(dfs('start', graph, collections.Counter(), 'start'))


def main():
    lines = []

    with open('2021/12/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    graph = collections.defaultdict(list)
    for line in lines:
        origin, dest = line.split('-')
        graph[origin].append(dest)
        graph[dest].append(origin)

    part_one(graph)
    part_two(graph)


if __name__ == '__main__':
    main()
