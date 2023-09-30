from typing import Text, Dict, Any, List
import rasa
import rasa_sdk
from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher

class email_sending(Action):
    def name(self):
        return "action_send_email"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
        print("custom code goes here")
        return []