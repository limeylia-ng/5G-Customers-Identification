import os

def load_data_from_gdrive(file_id, filename):
    import gdown
    url = f"https://drive.google.com/file/d/{file_id}/view?usp=drive_link"
    gdown.download(url, filename, quiet=False)

if __name__ == "__main__":
    load_data_from_gdrive("1mLHN5RRKy5FaU06TigpFtINhk09Y83Gn", "data/train_set")
    load_data_from_gdrive("1XzYq81ej6qYoxXx1UBNe-bOcic1qUktV", "data/train_label")
