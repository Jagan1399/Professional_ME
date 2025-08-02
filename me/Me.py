from dotenv import load_dotenv
import os   
from openai import OpenAI
import json
from PyPDF2 import PdfReader
from tools.tools_def import record_unknown_question_json, record_user_details_json, record_user_details, record_unknown_question
from prompts.prompts import system_prompt

# filepath: /Users/jaganrm/Downloads/MY_PROJECTS/Professionally Me!/me/Me.py
TOOL_FUNCTIONS = {
    "record_user_details_json": record_user_details_json,
    "record_unknown_question_json": record_unknown_question_json,
}

load_dotenv()

class Me:
    def __init__(self):
        self.gemini = OpenAI(base_url=os.getenv("GEMINI_URL"), api_key=os.getenv("GEMINI_KEY"))
        self.name = "Jagan"
        self.linkedin = self.load_linked_profile()
        self.tools = [
            {"type":"function", "function":record_user_details_json},
            {"type":"function", "function":record_unknown_question_json}
        ]


    def load_linked_profile(self):
        reader =  PdfReader("me/Profile.pdf")
        linkedin = ""
        self.summary = ""
        for page in reader.pages:
            linkedin += page.extract_text()
            with open("me/about_me.txt", "r", encoding="utf-8") as f:
                self.summary = f.read()
        return linkedin
    
    
    def handle_tool_calls(self, tool_calls):
        responses = []
        for tool_call in tool_calls:
            tool_name=tool_call.function.name
            print(tool_call)
            tool_arguments=json.loads(tool_call.function.arguments)
            print(f"Tool call: {tool_name} with arguments {tool_arguments}",flush=True)
            tool = globals().get(tool_name)
            result = tool(**tool_arguments) if tool else {}
            '''if tool_name == "record_user_details":
                response = record_user_details(**tool_arguments)
            elif tool_name == "record_unknown_question":
                response = record_unknown_question(**tool_arguments)
            else:
                response = {"error": "Unknown tool call"}
            print("About to serialize response", flush=True)
            print(response, flush=True)'''
            responses.append({"role":"tool","content":json.dumps(result), "tool_call_id":tool_call.id})
        return responses

    def system_prompt(self):
        system_prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills and experience. \
Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
You are given a summary of {self.name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        system_prompt += f"\n\n## Summary:\n{self.summary}\n\n## LinkedIn Profile:\n{self.linkedin}\n\n"
        system_prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return system_prompt

    def chat(self, message, history):
        messages = [{"role":"system", "content":self.system_prompt()}] + history + [{"role":"user", "content":message}]
        done = False
        while not done:
            try:
                response = self.gemini.chat.completions.create(
                    model="gemini-2.5-flash",
                    messages=messages,
                    tools=self.tools
                )
                finish_reasoning = response.choices[0].finish_reason
                if finish_reasoning == "tool_calls":
                    message = response.choices[0].message
                    tool_calls = getattr(message,"tool_calls", [])
                    result = self.handle_tool_calls(tool_calls)
                    messages.append(message)
                    messages.extend(result)
                    print(message, flush=True)
                else:
                    done = True
            except Exception as e:
                print(f"Error: {e}", flush=True)
                return "An error occurred, please try again later."
        return response.choices[0].message.content
        