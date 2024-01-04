import  zipfile
import pathlib


def make_archive(filepths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepths in filepths:
            archive.write(filepths)

if __name__ == "__main__":
    make_archive(filepths=["Quizapp.py", "gui.py"], dest_dir="destination")