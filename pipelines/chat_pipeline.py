import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)

from generator.model import get_llm
from pipelines.prompts import get_prompt_template


def build_chat_pipeline():
    chat_prompt_template = get_prompt_template(task="chat")
    llm = get_llm()

    chat_template = ChatPromptTemplate.from_messages(
        [
            chat_prompt_template,
            MessagesPlaceholder("history"),
            HumanMessagePromptTemplate.from_template(template="{query}"),
        ]
    )

    chain = chat_template | llm

    return chain


@st.cache_resource
def run_chat_pipeline(query: str):
    chain = build_chat_pipeline()

    transcript = st.session_state.youtube_video.transcript
    history = st.session_state.messages

    output = chain.invoke(
        {
            "transcript": transcript,
            "history": history,
            "query": HumanMessage(query),
        }
    )

    return output.content
