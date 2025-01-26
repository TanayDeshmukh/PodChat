from typing import Optional, List

from pydantic import BaseModel, Field, field_validator


class Summary(BaseModel):
    """
    Summary of the given video transcript.
    This model is designed to capture a structured summary of a long-form video transcript, that includes a title,
    a short summary, a detailed summary, keywords that an optional evaluation score
    """

    title: str = Field(
        ...,
        description="A concise and descriptive title for the transcript.",
    )
    short_summary: str = Field(
        ...,
        description="A very short summary of the given transcript, that is suitable for an introduction or as teaser.",
    )
    summary: str = Field(
        ...,
        description="A summary of the given text, that provides a deeper overview about the transcript.",
    )
    keywords: Optional[List[str]] = Field(
        ...,
        description="a list of relevant keywords or tags extracted from the transcript, useful for categorization or further research.",
    )
    score: Optional[int] = Field(
        default=None,
        description="An optional score (1 to 10) indicating how well the summary describes the input text.",
    )

    @field_validator("keywords", mode="before")
    def validate_keywords(cls, value):
        if value is None:
            return value
        if not isinstance(value, list):
            raise ValueError("Keywords must be a list of strings.")
        return [keyword.strip() for keyword in value if keyword.strip()]

    @field_validator("score")
    def validate_score(cls, value):
        if value is not None and not (1 <= value <= 10):
            raise ValueError("Score must be between 1 and 10.")
        return value
