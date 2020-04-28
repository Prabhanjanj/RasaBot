# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List

class ActionEnquireStatus(Action):
	def name(self) -> Text:
		return "action_enquire_status"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		 server= tracker.get_slot("server")
		 status="The jvm is up and running"
		 dispatcher.utter_message("Here is the status of the jvm {}:{}".format(server,status))
		 return [SlotSet("status",status)]
