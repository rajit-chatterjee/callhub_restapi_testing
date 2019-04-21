'''
This file is needed to validate the json objects returned by post and get method
'''

import sys
import Rest_automation_callhub.log_configuration as logger
log=logger.set_log("api_validation")
def validate_json(key,json1,json2):
    if key=="Phonebook":
        log.info("Phonebook validation is in progress")
    elif key=="Updated_contact":
        log.info("Updated contacts' validation is in progress")
    else:
        log.warning("Please select a correct key")
        sys.exit()
        
        
        
    if sorted(json1)==sorted(json2):
            log.info("Validation Passed")
    else:
        log.error("validation failed")
        sys.exit()

def validate_tags(key,json1,json2):
        if key=="Tags":
            log.info("Tags validation is in progress")
        else:
            log.error("Please give valid key entry")
            sys.exit()
        create_tag_id=str(json1['id'])
        get_tag_id=str(json2['results'][0]['id'])
        if create_tag_id==get_tag_id:
            log.info("Validation passed")
        else:
            log.error("Validation failed")
            sys.exit()
            
def validate_contacts(key,json1,json2):
        if key=="Contact":
            log.info("Contact validation is in progress")
        else:
            log.error("Please give valid key entry")
            sys.exit()
        #create_tag_id=str(json1['id'])
        create_contact_json=json1['contact']
        if sorted(create_contact_json)==sorted(json2):
            log.info("Validation passed")
        else:
            log.error("Validation failed")
            sys.exit()
        