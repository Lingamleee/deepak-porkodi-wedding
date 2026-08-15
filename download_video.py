import subprocess
import sys
import os

def run_cmd(args):
    print(f"Running: {' '.join(args)}")
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    return True

def main():
    print("Installing yt-dlp package...")
    if not run_cmd([sys.executable, "-m", "pip", "install", "--quiet", "yt-dlp"]):
        print("Failed to install yt-dlp.")
        return
    
    print("Downloading YouTube video as video.mp4...")
    video_url = "https://youtu.be/ZV450-kdTo4"
    output_path = os.path.join(os.path.dirname(__file__), "video.mp4")
    
    # Use -f "best[ext=mp4]" to ensure a single file format (video + audio merged) is downloaded
    # so that it does not require external ffmpeg installation to combine stream parts.
    import yt_dlp
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_path,
        'quiet': False
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"\nSuccess! Video downloaded to: {output_path}")
    except Exception as e:
        print(f"Error downloading: {e}")

if __name__ == "__main__":
    main()
