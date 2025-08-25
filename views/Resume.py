import streamlit as st 
import ollama
import fitz

def extract_text(uploaded_file):
    text=""
    doc=fitz.open(stream=uploaded_file.read(),filetype="pdf")
    for page in doc:
        text+=page.get_text()
    return text

def generate_response(resume_text):
    st.session_state["resume_conversation_history"].append({"role":"user","content":resume_text})
    response=ollama.chat(model="llama3:8b",messages=st.session_state["resume_conversation_history"])
    ai_response=response["message"]["content"]
    st.session_state["resume_conversation_history"].append({"role":"assistant","content":ai_response})

    return ai_response

def get_resume_feedback(resume_text):
    prompt=f"You are a professional career coach and here is a resume text:{resume_text}. Please give a detailed review with: 1. Missing sections (Education, Skills, Projects, etc) 2. Suggestions to improve wording and formatting 3.Skills or achievements that should be highlighted 4. A short summary score out of 10"
    ai_response=generate_response(prompt)
    st.session_state["resume_output"]=ai_response
    return ai_response

def main():
    st.markdown(
        """
        <h1 style='text-align: center;
                color: black;
                font-size: 24px;'>
                Resume Reviewer
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.session_state.setdefault("resume_conversation_history",[])

    
    uploaded_file=st.file_uploader("Upload your resume:",type=["pdf"])

    if uploaded_file is not None:
        st.success("Resume uploaded successfully")

        if st.button("Analyse Resume"):
                with st.spinner("Analyzing..."):
                    resume_text=extract_text(uploaded_file)
                    feedback=get_resume_feedback(resume_text)
                st.subheader("Resume Feedback")
                st.write(feedback)


if __name__=="__main__":
    main()
