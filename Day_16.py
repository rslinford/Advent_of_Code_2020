
import re

#   price: 45-507 or 526-956
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


class Ticket:
    def __init__(self, ticket):
        self.values = [int(x) for x in ticket.split(',')]
    def __repr__(self):
        return f'Ticket: {self.values}'


short = True
if short:
    filename = 'Day_16_short_data.txt'
else:
    filename = 'Day_16_data.txt'
with open(filename, 'r') as f:
    data = f.read().strip()

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


def part_one():
    # Read Data
    field_rules, your_ticket, nearby_tickets = data.split('\n\n')
    field_rule_list = []
    for rule in field_rules.split('\n'):
        field_rule_list.append(FieldRule(rule))
    nearby_ticket_list = []
    for i, ticket in enumerate(nearby_tickets.split('\n')):
        if i == 0:
            # skip first line, 'nearby tickets:'
            continue
        nearby_ticket_list.append(Ticket(ticket))

    # Scan for completely invalid tickets.
    scanning_error_rate = 0
    for ticket in nearby_ticket_list:
        completely_invalid, invalid_field_value = is_completely_invalid(ticket, field_rule_list)
        if completely_invalid:
            scanning_error_rate += invalid_field_value
            print(f'Completely invalid ticket: {ticket} because of invalid: {invalid_field_value}')
    print(f'Scanning error rate: {scanning_error_rate}')

part_one()