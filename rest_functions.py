'''
This file has the functions for API calls. This functions uses users' data to send inputs to the API
and get data from the database
'''
import Rest_automation_callhub.api_url as au
import Rest_automation_callhub.log_configuration as logger
import requests
import sys

log=logger.set_log("rest_phonebook_functions")
#Post method for creating phonebook
def create_phonebook(phonebook_details,apikey):
    log.info("Creation of Phonebook")
    headers = {'Authorization': 'Token %s' % apikey}
    data=phonebook_details
    response=requests.post(au.phonebook_url, data=data, headers=headers)
    

    try:
        if response.json()['name'][0]=='This field may not be blank.':
            log.error("Name can not be none")
            sys.exit()
    except KeyError as e:
        log.error("Key not found. Please check the parameters sent in post method")
        log.error(str(e))
        sys.exit()
    log.info("Phonebook has been created returning JSON object")
    log.info(response.json())    
    return response.json()

#Get method for getting phonebook information
def get_phonebook(phonebook_json,apikey):
    log.info ("Getting Phonebook")
    log.info("________________________")
    headers = {'Authorization': 'Token %s' % apikey}
    #phonebook_id=str(phonebook_json.json()['id'])
    #url = au.phonebook_url+phonebook_id+'/'
    phonebook_url=phonebook_json['url']
    response = requests.get(phonebook_url, headers=headers)
    log.info (response.json())
    return response.json()

#Post method to create tags
def create_tags(tags_details,apikey):
    log.info ("Creation of Tag")
    headers = {'Authorization': 'Token %s' % apikey,'cache-control':'no-cache'}
    log.info("________________________")
    data = tags_details#{"tag":"rajit_test_tag"}
    response = requests.post(au.tag_url, data=data, headers=headers)
    if response.json()['id']==None: #Name should not be none for a tags. But tags are getting created with empty name field
        log.info("Name can not be none")
        sys.exit()
        
    log.info (response.json())
    return response.json()

#Get method to get tags details
def get_tags(tag_json,apikey):
    headers = {'Authorization': 'Token %s' % apikey,'cache-control':'no-cache'}
    tag_id=str(tag_json['id'])
    url=au.tag_url+tag_id+'/'
    response = requests.get(url, headers=headers)
    return response.json()

#Post method to create contact in a phonebook
def create_phonebook_contact(phonebook_json,apikey,contact_details):
    headers = {'Authorization': 'Token %s' % apikey}
    data=contact_details
    #phonebook_id=str(phonebook_json.json['id'])
    url=phonebook_json['url']+'create_contact/'
    response = requests.post(url, data=data, headers=headers)
    if response.json().get('contact')==['This field may not be blank.']:
        log.error("Id or Contact numbers can not be none")
        sys.exit()
    log.info("Contact is created inside the phonebook")
    log.info(response.json())    
    return response.json()

#Get created contact in a phonebook
def get_phonebook_contact(phonebook_contact_json,apikey):
    headers = {'Authorization': 'Token %s' % apikey}
    phonebook_contact_id=str(phonebook_contact_json['contact']['id'])
    phonebook_contact_url=au.contact_url+phonebook_contact_id+'/'
    response=requests.get(phonebook_contact_url,headers=headers)
    return response.json()

#Put method to upgrade a contact
def update_contact(apikey,phonebook_contact_json,contact_update_details):
    headers = {'Authorization': 'Token %s' % apikey}
    data=contact_update_details
    #phonebook_contact_id=str(phonebook_contact_json.json()['contact']['id'])
    phonebook_contact_url=phonebook_contact_json['contact']['url']
    response = requests.put(phonebook_contact_url, data=data, headers=headers)
    if response.json().get('contact')==['This field is required.']:
        log.error("Contact can not be none. Please give contact")
        sys.exit()
    log.info(response.json())
    return response.json()
#Get updated contact
def get_updated_contact(updated_contact_json,apikey):
    headers = {'Authorization': 'Token %s' % apikey}
    url=updated_contact_json['url']
    
    response=requests.get(url,headers=headers)
    log.info(response.json())
    return response.json()