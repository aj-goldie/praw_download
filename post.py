import praw
from datetime import datetime


def download(submission_url):
    reddit = praw.Reddit(
        client_id="ArUzEr_tNWzicweDbQrVkg",
        client_secret="PK71knuBREIYAnimfBrT5FyanVPDmg",
        user_agent="BAI app by u/ajgoldie",
    )
    submission = reddit.submission(url=submission_url)

    # Function to create a safe filename from the title
    def create_safe_filename(title):
        safe_title = []
        for i, c in enumerate(title):
            if c.isalnum() or c in " _-":
                safe_title.append(c)
            elif i == len(title) - 1:  # Check if it's the last character
                safe_title.append("")
            else:
                safe_title.append("_")
        return "".join(safe_title)

    # Generate filename based on the post title
    filename = "output_posts/" + create_safe_filename(submission.title) + ".txt"

    # Convert the UTC timestamp to a datetime object
    submission_datetime = datetime.utcfromtimestamp(submission.created_utc)
    # Format the datetime object to the specified format mm-DD-YY
    submission_date = submission_datetime.strftime("%m-%d-%y")

    # Calculate the number of asterisks
    asterisks = "=" * (len(submission.title) + 8)

    # Open the file to write
    with open(filename, "w") as file:
        file.write(f"=== {submission.title} ===     {submission_date}\n")
        file.write(asterisks + "\n\n")
        file.write(f"{submission.selftext}\n")
        file.write(f"-{submission.author}\n\n")
        file.write(asterisks + "\n\n")

        def print_comments(comment, level=0, file=file):
            indent = "  " * level

            file.write(f"{indent}{comment.body}\n")
            file.write(f"{indent}-{comment.author} ({comment.score})\n\n")

            for reply in comment.replies:
                print_comments(reply, level + 1, file)

        file.write("\n")
        submission.comments.replace_more(limit=None)  # Retrieve all comments
        for comment in submission.comments:
            print_comments(comment)

    print(f"Data written to {filename}")


if __name__ == "__main__":
    download()
