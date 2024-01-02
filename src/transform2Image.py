import argparse

def run(file):

    import os

    if not os.path.exists(file):
        print("File not found")
        return 0
    
    f =  open(file, 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        print(line.replace('\n', ''))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Get block of coding in a file and transform it to image')
    parser.add_argument('--file', type=str, help='File to transform')

    args = parser.parse_args()

    run(file=args.file)