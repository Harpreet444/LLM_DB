# LLM Database Application

This project is a simple Streamlit web application that uses a Generative Language Model (LLM) to convert natural language questions into SQL queries for querying a database. The database (`student.db`) consists of student records with columns `NAME`, `CLASS`, `SECTION`, and `MARKS (int)`. The application supports both read and write operations, with write operations being secured via password authentication.

## Features

- **Natural Language to SQL**: Converts English questions into SQL queries.
- **Secure Access**: Write operations are restricted and require a password.
- **Lottie Animations**: A friendly interface enhanced with Lottie animations.
- **Database Interaction**: Retrieve data from an SQLite database with `access_db` function.
  
## Prerequisites

1. Python 3.x
2. Streamlit
3. SQLite3
4. Requests
5. [Streamlit-Lottie](https://github.com/andfanilo/streamlit-lottie)
6. [Google Generative AI](https://developers.generativeai.google)
7. A SQLite database (`student.db`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/llm-database-app.git
    cd llm-database-app
    ```

2. Install the required dependencies:
    ```bash
    pip install streamlit sqlite3 requests streamlit-lottie google-generativeai
    ```

3. Set up your environment:
    - Store your **Google Generative AI** API key in `secrets.toml` as follows:
      ```toml
      [secrets]
      GOOGLE_API_KEY = "your-google-api-key"
      pass = "your-password"
      ```

4. Create the `student.db` SQLite database (or use the `dummy_db()` function from the included `dummy.py` module to generate one).

## Running the Application

To run the Streamlit application, execute the following command:

```bash
streamlit run app.py
