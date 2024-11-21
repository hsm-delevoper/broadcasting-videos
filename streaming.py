import os
import subprocess

# Список видеофайлов для трансляции
video_files = [
    "video1.mp4",
    "video2.mp4",
    "video3.mp4"
]

# RTMP URL
rtmp_url = "rtmp://localhost/live/stream"

def stream_video(video_file):
    # Команда для запуска FFmpeg
    command = [
        'ffmpeg',
        '-re',  # Чтение входного файла в реальном времени
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
    
    # Запуск процесса FFmpeg
    process = subprocess.Popen(command)
    
    # Ожидание завершения процесса
    process.wait()

def main():
    # Цикл по видеофайлам
    for video in video_files:
        print(f"Начинаем трансляцию: {video}")
        stream_video(video)
        print(f"Трансляция завершена: {video}")

if __name__ == "__main__":
    main()