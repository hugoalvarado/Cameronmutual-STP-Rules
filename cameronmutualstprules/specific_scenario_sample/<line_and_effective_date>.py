from rule_engine import Rule
from _processors_<line> import (
    rule_test_reinstatement_v1,
    rule_test_reinstatement_something_else_v1,
    rule_test_reinstatement_another_thing_v1
)

# prefix the next section with an appreviation of your company
# then prefix it with the name of the line. Lastly increment your rules
# with prefix R starting at 001
CPNY_LINE_R001 = Rule('CPNY_LINE_R001', rule_test_something_v1)
CPNY_LINE_R002 = Rule('CPNY_LINE_R002', rule_test_something_else_v1)
CPNY_LINE_R003 = Rule('CPNY_LINE_R003', rule_test_another_thing_v1)

# make list of rules for all lines/risks.
risk_rules = [
    CPNY_LINE_R001,
    CPNY_LINE_R002
]

# Make list of all rules for sublines.
risk_subline_rules = []

# Make list of all rules that are policy level
policy_rules = [
    CPNY_LINE_R003
]

unscoped_rules = []
