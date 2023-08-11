import os
from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import ImageClip


def extract_frames(video_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_rate = 8

    video_files = sorted([f for f in os.listdir(video_folder) if f.endswith('_video.MP4')])
    for idx, video_file in enumerate(video_files):
        video_path = os.path.join(video_folder, video_file)
        video_output_folder = os.path.join(output_folder, f"video_{idx+1}")
        os.makedirs(video_output_folder, exist_ok=True)

        clip = VideoFileClip(video_path)
        fps = clip.fps

        frame_count = 0
        for t in range(int(clip.duration * frame_rate)):
            frame_time = t / frame_rate
            frame = clip.get_frame(frame_time)
            frame_filename = os.path.join(video_output_folder, f"frame_{frame_count}.jpg")
            frame_clip = ImageClip(frame)
            frame_clip.save_frame(frame_filename)
            frame_count += 1
if __name__ == "__main__":
    video_folder = "D:/videos"  # Specifică calea către videoclip
    output_folder = "D:/frames"  # Specifică calea către folderul de ieșire
    extract_frames(video_folder, output_folder)
