import argparse
import os

def run(folder="_DOCS"):
    
    topics = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file == 'README.md':
                title = root.split("\\")[-1]
                title = title.replace("_"," ")
                title = title.title()

                string = f"[{title}]({os.path.join(root, file)})".replace("\\","/")
                topics.append(string)

    f = open(f"README.md", "r")
    readme = f.readlines()
    f.close()

    tmp_readme = []
    for line in readme:
        if line.startswith("<!--STARTTOPICS-->"):
            tmp_readme.append(line)
            for topic in topics:
                test = [x for x in readme if x.find(topic) >= 0]
                if len(test) > 0:
                    continue
                tmp_readme.append(f"* [ ] - {topic}\n")
        else:
            tmp_readme.append(line)

    f = open(f"README.md", "w")
    f.writelines(tmp_readme)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add the README.md to the documentation')
    parser.add_argument('--folder', type=str, help='Folder to add the README.md')

    args = parser.parse_args()

    run(folder=args.folder)