import time
from dotenv import load_dotenv
import os
#from google import genai
import streamlit as st
from openai import OpenAI

BASE_URL = 'http://127.0.0.1:11434/v1/'
MODEL = "qwen2.5:0.5b"

###################################################################################
# This portion uses OpenAI style API to connect to local AI model "qwen2.5:0.5b"
# hosted through Ollama.
###################################################################################
def generate_ollama_stream(prompt, system: str, api_key:str):
    """
    Docstring for generate_ollama_stream
    
    :param prompt: Description
    :type prompt: str
    :param system: Description
    :type system: str
    """

    client = OpenAI(
        base_url= BASE_URL,
        api_key=api_key
    )
    prm = [
            {
            'role':'system',
            'content':system
            }
        ]  + prompt
    
    
    response = client.chat.completions.create(
        messages=prm,
        model=MODEL,
        stream=True
    )
    
    for chunk in response:
        token = chunk.choices[0].delta.content
        yield token

    
    
    