from common.constants import BASE_SYSTEM_PROMPT, task_map


def get_prompt_template(task: str) -> str:
    prompt_template = (
        f"{BASE_SYSTEM_PROMPT}\n\nTranscript: {{transcript}}\n\nTask: {task_map[task]}"
    )
    return prompt_template
