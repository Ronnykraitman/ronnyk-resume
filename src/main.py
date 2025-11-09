import streamlit as st
import time

from agent import RonnykAgent
from tools.py_tools import set_custom_background

st.set_page_config(layout="wide")

if "messages_history" not in st.session_state:
    st.session_state.messages_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "headline" not in st.session_state:
    st.session_state.headline = False

if "ronnyk_agent" not in st.session_state:
    ronnyk_agent: RonnykAgent = RonnykAgent()
    ronnyk_agent.create_an_agent()
    st.session_state.ronnyk_agent = ronnyk_agent

set_custom_background("../media/ronnyk_background.png")

with open('./style.css') as f:
    css = f.read()

ronnyk_avatar = "../media/ronnyk_profile.jpg"

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


def display_agent_answer(response_text):
    full_response = ""
    message_placeholder = st.empty()
    for chunk in response_text.split():
        full_response += chunk + " "
        time.sleep(0.10)
        message_placeholder.markdown(full_response + "▌")

    message_placeholder.markdown(full_response)

if __name__ == "__main__":
    col_1, col_2 = st.columns([3,2.5])
    with col_2:
        with st.container():
            st.markdown(f"""
                <div class="header-container">
                    <div class="title-container">
                        <div class="title">Hey There, I'm Ronny</div>
                        <div class="title-slogan">Senior Backend Developer</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            if not st.session_state.headline:
                time.sleep(2)
                st.session_state.headline = True
            st.markdown('<div class="prompt"', unsafe_allow_html=True)
            prompt = st.chat_input("Ask me anything you wanna know")

        with st.container(height=400, border=None):

            for message in st.session_state.messages:
                avatar = ronnyk_avatar if message["role"] == "assistant" else "user"
                with st.chat_message(message["role"], avatar=avatar):
                    st.markdown(message["content"])

            if prompt:
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user", avatar="user"):
                    st.markdown(prompt)

                agent_response = st.session_state.ronnyk_agent.chat(prompt)
                st.session_state.messages.append({"role": "assistant", "content": agent_response})

                with st.chat_message("assistant", avatar=ronnyk_avatar):
                    display_agent_answer(agent_response)

                st.rerun()
