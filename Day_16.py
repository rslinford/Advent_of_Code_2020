
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
        return f'{self.name}: {self.min_1}-{self.max_1} or {self.min_2}-{self.max_2}'

short = False
if short:
    filename = 'Day_16_short_data.txt'
else:
    filename = 'Day_16_data.txt'
with open(filename, 'r') as f:
    data = f.read().strip()
field_rules, your_ticket, nearby_tickets = data.split('\n\n')
field_rule_list = []
for rule in field_rules.split('\n'):
    field_rule_list.append(FieldRule(rule))

print(field_rule_list)


