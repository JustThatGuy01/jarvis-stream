# Jarvis AI - OpenAI Chatbot

This repository contains the source code for a simple chatbot application using Streamlit 
and OpenAI's GPT-3 model. The application allows users to interact with an AI agent through 
a user-friendly interface.

![Jarvis AI App](ZT.gif)

## Requirements

- Streamlit
- OpenAI
- Requests
- Python-Dotenv
- Python 3.10+

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/JustThatGuy01/jarvis-stream.git
    ```

2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

3. Make a simple .env file for your openai api key
    ```
    openai.api_key='place_your_api_key_here'
    ```

4. Run the Streamlit app:
    ```
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser. The app should be running at `http://localhost:8501`.
2. Type your message in the text field and press 'Send'.
3. The AI response will appear below your message.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what 
you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
