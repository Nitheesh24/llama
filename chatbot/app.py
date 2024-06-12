from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()
#to capture all monitoring results Langsmith Tracking
os.environ["OPENAI_APIKEY"] =  os.getenv("OPENAI_APIKEY")
os.environ["LANGCHAIN_TRACING_V2"] =  "TRUE"
os.environ["LANGCHAIN_APIKEY"] =  os.getenv("LANGCHAIN_APIKEY")

#PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_messages([
    ("system","please respond to client queries responsibly"),
    ("user","Question : {question}")
])
#streamlit framework
st.title("Langchain OPENAI DEMO")
input_text = st.text_input("search here")

#openAI llm 
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
   st.write(chain.invoke({"question":input_text}))

