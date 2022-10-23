# Instagram-dp_download
# Provide the username & get the dp of that person downloaded.
import instaloader
il = instaloader.Instaloader()
username = input("Enter username: ")
il.download_profile(username, profile_pic_only = True)
print(f"{username}'s DP is downloaded!!! ")
