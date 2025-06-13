"""
1. Use (?:) to avoid capturing the values that are unwanted
2. Use \w or [a-z0-9_] to extract purelly username in url, even the link may have ? or / and etc. after the username

re.sub(pattern, repl, string, count=0, flags=0) could be used to clean up data 
re.split(pattern, string, maxsplit=0, flags=0)
re.findall(pattern, string, flags=0)


"""

import re 

url = input("URL: ").strip()

# Approach Two: Extract the username directly
pattern = r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)"
if matches:= re.search(pattern, url,re.IGNORECASE):
    print(f"Username: {matches.group(1)}")


# Arroach One: Substitue pattern from the string to get the username
# pattern = r"(https?://)?(www\.)?twitter\.com/"
# username = re.sub(pattern, "", url)
# print(username)