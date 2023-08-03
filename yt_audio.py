from pytube import YouTube
def download_audio(video_url, output_path):
    yt = YouTube(video_url)
    audio_stream = yt.streams.get_audio_only()    
    audio_stream.download(output_path )

video_url = "https://www.youtube.com/watch?v=QU_HUDuCGu8"
output_path = "D:\programming"
download_audio(video_url, output_path)

!pip install Whisper 

import Whsiper

model = whisper.load_model(“large”)
text = model.transcribe(“I will find YouI will Kill You Taken Movie best scene ever liam neeson.mp4”)
#printing the transcribe
text['text']