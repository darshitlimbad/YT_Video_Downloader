import yt_dlp

from module.download import *
from module.formatting import print_colored_text

def print_license():
    """Prints the license information."""
    license_text = """
        YouTube Video Downloader 2.0 - Youtube Video downloader in Python
        Copyright (C) 2024  Darshit Limbad

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Contact
        For further information or support, please reach out at:
        - Email: darshitlimbad+git@example.com
        - LinkedIn: https://www.linkedin.com/in/darshit-limbad/
    """
    print(license_text)

def main():
    print_license()
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