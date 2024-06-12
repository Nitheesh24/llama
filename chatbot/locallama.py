from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] =  "TRUE"
os.environ["LANGCHAIN_APIKEY"] =  os.getenv("LANGCHAIN_APIKEY")

#PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_messages([
    ("system","please respond to client queries responsibly"),
    ("user","Question : {question}")
])
#streamlit framework
st.title("Langchain OLLAMA DEMO")
input_text = st.text_input("search here")

#ollama llm
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
   st.write(chain.invoke({"question":input_text}))
