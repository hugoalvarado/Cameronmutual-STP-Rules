# Cameronmutual-STP-Rules


## Installing the STP client rules

STP client rules should be used from the [legacy-stp](https://github.com/IntuitiveWebSolutions/legacy-stp) engine.

Clone that repo and install this rule package:

`pip install git+https://github.com/IntuitiveWebSolutions/Cameronmutual-STP-Rules.git`

Doing this will install the cameronmutualstprules package for the legacy-stp engine.


## STP client rules 101

Rules are a set of functions used by the legacy-stp engine to process a policy and, if all rule conditions are True,
allow the policy to be accepted (bind an application) without human intervention. 
Otherwise it will require review from an underwriter.

Sample rules were created by the cookiecutter template. 
The minimum files for a working rule are:
* mapping.py - defines a mapping such as:
    ```bash
    RULESET_MAP = {
        # This is a dictionary where each key is a tuple with the date, state, line and policy type name,
        # and the value the name of a py file with 'rules' that are defined for the policy type
    
        # SAMPLE LED: 2018-10-24
        ('2018-10-24', 'State1', 'Homeowners', 'Homeowners Policy'): 'homeowners_10_24_2018',
        ('2018-10-24', 'State2', 'Businessowners', 'Businessowners Policy'): 'businessowners_10_24_2018',
    
        # SAMPLE LED: 2018-10-25
        # ('2018-10-25', 'State1', 'Homeowners', 'Homeowners Policy'): 'homeowners_10_25_2018',
        # ('2018-10-25', 'State2', 'Businessowners', 'Businessowners Policy'): 'businessowners_10_25_2018',
        # ...
    }
    ```
    Each value in the RULESET_MAP dictionary corresponds to a script that will handle 
    the logic for the led, state, line and product.
    In this case there will be 2 files, businessowners_10_24_2018.py and homeowners_10_24_2018.py.
* 1 or more files that will handle the unique rule logic for each led, state, line and product combination (mentioned above).
* (optional) 1 or more processor files, these hold the common logic used by rules in all or several lines. 

More details are available [here](cameronmutualstprules/README.md).