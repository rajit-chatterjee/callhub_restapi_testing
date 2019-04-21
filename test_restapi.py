'''
Testcase file. The automation script for the particular feature is written here.
This file is test case specific.
Steps
Create a phonebook with name 'CallHub QA Test'
Add 2 contacts to this phonebook
Add a tag 'testing' to one of the contacts in this phonebook
'''
import Rest_automation_callhub.feature_configuration as fc
import Rest_automation_callhub.rest_functions as rf
import Rest_automation_callhub.api_validation as av

apikey= fc.authentication_key.get('api_key')

#Create phonebook, get phonebook and validate json
create_phonebook_object=rf.create_phonebook(fc.phonebook_details, apikey)
get_phonebook_json=rf.get_phonebook(create_phonebook_object, apikey)
av.validate_json(fc.validation_key.get('1'), create_phonebook_object, get_phonebook_json)

#Create tags, get tags and validate json
create_tags_json=rf.create_tags(fc.tags_details, apikey)
get_tags_json=rf.get_tags(create_tags_json, apikey)
av.validate_tags(fc.validation_key.get('2'), create_tags_json, get_tags_json)

#Create contact, get contact and validate contact
#1
create_phonebook_contact_json_1=rf.create_phonebook_contact(create_phonebook_object, apikey, fc.contact_details_1)
get_phonebook_contact_json_1=rf.get_phonebook_contact(create_phonebook_contact_json_1, apikey)
av.validate_contacts(fc.validation_key.get('3'), create_phonebook_contact_json_1, get_phonebook_contact_json_1)
#2
create_phonebook_contact_json_2=rf.create_phonebook_contact(create_phonebook_object, apikey, fc.contact_details_2)
get_phonebook_contact_json_2=rf.get_phonebook_contact(create_phonebook_contact_json_2, apikey)
av.validate_contacts(fc.validation_key.get('3'), create_phonebook_contact_json_2, get_phonebook_contact_json_2)

#Update contact details inside phonebook and verify
fc.update_contact.update({'tags':[create_tags_json]})
update_contact_json=rf.update_contact(apikey, create_phonebook_contact_json_2, fc.update_contact)
get_updated_contact_json=rf.get_updated_contact(update_contact_json, apikey)
av.validate_json(fc.validation_key.get('4'), update_contact_json, get_updated_contact_json)