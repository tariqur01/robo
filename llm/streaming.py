from llm.ollama_client import generate_ollama_stream#, init_gemini_client
from typing import Generator,Tuple



def generate_streaming_response(user_prompt, system_prompt: str = "") -> Generator[Tuple[str,bool],None,None]:
    """
    Docstring for generate_streaming_response
    
    :param user_prompt: Description
    :type user_prompt: str
    :param system_prompt: Description
    :type system_prompt: str
    :return: Description
    :rtype: Generator[Tuple[str, bool], None, None]
    """
    for token in generate_ollama_stream(user_prompt,system_prompt,api_key='ollama'):
        yield token


