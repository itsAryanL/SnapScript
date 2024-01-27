from flask import Flask 
from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)

@app.route('/video_id')
def hello_world():
    transcript_list = YouTubeTranscriptApi.list_transcripts('video_id')

    YouTubeTranscriptApi.get_transcript('video_id')

    transcript = YouTubeTranscriptApi.get_transcript('video_id', languages=['de', 'en'])

    YouTubeTranscriptApi.get_transcripts(["video_id1", "video_id2"], languages=['de', 'en'])

    YouTubeTranscriptApi.get_transcripts('video_ids', languages=['de', 'en'], preserve_formatting=True)
    return transcript_list.fetch()

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
    return str(transcript)

from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})

from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format': 'bestaudio'})


if __name__ == "__main__":
    app.run(debug=True)