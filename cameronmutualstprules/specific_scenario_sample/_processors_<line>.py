
from rule_engine import dynamic_defaults

# Here is where you would add your rules. A rule could have any parameters you
# pass in. Suffix each function with a version number. As you have new LEDs that
# require small changes, you can add them as a new function with an increased
# version number. ie v1, v2, v3, etc.
@dynamic_defaults
def rule_test_reinstatement_v1(param="{bc::<Group>::<Section>::<Value of question>}}", fallback=True):
    if param:
        success_value = param == "value"
        message = "something you would want to return if it's not successful"
        return_message = message if not success_value else None
        return {'success_key':success_value, 'return_message':return_message}

def rule_test_reinstatement_something_else_v1(entire_data_object):
    value_one = entire_data_object.get("{{bc::<Group>::<Value>}}")
    value_two = entire_data_object.get("{{bc::<Group>::<Subgroup>::<Second Subgroup>::<Value>}}")

    if value_one and value_two:
        return {'success_key':success_value, 'return_message':return_message}

@dynamic_defaults
def rule_test_reinstatement_another_thing_v1(param="{bc::<Revision/Policy/Item etc>::Section::<Value>}}", fallback=True):
    if param:
        success_value = param == "value"
        message = "something you would want to return if it's not successful"
        return_message = message if not success_value else None
        return {'success_key':success_value, 'return_message':return_message}

