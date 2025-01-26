import streamlit as st
from langchain_core.prompts import PromptTemplate

from generator.model import get_llm, get_llm_with_structured_output
from pipelines.schemas import Summary
from pipelines.templates import INITIAL_SUMMARY_TEMPLATE


@st.cache_resource
def run_initial_summary_pipeline(transcript: str) -> Summary:
    prompt = PromptTemplate(
        input_variables=["transcript"], template=INITIAL_SUMMARY_TEMPLATE
    )
    llm = get_llm()
    structured_llm = get_llm_with_structured_output(llm, Summary)

    chain = prompt | structured_llm

    output = chain.invoke({"transcript": transcript})
    return output
