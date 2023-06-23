import streamlit as st
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

def main():
    load_dotenv()
    # print(os.environ["OPENAI_API_KEY"])

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="SQL Query Generator")
    st.header("Get The SQL ✐ ")

    sql_template = '''Convert the following natural language description into a SQL query: {sql_description} '''

    prompt = PromptTemplate(
            input_variables=['sql_description'],
            template=sql_template
        )
    
    llm = OpenAI(temperature=0)
    SQLChain = LLMChain(llm=llm,prompt=prompt)


    question = st.text_input("Generate a SQL Query using English")

    if question is not None:

        # prompt.format(sql_description='select all rows')
        answer = SQLChain.run(question)
        st.write(answer)

if __name__ == "__main__":
    main()

#