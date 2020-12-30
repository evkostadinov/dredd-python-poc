import dredd_hooks as hooks
import json
import os

# discussed with Nathan Hall, that
# 400s shouldn't be tested 
# 200 shouldn't be tested on the POST routes
@hooks.before('/health > health > 401')
@hooks.before('/health > health > 403')
@hooks.before('/health > health > 404')
@hooks.before('/info > info > 401')
@hooks.before('/info > info > 403')
@hooks.before('/info > info > 404')
@hooks.before('/fhir/v2/validate > Validates a FHIR object against the v2.0 schemas > 200 > application/json')
@hooks.before('/fhir/v2/validate > Validates a FHIR object against the v2.0 schemas > 400')
@hooks.before('/fhir/v2/validate > Validates a FHIR object against the v2.0 schemas > 401')
@hooks.before('/fhir/v2/validate > Validates a FHIR object against the v2.0 schemas > 403')
@hooks.before('/fhir/v2/validate > Validates a FHIR object against the v2.0 schemas > 404')
@hooks.before('/fhir/v2_1/validate > Validates a FHIR object against the v2.1 schemas > 200 > application/json')
@hooks.before('/fhir/v2_1/validate > Validates a FHIR object against the v2.1 schemas > 400')
@hooks.before('/fhir/v2_1/validate > Validates a FHIR object against the v2.1 schemas > 401')
@hooks.before('/fhir/v2_1/validate > Validates a FHIR object against the v2.1 schemas > 403')
@hooks.before('/fhir/v2_1/validate > Validates a FHIR object against the v2.1 schemas > 404')
@hooks.before('/fhir/v3/validate > Validates a FHIR object against the 3.0.2 schemas > 200 > application/json')
@hooks.before('/fhir/v3/validate > Validates a FHIR object against the 3.0.2 schemas > 400')
@hooks.before('/fhir/v3/validate > Validates a FHIR object against the 3.0.2 schemas > 401')
@hooks.before('/fhir/v3/validate > Validates a FHIR object against the 3.0.2 schemas > 403')
@hooks.before('/fhir/v3/validate > Validates a FHIR object against the 3.0.2 schemas > 404')
@hooks.before('/fhir/r4/validate > Validates a FHIR object against the 4.0.1 schemas > 200 > application/json')
@hooks.before('/fhir/r4/validate > Validates a FHIR object against the 4.0.1 schemas > 400')
@hooks.before('/fhir/r4/validate > Validates a FHIR object against the 4.0.1 schemas > 401')
@hooks.before('/fhir/r4/validate > Validates a FHIR object against the 4.0.1 schemas > 403')
@hooks.before('/fhir/r4/validate > Validates a FHIR object against the 4.0.1 schemas > 404')
@hooks.before('/fhir/r5/validate > Validates a FHIR object against the 4.4.0 schemas > 200 > application/json')
@hooks.before('/fhir/r5/validate > Validates a FHIR object against the 4.4.0 schemas > 400')
@hooks.before('/fhir/r5/validate > Validates a FHIR object against the 4.4.0 schemas > 401')
@hooks.before('/fhir/r5/validate > Validates a FHIR object against the 4.4.0 schemas > 403')
@hooks.before('/fhir/r5/validate > Validates a FHIR object against the 4.4.0 schemas > 404')
def before_hook(transaction):
    transaction['skip'] = 'true'

@hooks.before('/fhir/v2/validate > Validates a FHIR object against the v2.0 schemas > 201')
@hooks.before('/fhir/v2_1/validate > Validates a FHIR object against the v2.1 schemas > 201')
def add_fhir_json(transaction):
    with open(os.path.join('fhir_json', 'v2.json'), 'r') as jsonfile:
        body = json.load(jsonfile)
    transaction['request']['body'] = body

@hooks.before('/fhir/v3/validate > Validates a FHIR object against the 3.0.2 schemas > 201')
def add_fhir_v3_json(transaction):
    body = ''
    with open(os.path.join('fhir_json', 'v3.json'), 'r') as jsonfile:
        body = json.load(jsonfile)
    transaction['request']['body'] = body

@hooks.before('/fhir/r4/validate > Validates a FHIR object against the 4.0.1 schemas > 201')
def add_fhir_v4_json(transaction):
    body = ''
    with open(os.path.join('fhir_json', 'v4.json'), 'r') as jsonfile:
        body = json.load(jsonfile)
    transaction['request']['body'] = body

@hooks.before('/fhir/r5/validate > Validates a FHIR object against the 4.4.0 schemas > 201')
def add_fhir_v4_json(transaction):
    body = ''
    with open(os.path.join('fhir_json', 'v5.json'), 'r') as jsonfile:
        body = json.load(jsonfile)
    transaction['request']['body'] = body
