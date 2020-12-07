import collections
import re
import sys
import queue

LINE_RE = re.compile('^([a-z ]+) bags contain (.+)\.$')
TO_RE = re.compile('(\d+) ([a-z ]+) bags?')


def make_graph(lines):
    nodes = set()
    edges = collections.defaultdict(lambda: collections.defaultdict(None))
    rev_edges = collections.defaultdict(lambda: collections.defaultdict(None))

    for line in lines:
        source, rest = LINE_RE.match(line).groups()
        nodes.add(source)

        if rest != 'no other bags':
            for r in rest.split(','):
                weight, dest = TO_RE.match(r.strip()).groups()
                nodes.add(dest)
                edges[source][dest] = int(weight)
                rev_edges[dest][source] = int(weight)

    return nodes, edges, rev_edges


def part_one(lines):
    nodes, edges, rev_edges = make_graph(lines)

    can_contain = set()
    queue = ['shiny gold']
    while len(queue) > 0:
        curr = queue[0]
        queue.remove(curr)

        up_nodes = rev_edges[curr].keys()
        can_contain.update(up_nodes)
        queue.extend(up_nodes)

    print(len(can_contain))


def part_two(lines):
    nodes, edges, rev_edges = make_graph(lines)

    def count_bags(curr):
        if len(edges[curr]) == 0:
            return 1
        else:
            count = 1
            for node, weight in edges[curr].items():
                count += weight * count_bags(node)

            return count

    count = count_bags('shiny gold')
    print(count - 1)  # because gold is in count and we want how many are in *it*.


def main():
    lines = []
    with open('2020/7/input.txt', 'r') as f:
        lines = [l for l in f]

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
