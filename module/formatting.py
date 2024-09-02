from .utils import get_file_size_from_url , convert_bytes

# ascii escape codes 
esc_codes = {
    # color codes
    'fore': {
        'red': '\033[31m',       # Red text
        'green': '\033[32m',     # Green text
        'bright_red': '\033[91m',     # Bright Red text
        'bright_green': '\033[92m',   # Bright Green text
        'dark_grey': '\033[90m',       # Dark Grey text
        'reset': '\033[39m',      # Reset to default foreground
    },
    'back': {
        'red': '\033[41m',       # Red background
        'green': '\033[42m',     # Green background
        'light_red': '\033[101m',       # Light Red background
        'light_green': '\033[102m',     # Light Green background
        'light_yellow': '\033[103m',    # Light Yellow background
        'light_blue': '\033[104m',      # Light Blue background
        'light_magenta': '\033[105m',   # Light Magenta background
        'light_cyan': '\033[106m',      # Light Cyan background
        'light_white': '\033[107m',     # Light White background
        'reset': '\033[49m',      # Reset to default background

    },
    
    'bold': '\033[1m',  # Bold text attribute
    'underline': '\033[4m',  # Underlined text attribute
    
    'reset': '\033[0m',      # Reset all attributes  
}


def print_formats(format_type:str="video", video_only_formats:dict =None, audio_only_formats:dict =None):
    """
    Prints available formats in a structured table format based on the format type.

    Args:
        format_type (str): Type of formats to print, either 'video' or 'audio'.
        video_only_formats (list, optional): A list of dictionaries containing video format information.
        audio_only_formats (list, optional): A list of dictionaries containing audio format information.
    
    Description:
        This function displays the available formats (video or audio) in a tabular format.
        It includes headers for each column and prints a list of formats with their details.
        Each format is displayed with an index, which allows users to choose a format based
        on its number.
    """

    if format_type == 'video':
        header = f"{f'{esc_codes['fore']['bright_green']}Index{esc_codes['reset']}':<5} {'Format ID':<15} {'Codec':<15} {'Resolution':<20} {'FPS':<10} {'Filesize':<20}"
        formats = video_only_formats
        fields = ['format_id', 'vcodec', 'format_note', 'fps', 'filesize']
    elif format_type == 'audio':
        header = f"{f'{esc_codes['fore']['bright_green']}Index{esc_codes['reset']}{esc_codes['bold']}':<5} {'Format ID':<15} {'Codec':<15} {'Quality':<20} {'Filesize':<20}"
        formats = audio_only_formats
        fields = ['format_id', 'acodec', 'format_note', 'filesize']
    else:
        raise ValueError("Invalid format type. Choose 'video' or 'audio'.")

    heading = f"\n{esc_codes['bold']}{esc_codes['fore']['green']}Available {format_type} formats:{esc_codes['reset']}"
    print(heading)
    print("=" * len(header))  # Separator line
    print(f'{esc_codes['bold']}{header}{esc_codes['reset']}')            # Print the formats header    
    print("=" * len(header))  # Separator line
    
    for i, f in enumerate(formats, start=1):
            
        filesize = convert_bytes(f.get('filesize')) or f"{esc_codes['fore']['dark_grey']} ~ {convert_bytes(get_file_size_from_url(f.get('url')))} ( dash ) {esc_codes['reset']}"

       
        # Define the common elements for both video and audio
        base_format = (f"{esc_codes['fore']['green']}{esc_codes['bold']}{i:<5}{esc_codes['reset']} "
                    f"{f.get(fields[0], 'N/A'):<15} {f.get(fields[1], 'N/A'):<15} {f.get(fields[2], 'N/A'):<20}")

        # Add specific details based on the format type
        if format_type == 'video':
            print(f"{base_format} {f.get(fields[3], 'N/A'):<10} {filesize:<20}")
        elif format_type == 'audio':
            print(f"{base_format} {filesize:<20}")
            
    print("=" * len(header))

def print_colored_text(text, fg_color=None, bg_color=None):
    """
    Prints text with specified foreground and background colors, with an option to reset color attributes.

    Args:
        text (str): The text to print.
        fg_color (str, optional): The foreground color. Choices: 'red', 'green', 'bright_red', 'bright_green', etc.
        bg_color (str, optional): The background color. Choices: 'light_red', 'light_green', etc.
        reset (str, optional): The type of reset. Choices: 'all', 'foreground', 'background'.
    """
    fg_code = esc_codes['fore'].get(fg_color, '')
    bg_code = esc_codes['back'].get(bg_color, '')
    reset_code = esc_codes['reset']

    # Print text with color codes
    print(f"{fg_code}{bg_code}{text}{reset_code}",end="")