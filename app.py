import streamlit as st
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

st.title('GeekCook ???? || Recipe Recommendation System')

def generate_recommendations(input_text):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, model="gpt-3.5-turbo-instruct")
        prompt = f"Given the ingredients: {input_text}, suggest an easy-to-cook step-by-step recipe."
        response = llm(prompt)
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

with st.form('my_form'):
    user_input = st.text_area('Enter your preferred ingredients (separated by commas):')
    submitted = st.form_submit_button('Get Recipe Recommendations')

if submitted:
    recommended_recipe = generate_recommendations(user_input)
    st.info(recommended_recipe)