# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

# Set up the Streamlit framework
st.title('LLaMA 3 Chatbot 🦙')  # Set the title of the Streamlit app
input_text = st.text_input('How may I help you?')  # Create a text input field in the Streamlit app

# Define a prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please response to the questions'),
        ('user', 'Question: {question}')
    ]
)

# Initialize the Ollama model
llm = Ollama(model='llama3')

# Create a chain that combines the prompt and the Ollama model
chain = prompt|llm

# Invoke the chain with the input text and display the output
if input_text:
    st.write(chain.invoke({'question': input_text}))

