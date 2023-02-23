import os
import random
import urllib.request

# Get the user's home directory and use it as the base for the download directory
DOWNLOAD_DIR = os.path.expanduser("~/wallpaper")

# Prompt the user for the number of wallpapers to download (1-10)
num_wallpapers = input("Enter the number of wallpapers you would like to download (1-10): ")

try:
    # Convert the user's input to an integer
    num_wallpapers = int(num_wallpapers)

    # Validate the input to ensure it's between 1 and 10
    if num_wallpapers < 1 or num_wallpapers > 10:
        raise ValueError("Please enter a number between 1 and 10")

    # Loop through the specified number of wallpapers and download each one
    for i in range(num_wallpapers):
        # Set the URL to download the wallpaper from, with a unique signature for each wallpaper
        URL = f"https://source.unsplash.com/random/720x1280/?sig={i+1}"

        # Generate a random file name for the wallpaper
        FILE_NAME = f"wallpaper-{random.randint(10000000, 99999999)}.jpg"
        FILE_PATH = os.path.join(DOWNLOAD_DIR, FILE_NAME)

        # Download the wallpaper to the specified location
        urllib.request.urlretrieve(URL, FILE_PATH)

        # Print a success message with the path to the downloaded wallpaper
        print(f"Wallpaper {i+1} downloaded to: {FILE_PATH}")

except ValueError as e:
    # Handle invalid input errors
    print(f"Error: {e}")
except urllib.error.URLError as e:
    # Handle URL errors
    print(f"Error downloading wallpaper: {e}")
except IOError as e:
    # Handle file I/O errors
    print(f"Error saving wallpaper: {e}")
except Exception as e:
    # Handle all other exceptions
    print(f"Error: {e}")
