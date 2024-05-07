import post
import sys
import os

# Check if the command line argument is provided
if len(sys.argv) < 2:
    print("Usage: python main.py <submission_url>")
    sys.exit(1)

# Assign the first command line argument to submission_url
submission_url = sys.argv[1]

# change to the current directory of the process
os.chdir(os.path.dirname(__file__))


def main():
    post.download(submission_url)


if __name__ == "__main__":
    main()
