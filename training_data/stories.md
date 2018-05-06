## greet
* greet
    - utter_greet

## Good bye
* goodbye
    - utter_goodbye

## NGO according to entities
* greet
    - utter_greet
    - utter_ask
* NGO_search[field=children]
    - utter_children
    - action_search_ngo_name
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO according to entities
* greet
    - utter_greet
    - utter_ask
* NGO_search[field=women]
    - utter_women
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO according to entities
* NGO_search[field=education]
    - utter_education
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO according to all entities 1
* greet
    - utter_greet
    - utter_ask
* NGO_search[field=children]
    - utter_children
* NGO_search[field=education]
    - utter_education
* NGO_search[field=women]
    - utter_women
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO according to all entities 2
* greet
    - utter_greet
    - utter_ask
* NGO_search[field=education]
    - utter_education
* NGO_search[field=women]
    - utter_women
* NGO_search[field=children]
    - utter_children
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO according to all entities 3
* greet
    - utter_greet
    - utter_ask
* NGO_search[field=women]
    - utter_women
* NGO_search[field=children]
    - utter_children
* NGO_search[field=education]
    - utter_education
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO for children 
* greet
    - utter_greet
    - utter_ask
* NGO_search
    - utter_category
* NGO_search[field=children]
    - utter_children
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO for women
* greet
    - utter_greet
    - utter_ask
* NGO_search
    - utter_category
* NGO_search[field=women]
    - utter_women
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye

## NGO for education
* greet
    - utter_greet
    - utter_ask
* NGO_search
    - utter_category
* NGO_search[field=education]
    - utter_education
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye


## NGO for donations online
* greet
    - utter_greet
    - utter_ask
* NGO_donation
    - utter_donation
* affirm
    - utter_did_that_help
* donation_type[donation_mode=online]
    - action_donate_online
* affirm
    - utter_okay_donation_online
* goodbye
    - utter_goodbye

## NGO for donations offline
* greet
    - utter_greet
    - utter_ask
* NGO_donation
    - utter_donation
* affirm
    - utter_did_that_help
* donation_type[donation_mode=donate in kind]
    - utter_donation_in_kind
* affirm
    - utter_okay_donation_offline
* goodbye
    - utter_goodbye

## Affirm
* affirm
    - utter_did_that_help

## NGO direct information
* greet
    - utter_greet
    - utter_ask
* NGO_search_direct
    - utter_field
* affirm
    - utter_did_that_help
* affirm
    - utter_okay
* goodbye
    - utter_goodbye
