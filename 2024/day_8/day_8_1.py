def find_antinodes(curr_node: tuple[int, int], nodes: list[tuple[int, int]], height: int, width: int) -> set[tuple[int, int]]:
    c_x, c_y = curr_node
    result: set[tuple[int, int]] = set()

    for node in nodes:
        n_x, n_y = node
        dif_x = c_x - n_x
        dif_y = c_y - n_y

        if 0 <= (c_x + dif_x) < width and 0 <= (c_y + dif_y) < height:
            result.add((c_x + dif_x, c_y + dif_y))
        if 0 <= (n_x - dif_x) < width and 0 <= (n_y - dif_y) < height:
            result.add((n_x - dif_x, n_y - dif_y))

    return result


with open("day_8.txt") as f:
    node_map = f.readlines()

    nodes: dict[str, list[tuple[int, int]]] = {}
    used_nodes: set[str] = set()
    antinodes: set[tuple[int, int]] = set()
    height = len(node_map)
    width = len(node_map)

    for y, line in enumerate(node_map):
        for x, char in enumerate(line):
            if char != '.':
                if char in used_nodes:
                    antinodes.update(find_antinodes((x, y), nodes[char], height, width))
                    nodes[char].append((x, y))

                else:
                    used_nodes.add(char)
                    nodes[char] = [(x, y)]

    print(len(antinodes))