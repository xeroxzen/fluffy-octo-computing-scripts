# cyclomatic_example.py
import sys

def main():
    if len(sys.argv) > 1:  # 1
        filepath = sys.argv[1]
    else:
        print("Provide a file path")
        exit(1)
    if filepath:  # 2
        with open(filepath) as fp:  # 3
            for line in fp.readlines():  # 4
                if line != "\n":  # 5
                    print(line, end="")

if __name__ == "__main__":  # Ignored.
    main()
