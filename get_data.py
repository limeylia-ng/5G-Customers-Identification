# data/get_data.py

import os

def download_from_gdrive(file_id, filename):
    try:
        import gdown
    except ImportError:
        os.system("pip install gdown")
        import gdown

    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, filename, quiet=False)

if __name__ == "__main__":
    # Example: replace with your actual file ID and filename
    file_id = "your_file_id_here"
    filename = "your_data.csv"
    
    print(f"Downloading {filename}...")
    download_from_gdrive(file_id, f"data/{filename}")
