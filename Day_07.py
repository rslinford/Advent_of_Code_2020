def load_bag_rules(filename):
    with open(filename, 'r') as f:
        rules = f.read().split('\n')
    return rules


class Bag:
    instances = {}

    def __init__(self, fancy_color):
        self.fancy_color = fancy_color
        self.children = {}

    def __repr__(self):
        return f'Bag({self.fancy_color})'

    def __eq__(self, other):
        return self.fancy_color == other.fancy_color

    def __hash__(self):
        return hash(self.fancy_color)

    def render_children(self):
        rval = []
        for i, child in enumerate(self.children.keys()):
            if i > 0:
                rval.append(', ')
            rval.append(str(self.children.get(child)))
            rval.append(' ')
            rval.append(str(child))
        return ''.join(rval)

    def add_child(self, child_bag, can_contain_count):
        self.children[child_bag] = can_contain_count


def bag_factory_fancy(fancy_color_name: str) -> Bag:
    if fancy_color_name in Bag.instances:
        bag = Bag.instances.get(fancy_color_name)
    else:
        bag = Bag(fancy_color_name)
        Bag.instances[fancy_color_name] = bag
    return bag


def bag_factory(adjective, color):
    fancy_color_name = f'{adjective} {color}'
    return bag_factory_fancy(fancy_color_name)


def bag_can_contain_shiny_gold(fancy_color):
    bag = bag_factory_fancy(fancy_color)
    if len(bag.children) == 0:
        return False
    for child in bag.children:
        if child.fancy_color == 'shiny gold':
            return True
    rval = False
    for child in bag.children:
        rval = bag_can_contain_shiny_gold(child.fancy_color)
        if rval is True:
            break

    return rval


def load_bag_hierarchy(filename):
    data = load_bag_rules(filename)
    for rule in data:
        rlist = rule.strip().split(' ')
        parent_bag = bag_factory(rlist[0], rlist[1])
        # print(parent_bag, rule)
        assert (rlist[2] == 'bags')
        assert (rlist[3] == 'contain')
        if rlist[4] != 'no':
            index = 5
            while index < len(rlist):
                parent_bag.add_child(bag_factory(rlist[index], rlist[index + 1]), int(rlist[index - 1]))
                # todo add as child
                index += 4
        # print(f'Created {parent_bag} with children: {parent_bag.render_children()}')


def part1(filename):
    load_bag_hierarchy(filename)
    tally = 0
    for fancy_color in Bag.instances.keys():
        if bag_can_contain_shiny_gold(fancy_color):
            tally += 1
        # print(f'Bag {fancy_color}  can contain "shiny gold": {bag_can_contain_shiny_gold(fancy_color)}')
    print(f'Number of bags that can eventually contain "shiny gold": {tally}')
    if filename == 'Day_07_small_data.txt':
        assert (tally == 4)
    elif filename == 'Day_07_data.txt':
        assert (tally == 172)




# part1('Day_07_small_data.txt')
part1('Day_07_small_data.txt')
