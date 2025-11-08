import streamlit as st
import time

def display_agent_answer(response_text):
    full_response = ""
    message_placeholder = st.empty()
    for chunk in response_text.split():
        full_response += chunk + " "
        time.sleep(0.10)
        message_placeholder.markdown(full_response + "▌")

    message_placeholder.markdown(f'<div style="text-align:left;"><div class="assistant-msg">{full_response}</div></div>', unsafe_allow_html=True)



#
#
# with st.chat_message("assistant", avatar=RONNY_AVATAR):
#         full_response = ""
#         message_placeholder = st.empty()
#         for chunk in response_text.split():
#             full_response += chunk + " "
#             time.sleep(0.10)
#             message_placeholder.markdown(full_response + "▌")
#
#     message_placeholder.markdown(full_response)