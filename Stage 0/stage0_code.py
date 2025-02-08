'''
**Project Title: Exploring Python Dictionaries at Stage 0**  
Learners of the team: *Chama Benslimane (leader)* and *Mohammad Hicham Polo*   
**HackBio Internship - Stage 0 Task**
Team members : 
Chama Benslimane (Leader) ; GitHub : https://github.com/BenslimaneChama
and
Mohammad Hicham Polo ; GitHub : https://github.com/MohammadHichamPolo
LinkedIn Video Link : https://www.linkedin.com/feed/update/urn:li:activity:7293763037985976320/
Repository Link : https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%200%20
'''



team_info = {
    "names" : ["Chama Benslimane" , "Mohammad Hicham Polo"],
    "slack_usernames" : ["@Chama" , "@POLO"],
    "emails" : ["benslimanechama@gmail.com" , "mohammad.hicham@um5r.ac.ma"],
    "hobbies" : ["reading" , "sleeping"],
    "countries" : ["Morocco" , "Morocco/Spain"],
    "disciplines" : ["Genomics and Bioinformatics" , "Genomics and Bioinformatics"],
    "preferred_languages" : ["R" , "Python"],
    "messages" : [
        "Never stop learning! Keep pushing your boundaries.",
        "Mathematics and programming go hand in hand. Stay curious!"
    ]
}
print("Names                           :", team_info["names"][0], "           |", team_info["names"][1])
print("Slack Usernames                 :", team_info["slack_usernames"][0], "                     |", team_info["slack_usernames"][1])
print("Emails                          :", team_info["emails"][0], "  |", team_info["emails"][1])
print("Hobbies                         :", team_info["hobbies"][0], "                    |", team_info["hobbies"][1])
print("Countries                       :", team_info["countries"][0], "                    |", team_info["countries"][1])
print("Disciplines                     :", team_info["disciplines"][0], "|", team_info["disciplines"][1])
print("Preferred Programming Languages :", team_info["preferred_languages"][0], "                          |", team_info["preferred_languages"][1])

print("\nMessages to the Community:")
print(f" - * {team_info['messages'][0]} * ")
print(f" - * {team_info['messages'][1]} * ")


print(
    f"Hello! My name is {team_info['names'][0]}, and I am from {team_info['countries'][0]}. "
    f"I specialize in {team_info['disciplines'][0]} and love {team_info['hobbies'][0]} in my free time. "
    f"My favorite programming language is {team_info['preferred_languages'][0]}. "
    f"Here's my message to the community: \"{team_info['messages'][0]}\"\n"
)


print(
    f"Hello! My name is {team_info['names'][1]}, and I am from {team_info['countries'][1]}. "
    f"I specialize in {team_info['disciplines'][1]} and love {team_info['hobbies'][1]} in my free time. "
    f"My favorite programming language is {team_info['preferred_languages'][1]}. "
    f"Here's my message to the community: \"{team_info['messages'][1]}\"\n"
)
