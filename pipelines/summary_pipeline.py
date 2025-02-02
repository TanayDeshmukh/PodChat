import streamlit as st
from langchain_core.prompts import PromptTemplate, SystemMessagePromptTemplate

from generator.model import get_llm, get_llm_with_structured_output
from pipelines.prompts import get_prompt_template
from pipelines.schemas import Summary
from pipelines.templates import INITIAL_SUMMARY_TEMPLATE


def build_summarization_pipeline():
    summarization_prompt_template = get_prompt_template(task="summary")
    summarization_prompt = PromptTemplate.from_template(
        template=summarization_prompt_template
    )
    llm = get_llm()
    structured_llm = get_llm_with_structured_output(llm, Summary)

    chain = summarization_prompt | structured_llm

    return chain


@st.cache_resource
def run_initial_summary_pipeline(transcript: str) -> Summary:
    chain = build_summarization_pipeline()

    output = chain.invoke({"transcript": transcript})
    return output
