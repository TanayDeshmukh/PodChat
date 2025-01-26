import streamlit as st
from langchain_core.runnables.base import RunnableSequence

from langchain_openai import ChatOpenAI
from pydantic import BaseModel


@st.cache_resource
def get_llm(model: str = "gpt-4o-mini") -> ChatOpenAI:
    llm = ChatOpenAI(model=model)
    return llm


@st.cache_resource
def get_llm_with_structured_output(
    _llm: ChatOpenAI, output_schema: BaseModel
) -> RunnableSequence:
    llm_with_structured_output = _llm.with_structured_output(schema=output_schema)
    return llm_with_structured_output
