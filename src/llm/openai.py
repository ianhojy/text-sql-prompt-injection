from dotenv import load_dotenv
import os
from openai import AzureOpenAI

import sys
sys.path.append('../')

from src.model.openai import MessageRole

class OpenAICompletionEngine:
    
    def __init__(self, cred_source='env', manual_cred={}):
        if cred_source == 'env':
            assert load_dotenv() == True
            self.client = AzureOpenAI(
                api_key = os.getenv("OPENAI_API_KEY"),  
                api_version = os.getenv("OPENAI_API_VERSION"),
                azure_endpoint = os.getenv("OPENAI_BASE_URL")
            )
        elif cred_source == 'manual':
            self.client = AzureOpenAI(
                api_key = manual_cred["OPENAI_API_KEY"],  
                api_version = manual_cred["OPENAI_API_VERSION"],
                azure_endpoint = manual_cred["OPENAI_BASE_URL"]
            )
        else:
            raise Exception("Invalid value for `cred_source`")
    
        self._messages: List[Dict] = list()
        self._model = "gpt-35-turbo"
    
    def set_model(self, model) -> None:
        self._model = model
        
        
    def _insert_system_message(self, message: str) -> None:
        self._messages.append(
            {
                "role": "system",
                "content": message
            })
        
    def _insert_user_message(self, message: str) -> None:
        self._messages.append(
            {
                "role": "user",
                "content": message
            })
        
    def insert_message(self, role: MessageRole, message: str) -> None:
        if role == MessageRole.USER:
            self._insert_user_message(message)
        elif role == MessageRole.SYSTEM:
            self._insert_system_message(message)
        else:
            raise Exception("Message role not valid.")
    
    
    def get_response(self):
        try:
            response = self.client.chat.completions.create(
                model=self._model,
                messages=self._messages
                )
            return response
        except Exception as e:
            print(e)
            
    