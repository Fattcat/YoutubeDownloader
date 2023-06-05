from pytube import YouTube
from moviepy.editor import *

# YouTube video URL
video_url = "PASTE SOME YOUTUBE VIDEO FOR DOWNLOAD HERE :D"

# Provide the YouTube video URL and create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution video stream
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_path = video_stream.download()

# Create a VideoFileClip object from the downloaded video
video_clip = VideoFileClip(video_path)

# Extract the audio from the video clip
audio_clip = video_clip.audio

# Define the output audio file path
audio_file_path = "audio.mp3"

# Save the audio clip as an audio file
audio_clip.write_audiofile(audio_file_path)

# Close the video and audio clips
video_clip.close()
audio_clip.close()

# Print a message when the download is complete
print("Video and audio downloaded successfully!")
