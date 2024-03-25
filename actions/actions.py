# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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



from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from typing import Any, Dict, List, Text, Optional

class ActionRestarted(Action):
    
    def name(self) -> Text:
        return "action_restart"   
    
    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

        return [Restarted()]
    

    
class ActionTurnOnLight(Action):

    def name(self) -> Text:
        return "action_turn_on_light"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")

        if not location:
            dispatcher.utter_message(text="어디 불을 켜드릴까요?")
        else:
            dispatcher.utter_message(text=f"{location} 조명을 켰습니다.")
        return []
