## source provided
* greet
  - utter_greet
* iml_query
  - slot{"src":"UFE"}
  - iml_form
  - form{"name":"iml_form"}
  - form{"name":null}

## destination provided
* greet
  - utter_greet
* iml_query
  - slot{"dest":"CRM"}
  - iml_form
  - form{"name":"iml_form"}
  - form{"name":null}

## no slot provided
* greet
  - utter_greet
* iml_query
  - iml_form
  - form{"name":"iml_form"}
  - form{"name":null}

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
