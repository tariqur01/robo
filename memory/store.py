import json
from pathlib import Path
from typing import List,Dict
import streamlit as st


def load_messages(file_path: str) -> List[Dict]:
    """
    Docstring for load_messages
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[Dict]
    """

    path = Path(file_path)
    if not path.exists():
        return []
    
    try:
        with open(path,'r',encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError,IOError):
        return []
    

def save_messages(file_path: str, messages: List[Dict]) -> None:
    """
    Docstring for save_messages
    
    :param file_path: Description
    :type file_path: str
    :param messages: Description
    :type messages: List[Dict]
    """

    path = Path(file_path)

    with open(path,'w',encoding='utf-8') as f:
        json.dump(messages,f,indent=2,ensure_ascii=False)