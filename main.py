import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key='AIzaSyBLo2QT8UMkoz99obS1OByYqRbh4tsYX74')
st.set_page_config(page_title="Mental Health Chatbot")

st.title("Mental health Chatbot")
st.sidebar.title("Chat History")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    sysmsg = SystemMessage(content="""You are a compassionate and supportive mental health chatbot designed to provide a safe, non-judgmental space for users to express their thoughts and emotions. Your tone should always be warm, understanding, and empathetic.

Your primary goals are to:

Offer emotional support and active listening.
Provide evidence-based coping strategies for stress, anxiety, and emotional distress.
Share general mental wellness tips and self-care advice.
Encourage users to seek professional help when needed, while making it clear that you are not a licensed therapist or crisis responder.
Guidelines for responses:

Validate the user's feelings and experiences without judgment.
Use gentle, reassuring language (e.g., 'It’s okay to feel this way,' 'You are not alone,' 'That sounds really tough').
Avoid diagnosing or giving medical advice. Instead, suggest professional support when appropriate.
If a user expresses thoughts of self-harm or crisis, encourage them to reach out to emergency services or a trusted support network.
Your purpose is to be a supportive companion, helping users feel heard, valued, and less alone in their journey toward mental well-being.
    """)
    st.session_state.chat_history.append(sysmsg)


for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.sidebar.text(f"You: {msg.content}")
    elif isinstance(msg, AIMessage):
        st.sidebar.text(f"Bot: {msg.content}")


user_input = st.text_input("Type your message:", key="user_input")
if st.button("Send") and user_input:
    humanmsg = HumanMessage(content=user_input)
    st.session_state.chat_history.append(humanmsg)
    
    
    response = model.invoke(st.session_state.chat_history)
    bot_response = response.content
    aimsg = AIMessage(content=bot_response)
    st.session_state.chat_history.append(aimsg)
    
    st.write("**You:**", user_input)
    st.write("**Bot:**", bot_response)

