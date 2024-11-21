import os
import subprocess

video_files = [
    "video1.mp4",
    "video2.mp4",
    "video3.mp4"
]

# RTMP URL
rtmp_url = "rtmp://localhost/live/stream"

def stream_video(video_file):
    command = [
        'ffmpeg',
        '-re', 
        '-i', video_file,
        '-c:v', 'libx264',
        '-preset', 'veryfast',
        '-maxrate', '1000k',
        '-bufsize', '2000k',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-f', 'flv',
        rtmp_url
    ]
    
    process = subprocess.Popen(command)
    process.wait()

def main():
    for video in video_files:
        print(f"Starting the broadcast: {video}")
        stream_video(video)
        print(f"Broadcast completed: {video}")

if __name__ == "__main__":
    main()
