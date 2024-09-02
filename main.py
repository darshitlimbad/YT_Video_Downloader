import yt_dlp

from module.download import *
from module.formatting import print_colored_text

def main():
    print("-" * 100)
    
    # Display options to the user
    print("Please choose an option for download:")
    print("1. Playlist")
    print("2. Video")
    
    option = input("Enter your choice (1 or 2): ").strip()

    # Execute based on user's choice
    if option == "1":
        print("-" * 100)
        print_colored_text(text="Enter Playlist URL:", fg_color="green")
        playlist_url = input()
        download_playlist(playlist_url)
    elif option == "2":
        print("-" * 100)
        print_colored_text(text="Enter Video URL:", fg_color="green")
        video_url = input()
        download_video(video_url)
    else:
        print_colored_text(text="Invalid choice! Please enter 1 or 2.", fg_color="red")

if __name__ == '__main__':
    main()