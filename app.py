import streamlit as st
import openai
import requests
import time

# Configure your base URLs for the different APIs 

openai.api_base = "https://api.openai.com/v1"

deepseek_api_base = "https://api.deepseek.com/v1"

llama_api_base = "https://api.llama-ai.com/v1"

st.set_page_config(page_title="AI Code Reviewer Tool", layout="wide")
st.title("AI Code Reviewer Tool")

st.sidebar.title("Configure this before using this tool..")
api_key = st.sidebar.text_input("Enter your API key")
model_choice = st.sidebar.selectbox("Select Model", ["OpenAI", "DeepSeek R1 Distill", "Meta Llama 3 70B Turbo"])

# For Python code input..
user_input = st.text_area("Enter your Python code..")

def generate_response(prompt, model_name, api_base):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model_name,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(
            f"{api_base}/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        st.error(f"API Error: {e}")
        return None

def process_response(response):
    # Remove <think> tags and their closing tags
    response = response.replace("<think>", "").replace("</think>", "")
    return response

if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please enter some code to review..")
    else:
        status_text = st.empty()  # Create an empty placeholder for status updates
        status_text.info("Analyzing your code...")

        time.sleep(2)  # Simulate analysis time

        prompt = f"Review the following Python code and provide both the fixed code and an explanation of any errors:\n\n{user_input}"
        if model_choice == "OpenAI":
            status_text.info("Reviewing with OpenAI...")
            response = generate_response(prompt, "gpt-4o", openai.api_base)  # change model name according to your preference
        elif model_choice == "DeepSeek R1 Distill":
            status_text.info("Reviewing with DeepSeek R1 Distill...")
            response = generate_response(prompt, "deepseek-r1", deepseek_api_base)
        elif model_choice == "Meta Llama 3 70B Turbo":
            status_text.info("Reviewing with Meta Llama 3 70B Turbo...")
            response = generate_response(prompt, "Meta-Llama-3.3-70B-Instruct-Turbo", llama_api_base)

        if response:
            status_text.info("Getting results...")
            time.sleep(2)  # Simulate result fetching time

            # remove the <think> tags of Deepseek R1 Distill model
            response = process_response(response)

            # Split the response into fixed code and explanation
            parts = response.split("\n\n\n\n")
            if len(parts) > 1:
                fixed_code = parts[0]
                explanation = "\n\n".join(parts[1:])
            else:
                fixed_code = response
                explanation = ""

            status_text.empty()

            st.subheader("Review Result..")
            st.code(fixed_code, language="python")

            if explanation:
                st.subheader("Explanation:")
                st.write(explanation)
        else:
            status_text.error("Failed to get a response from the API.")
