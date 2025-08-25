import streamlit as st 
import ollama

def main():
    st.markdown(
        """
        <h1 style='text-align: center;
                color: black;
                font-size: 24px;'>
                Free Chat
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<p style='text-align: center; font-size:18px; color: #CD7F32;'>Chat with your career assistant freely and ask any questions.</p>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .stTextInput input{
            background-color: #947070;
            color: white;
        }
        .user-msg{
            color: #004080;
            font-weight: bold;
        }
        .ai-msg{
            color: #CD7F32;
            font-size: italic;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
    st.session_state.setdefault("free_chat_conversation_history",[])

    def generate_response(user_input):
        st.session_state["free_chat_conversation_history"].append({"role":"user","content":user_input})
        response=ollama.chat(model="llama3:8b",messages=st.session_state["free_chat_conversation_history"])
        ai_response=response["message"]["content"]
        st.session_state["free_chat_conversation_history"].append({"role":"assistant","content":ai_response})

        return ai_response
    
    if st.button("Reset Conversation"):
        st.session_state["free_chat_conversation_history"]=[]
        if "user_message" in st.session_state:
            st.session_state["user_meassage"]=""


    for msg in st.session_state["free_chat_conversation_history"]:
        role="You" if msg["role"]=="user" else "AI"
        st.markdown(f"**{role}:**{msg['content']}")

    user_message=st.text_input("How can I help you today?")
    if user_message:
        with st.spinner("Thinking..."):
            ai_response=generate_response(user_message)
            st.markdown(f"**AI:**{ai_response}")

if __name__ == "__main__":
    main()