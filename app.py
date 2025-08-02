from dotenv import load_dotenv
import os   
from openai import OpenAI
import json
import requests
from PyPDF2 import PdfReader
import gradio as gr
from me.Me import Me

if __name__ == "__main__":
    me = Me()
    gr.ChatInterface(me.chat,type="messages").launch()    

