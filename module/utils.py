from urllib.parse import urlparse, parse_qs

def get_valid_index(prompt, max_index):
    """
    Prompts the user to enter an index and validates the input.

    Args:
        prompt (str): The message to display to the user when asking for input.
        max_index (int): The maximum valid index value. The user must enter a number between 1 and this value (inclusive).

    Returns:
        int: A valid 0-based index entered by the user.
    """
    while True:
        try:
            # Prompt user for input and convert to integer
            user_input = int(input(prompt))
            
            # Check if the input is within the valid range (1 to max_index inclusive)
            if 1 <= user_input <= max_index:
                # Convert to 0-based index (subtract 1) and return
                return user_input - 1
            else:
                # Inform the user that the input is out of the valid range
                print(f"Invalid input! Please enter a number between 1 and {max_index}.")
        except ValueError:
            # Inform the user that the input is not a valid integer
            print("Invalid input! Please enter a valid number.")

def hook_function(d):
    if d['status'] == 'finished':
        print(f"Downloaded {d['filename']}, now post-processing...")
        
def get_file_size_from_url(url):
    
    # Parse the URL
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    
    # Find the part that contains 'clen' and extract the value
    for part in path_parts:
        if 'clen' in part:
            clen_value = part.split('%3D')[1].split('%3B')[0]             
            break
        
    return int(clen_value) if clen_value else None

def convert_bytes(size_in_bytes=None):
    if not size_in_bytes:
        return None

    # Define the units
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
    
    size = float(size_in_bytes)
    
    # Initialize the unit index
    unit_index = 0
    
    # Loop to convert the size to the appropriate unit
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    
    # Format the size to 2 decimal places and append the unit
    return f"{size:.2f} {units[unit_index]}"