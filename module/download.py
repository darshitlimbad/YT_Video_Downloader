import os
import yt_dlp

from .utils import *
from .formatting import *

def download_video_media(video_url, download_folder, video_format, audio_format):
    ydl_options = {
        'format': f'{video_format}+{audio_format}',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'progress_hooks': [hook_function],
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([video_url])

def download_video(video_url,download_folder:str=".\\Downloads"):
    try:
        if '/playlist?' in video_url:
            download_playlist(video_url)
            return
        
        if not os.path.exists(download_folder):
            os.mkdir(download_folder)
        
        video_only_formats= {}    
        audio_only_formats= {}   
        
        # Get video info
        ydl_opts = {
            'quiet': True,
            'listformats': False,
            'noplaylist': True, 
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)

        print(f"\nProcessing: {video_info['title']}") 
        
        formats = video_info.get('formats', [])
                
        video_only_formats = [f for f in formats if f.get('vcodec','none') != 'none' and f.get('acodec','none') == 'none']
        audio_only_formats = [f for f in formats if f.get('vcodec','none') == 'none' and f.get('acodec','none') != 'none']
        
        if not len(video_only_formats) or not len(audio_only_formats):
            print_colored_text("No Format found\n",fg_color="red")
            return
        
        # Validate and get user input for the desired video and audio
        print_formats(format_type="video",video_only_formats=video_only_formats)   
        print_colored_text(text="Enter Video Index:",fg_color="green")
        video_index = get_valid_index("", len(video_only_formats))
        
        print_formats(format_type="audio",audio_only_formats=audio_only_formats) 
        print_colored_text(text="Enter Audio Index: ",fg_color="green")  
        audio_index = get_valid_index("", len(audio_only_formats))

        # Retrieve the selected format IDs
        video_format = video_only_formats[video_index]['format_id']
        audio_format = audio_only_formats[audio_index]['format_id']
        
        if not video_format or not audio_format:
            print_colored_text("No Format found\n",fg_color="red")
            return
        
        # Download the video with yt-dlp, which will automatically merge video and audio
        download_video_media(video_url, download_folder, video_format, audio_format)
           
    except Exception as e:
        print_colored_text("\nSomething went wrong:",fg_color="red")
        print(e)
         
def download_playlist(playlist_url):
    try:
        if '/watch?' in playlist_url:
            download_video(playlist_url)
            return
    
        download_root = '.\\Downloads'
        if not os.path.exists(download_root):
            os.mkdir(download_root)

        # Get playlist info
        ydl_opts = {
            'quiet': True,
            'listformats': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_info = ydl.extract_info(playlist_url, download=False)
        
        playlist_title = playlist_info.get('title', 'Playlist')
        playlist_folder = os.path.join(download_root, playlist_title)
        
        if not os.path.exists(playlist_folder):
            os.mkdir(playlist_folder)

        print_colored_text(text="\nDownloading Playlist: ",fg_color="green")  
        print(playlist_title)
        print_colored_text(text="Saving files to:",fg_color="green")  
        print(playlist_folder,end="\n\n")

        for entry in playlist_info['entries']:
            video_url = entry['webpage_url'] 
            download_video(video_url,download_folder=playlist_folder)

        print_colored_text(text="\nPlaylist download successfully completed.",fg_color="green")
        print_colored_text(text="\nPlaylist folder:",fg_color="green")
        print(playlist_folder,end="\n\n")
        print("-"*100)

    
    except KeyError as ke:
        print_colored_text("\nProcess Terminated. \nIt looks like you entered a single video URL instead of a playlist URL.",fg_color="red")
        
        if os.path.exists(playlist_folder) and len(os.listdir(playlist_folder)) == 0:
            os.rmdir(playlist_folder)
    except Exception as e:
        print_colored_text("\nSomething went wrong:",fg_color="red")
        print(e)
        
        if os.path.exists(playlist_folder) and len(os.listdir(playlist_folder)) == 0:
            os.rmdir(playlist_folder)
                    