from stage1library import hamming_distance
slack_username = input("Paste your slack_username")
X_username = input("Paste your X_username")
print(f"the hamming distance between your slack username and X username is {hamming_distance(slack_username, X_username)}")