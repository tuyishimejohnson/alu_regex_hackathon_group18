import re
def validate_movie_title(title):
    pattern = r"^(.*?) \(\d{4}\)$"
    match = re.match(pattern, title)
    if match:
        print(title, "is a valid movie title.")
    else:
        print(title, "is not a valid movie title.")
# Example usage:
movie_title = "kevin and kagame (1990)"
validate_movie_title(movie_title)
