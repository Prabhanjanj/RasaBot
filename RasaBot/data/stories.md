## restart Jvms happy path
* greet
  -utter_how_can_i_help
* inform_server{"server":"sit10abcde","environment":"sit"}
  -action_enquire_status
  -slot{"status":"The jvm is up and running"}
* thanks
  -utter_goodbye

## restart server
* greet
  -utter_how_can_i_help
* inform_server{"server":"sit10abcde"}
  -utter_ask_environment
* inform_environment{"environment":"sit"}
  -action_enquire_status
  -slot{"status":"The jvm is up and running"}
* thanks
  -utter_goodbye 

## restart+status
* greet
  -utter_how_can_i_help
* jvm_details{"environment":"sit"}
  -utter_ask_server_name
* inform_server{"server":"sit10abcde"}
  -action_enquire_status
  -slot{"status":"The jvm is up and running"}
* thanks
  -utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_how_can_i_help

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
