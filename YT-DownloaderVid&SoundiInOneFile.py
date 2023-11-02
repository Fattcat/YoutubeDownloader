from pytube import YouTube
from moviepy.editor import *

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"

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

# Combine the video without audio and the extracted audio
final_video = video_clip.set_audio(audio_clip)

# Define the output video file path (use the same video_path to overwrite the original video)
output_video_path = video_path

# Write the final video to the original video file
final_video.write_videofile(output_video_path, codec="libx264")

# Close the final video clip
final_video.close()

# Print a message when the process is complete
print("Video and audio combined successfully in the original video file!")
