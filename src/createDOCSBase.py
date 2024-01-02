import argparse
import os
import datetime

def run(folder,subject):
    
    if os.path.isdir(f"_DOCS/{folder}"):
        print(f"Folder _DOCS/{folder} already exists")
    else:
        os.makedirs(f"_DOCS/{folder}")

    subject = subject.replace(" ","_")
    if os.path.isdir(f"_DOCS/{folder}/{subject}"):
        print(f"Folder _DOCS/{folder}/{subject} already exists")
    else:
        os.makedirs(f"_DOCS/{folder}/{subject}")

    if os.path.isfile(f"_DOCS/{folder}/{subject}/README.md"):
        print(f"File _DOCS/{folder}/{subject}/README.md already exists")
    else:
        f = open(f"_DOCS/{folder}/{subject}/README.md", "w")
        f.write(f"# {subject}\n\n")
        f.write(f"---\n\n")
        f.write(f"creation: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"---\n\n")
        f.write(f"## Description\n\n")
        f.write(f"## Examples\n\n")
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create the base of the documentation')
    parser.add_argument('--folder', type=str, help='Folder to create the documentation')
    parser.add_argument('--subject', type=str, help='Subject of the documentation')

    args = parser.parse_args()

    run(folder=args.folder,subject=args.subject)