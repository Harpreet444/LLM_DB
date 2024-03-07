import streamlit as st
import sqlite3
import requests
from streamlit_lottie import st_lottie
import dummy as dm
import google.generativeai as genai

## TO access db
def access_db(sql,db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    con.commit()
    con.close()
    for row in rows:
        print(row)
    return rows


# Creating dummb db

try:
    access_db("select * from Student","student.db")

except:
    dm.dummy_db()
 

## API key
genai.configure(api_key = st.secrets["GOOGLE_API_KEY"])

## Loading LLM model

def get_response(que,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],que])
    return response.text


# Prompt:
prompt=["""
    You are an expert in converting English questions to SQL query! 
    but remember dont perform any write,manuplation and delete operation
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS(int) For example, Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """]
prompt_lst=[
    """
    You are an expert in converting English questions to SQL query!
    but remember dont perform any write, manuplation and delete operation
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS(int) For example, Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    if user is asking for write of delete operations simply return 0
    """,
        """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS(int) For example, Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]


## Streamlit front end

st.set_page_config(page_title="LLM Database Application")



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://lottie.host/51416c90-9d01-4bc0-bcf2-7c3d2be918a3/b5tuClLgFV.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("LLM Database Application :")

switch = st.toggle("Authorization")

if switch:
    k = st.text_input("Pass Key",key="pass",type="password")
    if k == st.secrets["pass"]:
        switch = True
        st.write("Write Operation Allowed")
        prompt[0]=prompt_lst[1]

    else:
        switch = False
        st.write("Invalid Pass Key")
        prompt[0]=prompt_lst[0]

else:
    st.write("Only Read Operation Allowed")
    prompt[0]=prompt_lst[0]

question = st.text_input("Input: ",key="input")
submit = st.button("RUN")

# Click on action
if submit:
    response = get_response(question,prompt)
    print(response)
    data = access_db(response,"student.db")
    st.balloons()
    st.subheader("Result :")
    st.table(data)


st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="medium", # medium ; high
    height=None,
    width=None,
    key=None,
)
