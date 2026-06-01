from dataclasses import dataclass
from enum import Enum

class DownloadStatus(Enum):
    QUEUED = "queued"
    DOWNLOADING = "downloading"
    PROCESSING = "processing"
    UPLOADING = "uploading"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class TrackInfo:
    url: str
    title: str
    artist: str
    duration: int
    thumbnail: str = ""
