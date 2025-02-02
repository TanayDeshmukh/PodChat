import json
import os.path
from typing import Optional, List

from pydantic import BaseModel
from pytube import extract

from data.utils import get_transcript
from pipelines.schemas import Summary
from pipelines.summary_pipeline import run_initial_summary_pipeline


class YoutubeVideo(BaseModel):
    url: str
    video_id: Optional[str] = None
    transcript_sections: Optional[List] = None
    transcript: Optional[str] = None
    summary: Optional[Summary] = None

    def __init__(self, url: str):
        super().__init__(url=url)

        self.video_id = extract.video_id(url=url)
        self.transcript_sections, self.transcript = get_transcript(
            video_id=self.video_id
        )

        # self.summary = run_initial_summary_pipeline(transcript=self.transcript)

        # TODO uncomment the above line and remove the next lines. This code is just for testing purpose.
        cache_file = "cache.json"
        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                summary_data = json.load(f)
            self.summary = Summary.model_construct(**summary_data)
        else:
            self.summary = run_initial_summary_pipeline(transcript=self.transcript)
            with open(cache_file, "w") as f:
                f.write(self.summary.model_dump_json())
