# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ImlForm(FormAction):
    """Interface Info Form"""

    def name(self) -> Text:
        return "iml_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["src", "dest"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        #return {
        #    "src": [
        #        self.from_entity(entity="app",intent="iml_query",role="src"),
        #        self.from_entity(entity="app",intent="iml_query")
        #    ],
        #    "dest" : [
        #        self.from_entity(entity="app",intent="iml_query",role="dest"),
        #        self.from_entity(entity="app",intent="iml_query")
        #    ]
        #}
        return {
            "src": [
                self.from_entity(entity="app",intent="iml_query",role="src"),
                self.from_entity(entity="app",intent="iml_query")
            ],
            "dest": [
                self.from_entity(entity="app",intent="iml_query",role="dest"),
                self.from_entity(entity="app",intent="iml_query")
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message(template='utter_submit')
        dispatcher.utter_message(template='utter_submit', src=tracker.get_slot("src"), dest=tracker.get_slot("dest"))
        return []