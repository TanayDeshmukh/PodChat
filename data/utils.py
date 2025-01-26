from typing import Tuple, List, Dict, Union

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi


@st.cache_data
def get_transcript(video_id: str) -> Tuple[List[Dict[str, Union[str, float]]], str]:
    transcript_sections = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join([section["text"] for section in transcript_sections])

    return transcript_sections, transcript_text
