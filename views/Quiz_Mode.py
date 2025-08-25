import streamlit as st 
import ollama

def main():
    st.markdown(
        """
        <h1 style='text-align: center;
                color: black;
                font-size: 24px;'>
                Quiz Mode
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    .stRadio label {
        font-size: 28px;
        color: black;
        margin-bottom: 8px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    
        
    st.session_state.setdefault("quiz_conversation_history",[])

    
    def generate_response(user_input):
        st.session_state["quiz_conversation_history"].append({"role":"user","content":user_input})
        response=ollama.chat(model="llama3:8b",messages=st.session_state["quiz_conversation_history"])
        ai_response=response["message"]["content"]
        st.session_state["quiz_conversation_history"].append({"role":"assistant","content":ai_response})

        return ai_response

    q1=st.radio("What are the subjects you enjoy studying the most?",["Maths","Science","Arts","Commerce"])       
    q2=st.radio("Do you enjoy working with numbers?",["Yes","No"])
    q3=st.radio("Which excites you more?",["Building things","Solving problems","Helping others"])

    if st.button("Get Career Suggestion"):
        answer={"Q1":q1,"Q2":q2,"Q3":q3}
        prompt=f"Based on these answers {answer}, suggest 3 possible careers and learning roadmap."
        ai_response=generate_response(prompt)
        st.session_state["quiz_output"]=ai_response

    st.subheader("Suggested Careers")
    if "quiz_output" in st.session_state:
            st.markdown(
            f"<div style='color: black; font-size: 18px;'>{st.session_state['quiz_output']}</div>",
            unsafe_allow_html=True
            )