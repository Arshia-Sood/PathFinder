import streamlit as st 
import ollama

def main():
    st.markdown(
        """
        <h1 style='text-align: center;
                color: black;
                font-size: 24px;'>
                Career Roadmap
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .stTextInput input{
        background-color: #947070;
        color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.session_state.setdefault("career_conversation_history",[])

    def generate_response(user_input):
        st.session_state["career_conversation_history"].append({"role":"user","content":user_input})
        response=ollama.chat(model="llama3:8b",messages=st.session_state["career_conversation_history"])
        ai_response=response["message"]["content"]
        st.session_state["career_conversation_history"].append({"role":"assistant","content":ai_response})

        return ai_response

    skills=st.text_input("Enter your skills")
    interests=st.text_input("Enter your interests")

    if st.button("Generate Roadmap"):
        if skills.strip() and interests.strip():
            prompt=f"Given these skills {skills} and interests {interests}, suggest a suitable career path and give a step by step roadmap."
            ai_response=generate_response(prompt)
            st.session_state["roadmap_output"]=ai_response
        else:
            st.warning("⚠️ Please enter both skills and interests before generating roadmap.")
            st.session_state.pop("roadmap_output",None)

    st.subheader("Your Career Roadmap")
    if "roadmap_output" in st.session_state:
        st.markdown(st.session_state["roadmap_output"])