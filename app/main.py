import time

import streamlit as st
from streamlit.runtime.media_file_storage import MediaFileStorageError

from data.data_classes import YoutubeVideo


def stream_response(response: str):
    for word in response.split():
        yield word + " "
        time.sleep(0.08)


def run_app():
    st.set_page_config(
        page_title="Chat with a podcast!",
        page_icon="💬",
        layout="wide",
    )

    with st.sidebar:
        youtube_url = st.text_input("Enter the YouTube url")
        if youtube_url:
            try:
                st.video(youtube_url)
                with st.spinner("Processing..."):
                    st.session_state.youtube_video = YoutubeVideo(url=youtube_url)
            except MediaFileStorageError as m:
                st.error(f"Invalid {youtube_url=}")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "youtube_video" not in st.session_state:
        st.session_state.youtube_video = None

    if st.session_state.youtube_video:
        st.title(st.session_state.youtube_video.summary.title)
        initial_system_message = (
            st.session_state.youtube_video.summary.summary
            + "\n"
            + "Would you like to know anything more about this topic?"
        )
        with st.chat_message("assistant"):
            st.write_stream(stream_response(initial_system_message))

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What would you like to know?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    run_app()
