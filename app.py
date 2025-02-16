import streamlit as st
import os 
from google import genai
from google.genai import types

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

client = genai.Client(api_key=GOOGLE_API_KEY)

MODEL_ID = "gemini-2.0-pro-exp-02-05"

st.title("Test Case Generator")

user_story = st.text_area("Enter User Story/Requirement:")

if st.button("Generate Test Cases"):
    if user_story:
        with st.spinner("Generating Test Cases..."): 
            prompt = f"""You are a helpful assistant that generates test cases for software requirements. 
                Generate a comprehensive set of test cases for the following user story. 

                Format the test cases clearly, including:
                * **Test Case ID:**(e.g., TC-001,TC-002)
                * **Test Case Description:**(Briefly describe the test)
                * **Test Steps:**(Numbered steps to execute the test)
                * **Expected Results:**(What should happen if the test passes)
                * **Test data:**(if specific data is needed, mention it)

                Be concise but thorough, covering both positive and negative scenarios.
                Do NOT include any introductory or concluding text. Output ONLY the test cases.

                User Story:
                {user_story}"""
            try:

                response = client.models.generate_content(model=MODEL_ID, contents=prompt)
                st.markdown(response.text)

            except Exception as e:
                st.error(f"An error occurred:{e}")

    else:
        st.warning("Please enter a user story.")









        



