import streamlit as st
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

load_dotenv()
st.set_page_config(page_title="SQL Query Generator")
st.header("Get The SQL✐")

question = st.text_input("Generate a SQL Query using English")

sql_template = '''Convert the following natural language description into a SQL query: {sql_description} '''

prompt = PromptTemplate(
    input_variables=['sql_description'],
    template=sql_template
)

# prompt.format(sql_description='select all rows')

llm = OpenAI(temperature=0.5)
SQLChain = LLMChain(llm=llm,prompt=prompt)

answer = SQLChain.run(question)
st.write(answer)


