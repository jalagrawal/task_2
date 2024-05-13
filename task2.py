from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def extract_frames(video_url, duration):
    
    clip = VideoFileClip(video_url)
    
    
    output_folder = "extracted_frames"
    os.makedirs(output_folder, exist_ok=True)
    
    
    start_time = 0
    end_time = start_time + duration
    
    
    for i, frame in enumerate(clip.iter_frames(t=[start_time, end_time], fps=clip.fps)):
        frame_path = os.path.join(output_folder, f"frame_{i}.jpg")
        frame.save_frame(frame_path)
    
    
    clip.close()


video_url = "https://drive.google.com/file/d/1eOlOXn5joaUFRFB4j1MPpbkoP9fU8D42/view?usp=sharing"
duration = 10  
extract_frames(video_url, duration)
