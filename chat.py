import streamlit as st
import openai

##PI KEY

OPEN_AI_API_KEY = 'open ai key'

openai.api_key = OPEN_AI_API_KEY

## to customize our title and favicon
st.set_page_config(page_title='vortex GPT', page_icon = "🤖", layout = 'wide', initial_sidebar_state = 'auto')


st.title("vortex GPT")

#initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

##chatgpt memory initialization 
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

## fills up the session history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




##chat in[put section]
prompt = st.chat_input("Let's Talk!")

## check if there's a messages
if prompt:
    # display content of message
    with st.chat_message("user", avatar="🧑🏾‍🦱"):
        st.markdown(prompt)

    ## add this input to session
    st.session_state.messages.append({'role':'user', 'content':prompt})

    response = f"Echo: {prompt}"

    ## assistant message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages = [
                {"role": m["role"], "content" : m["content"]}
                for m in st.session_state.messages
            ],

            stream = True,
            ):

            full_response += response.choices[0].delta.get("content", " ") 
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content":full_response})

