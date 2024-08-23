import time
import datetime as dt
import streamlit as st
import requests

url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

today = dt.datetime.today()

with col1:
    st.title("CHAT AI")
    st.subheader("LOGIN")
    username = "BERRY21"
    password = "Nabeelah@21"
    login_details1 = st.text_input("Enter Your username",placeholder="Josh4533")
    login_details2 = st.text_input("Enter Your password")

    if login_details1 == username and login_details2 == password:
        time.sleep(1)
        st.success("LOGIN SUCCESSFUL")
        time.sleep(1)
        with col2:
            user_input = st.text_input("Please How May I Help You?",placeholder="Question")

            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                "system_prompt": "",
                "temperature": 0.9,
                "top_k": 5,
                "top_p": 0.9,
                "max_tokens": 256,
                "web_access": False
            }
            headers = {
                "x-rapidapi-key": "d1efda5bfcmshacb3daae72997eep11f3e5jsnbdaf2b87d985",
                "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
                "Content-Type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)

            result = dict(response.json())
            r = list(result.items())[0]
            for i in r:
                st.info(i)

        # with open("chatbot data", "w") as file:
        #     file.write("")

        with open("chatbot data.txt", "a") as appendFile:
            appendFile.write(f"""{today} Log
\n{user_input}
{result}
\n
""")

    else:
        st.warning("Username or Password is Incorrect")


