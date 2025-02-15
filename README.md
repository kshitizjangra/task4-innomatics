# Task 4 - Data Science With Gen AI Internship @ Innomatics Research Labs

This repository contains the code and resources for Task 4 - Data Science With Gen AI Internship @ Innomatics Research Labs. The task involves building a web application using Streamlit and integrating it with AI models for code review.

To format the commands and steps with asterisks for emphasis, here’s the updated content:
markdownCopy
# Task 4 - Innomatics

This repository contains the code and resources for Task 4 of the Innomatics program. The task involves building a web application using Streamlit and integrating it with AI models for code review.

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Setting Up Virtual Environment](#setting-up-virtual-environment)
- [Usage](#usage)
- [Application Overview](#application-overview)
- [Steps to Use the Application](#steps-to-use-the-application)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

This repository includes a Streamlit application that uses various AI models to review Python code. The tool can analyze your code, provide fixed code, and explain any errors. The supported models include OpenAI, DeepSeek R1 Distill, and Meta Llama 3 70B Turbo.

## Prerequisites

Before running the application, make sure you have the following installed:

- *Python 3.8 or higher*
- *Git*

## Setting Up Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project. Here are the *steps to set up a virtual environment*:

1. *Install Virtual Environment*:
   If you don't have `virtualenv` installed, install it using pip:

   *pip install virtualenv*

2. *Create a Virtual Environment*:
   Navigate to your project directory and create a virtual environment:

   *cd task4-innomatics*

   *virtualenv venv*

3. *Activate the Virtual Environment*:
   - On Windows: Activate the environment from the Scripts directory:

     *.\venv\Scripts\activate*

   - On macOS and Linux: Activate the environment using the bin directory:

     *source venv/bin/activate*

4. *Install Dependencies*:
   With the virtual environment activated, install the required libraries:

   *pip install streamlit openai requests*

## Usage

1. *Clone the Repository*:
   Download the repository and navigate to its directory:

   *git clone https://github.com/kshitizjangra/task4-innomatics.git*

   *cd task4-innomatics*

2. *Create and Activate the Virtual Environment*:
   Follow the steps in the *Setting Up Virtual Environment* section.

3. *Run the Streamlit Application*:

   *streamlit run app.py*

4. *Open Your Browser*:
   Go to the local server address to access the application:

   *http://localhost:8501*

## Application Overview

The application allows you to input Python code and select an AI model to review the code. The supported models are:

- *OpenAI*
- *DeepSeek R1 Distill*
- *Meta Llama 3 70B Turbo*

## Steps to Use the Application

1. *Enter your API key in the sidebar*.
2. *Select the model you want to use for code review*.
3. *Enter your Python code in the text area*.
4. *Click the "Generate" button to analyze your code*.

The application will display the fixed code and an explanation of any errors.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome and greatly appreciated!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or issues, please open an issue on GitHub or contact the repository owner directly.
This version uses asterisks to emphasize commands, steps, and application features, making them stand out in a user-friendly way.
## Contact

If you have any questions or issues, please open an issue on GitHub or contact the repository owner directly.
