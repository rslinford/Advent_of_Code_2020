
import re

#   price: 45-507 or 526-956
import unittest


class FieldRule:
    def __init__(self, field_rule):
        result = re.search(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$', field_rule)
        self.name = result.group(1)
        self.min_1 = int(result.group(2))
        self.max_1 = int(result.group(3))
        self.min_2 = int(result.group(4))
        self.max_2 = int(result.group(5))
    def __repr__(self):
        return f'FieldRule {self.name}: {self.min_1}-{self.max_1} or {self.min_2}-{self.max_2}'
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)

class Ticket:
    def __init__(self, ticket):
        self.values = [int(x) for x in ticket.split(',')]
    def __repr__(self):
        return f'Ticket: {self.values}'


def is_completely_invalid(ticket, field_rule_list):
    # Scan for a value that doesn't pass any rules.
    for field_value in ticket.values:
        field_doesnt_pass_any_rules = True
        for rule in field_rule_list:
            if  ((rule.min_1 <= field_value <= rule.max_1) or (rule.min_2 <= field_value <= rule.max_2)):
                field_doesnt_pass_any_rules = False
                break
        if field_doesnt_pass_any_rules == True:
            return True, field_value
    return False, 0


def scan_for_completely_invalid(nearby_ticket_list, field_rule_list):
    # Scan for completely invalid tickets.
    scanning_error_rate = 0
    for ticket in nearby_ticket_list:
        completely_invalid, invalid_field_value = is_completely_invalid(ticket, field_rule_list)
        if completely_invalid:
            scanning_error_rate += invalid_field_value
            # print(f'Completely invalid ticket: {ticket} because of invalid: {invalid_field_value}')
    print(f'Scanning error rate: {scanning_error_rate}')
    return scanning_error_rate


def parse_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    field_rules, your_ticket, nearby_tickets = data.split('\n\n')
    # Drop the heading "your ticket:"
    your_ticket = your_ticket.split('\n')[1]
    your_ticket = Ticket(your_ticket.strip())
    field_rule_list = []
    for rule in field_rules.split('\n'):
        field_rule_list.append(FieldRule(rule))
    nearby_ticket_list = []
    for i, ticket in enumerate(nearby_tickets.split('\n')):
        if i == 0:
            # skip first line, 'nearby tickets:'
            continue
        nearby_ticket_list.append(Ticket(ticket))
    return field_rule_list, nearby_ticket_list, your_ticket


def deduce_rule_to_column_mapping_first_try(field_rule_list, nearby_ticket_list):
    rule_to_column_mapping = {}
    for rule in field_rule_list:
        # Rule passes for which column
        if short:
            column_width = 3
        else:
            column_width = 20
        for column in range(column_width):
            column_passes_rule = True
            for ticket in nearby_ticket_list:
                # Make sure ticket isn't completely invalid
                completely_invalid, invalid_field_value = is_completely_invalid(ticket, field_rule_list)
                if completely_invalid:
                    continue
                value = ticket.values[column]
                if ((rule.min_1 <= value <= rule.max_1) or (rule.min_2 <= value <= rule.max_2)):
                    pass
                else:
                    column_passes_rule = False
                    break
            if column_passes_rule:
                if rule in rule_to_column_mapping.keys():
                    print(f'Warning: already have {rule} mapping to column {column}')
                rule_to_column_mapping[rule] = column
                break
    return rule_to_column_mapping


def deduce_rule_to_column_mapping(field_rule_list, nearby_ticket_list):
    column_width = len(nearby_ticket_list[0].values)
    column_to_rule_mapping = {}
    for column in range(column_width):
        for rule in field_rule_list:
            for ticket in nearby_ticket_list:
                value = ticket.values[column]
                if not (((rule.min_1 <= value <= rule.max_1) or (rule.min_2 <= value <= rule.max_2))):
                    # Then this Rule is not for this column
                    break #  next rule
            # Then this Rule works for this column
            # Check if we already have a rule
            if column in column_to_rule_mapping.keys():
                print(f'Warning: overwriting a rule that already passed: {column_to_rule_mapping[column]}')
            print(f'{rule} works for column {column}')
            column_to_rule_mapping[column] = rule
    print(column_to_rule_mapping)




short = False
if short:
    filename = 'Day_16_short_data.txt'
else:
    filename = 'Day_16_data.txt'


def part_one():
    field_rule_list, nearby_ticket_list, your_ticket = parse_puzzle_data(filename)
    scan_for_completely_invalid(nearby_ticket_list, field_rule_list)

def part_two(filename):
    field_rule_list, nearby_ticket_list, your_ticket = parse_puzzle_data(filename)
    rule_to_column_mapping = deduce_rule_to_column_mapping(field_rule_list, nearby_ticket_list)
    # Multiply the 6 departures
    answer = 1
    for rule, column in rule_to_column_mapping.items():
        print(f'Rule {rule.name}  column {column}  value {your_ticket.values[column]}')
        if rule.name.find('departure') == 0:
            answer *= your_ticket.values[column]
    print(f'Departures multiplied together {answer}')

part_two('Day_16_data.txt')

class TestDay16(unittest.TestCase):
    def test_scan_for_completely_invalid(self):
        field_rule_list, nearby_ticket_list, your_ticket = parse_puzzle_data(filename)
        if short:
            self.assertEqual(71, scan_for_completely_invalid(nearby_ticket_list, field_rule_list))
        else:
            self.assertEqual(21996, scan_for_completely_invalid(nearby_ticket_list, field_rule_list))