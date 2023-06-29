import streamlit as st
import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')


# Function to format and display conversation history
def display_conversation(conversation):
    for message in conversation:
        if message['role'] == 'user':
            st.text_area("You: ", value=message['content'], key=message['content'])
        else:
            st.text_area("AI: ", value=message['content'], key=message['content'])


# Main Streamlit app
def main():

    # Display a gif image
    st.image('ZT.gif', width=256)

    st.title('Jarvis AI')

    # Initialize the session state for conversation history if it's not already
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # User input
    user_input = st.text_input('Whats on your mind?', key='user_input')

    if st.button('Send'):
        # Add user input to conversation history
        st.session_state.conversation.append({'role': 'user', 'content': user_input})

        # Generate agent's response
        try:
            agent_response = generate_agent_response(st.session_state.conversation)
            response_content = agent_response['choices'][0]['message']['content']

            # Add agent's response to conversation history
            st.session_state.conversation.append({'role': 'agent', 'content': response_content})

            # Clear the input field
            st.empty()

        except Exception as e:
            st.error("Sorry, I couldn't understand your request. Could you please rephrase or try again?")

    # Display conversation history
    display_conversation(st.session_state.conversation)


# Function to generate agent's response using OpenAI API
def generate_agent_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response


if __name__ == '__main__':
    main()
