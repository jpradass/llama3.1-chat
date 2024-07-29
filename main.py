import ollama
import streamlit as st


def get_ai_response(messages):
    try:
        response = ollama.chat(model="llama3.1", messages=messages)
        return response["message"]["content"]
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None


def main():
    st.title("Chat with Llama 3.1")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is your message?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        ai_response = get_ai_response(st.session_state.messages)

        with st.chat_message("assistant"):
            st.markdown(ai_response)

        st.session_state.messages.append({"role": "assistant", "content": ai_response})


if __name__ == "__main__":
    main()
