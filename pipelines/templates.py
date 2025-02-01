BASE_TEMPLATE = (
    "Intro: You are provided with a transcript of a youtube video and the the task that you are supposed to perform."
    "Make sure that you stick to the given task.\n\n"
    "Transcript: {transcript}\n\n"
)

INITIAL_SUMMARY_TEMPLATE = (
    BASE_TEMPLATE + "Task: Generate a concise summary of the given video transcript.\n"
)

CHAT_TEMPLATE = BASE_TEMPLATE + "Task: "
