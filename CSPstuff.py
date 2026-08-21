username = "Alice1234"
course_progress = 67

print("Username: " + username)
print("Course Progress (%): " + str(course_progress))

Name = input("Enter username:")
password = input("Enter a secure password:")
print("Welcome " + username + "!")
print("Your password is " + password)

secureKeys = [85, 92, 78, 90]
keySum = 0

for key in secureKeys:
    keySum = key + keySum

print("Verified keysum: " + str(keySum))


passwordStrengthScore=int(88)
def isPasswordSecure(passwordStrengthScore):
	if passwordStrengthScore >= 80:  
		return("Yes")

	elif passwordStrengthScore >= 70:
		return("Consider Strengthening")

	else:
		return("Strengthen immediately")

securityMessage = isPasswordSecure(passwordStrengthScore)
print("Password security status: " + (securityMessage))



passwordStrengthScore = 85
programSecurityScore = 92
firewallScore = 88

passwordStrengthWeight = 0.4
programSecurityWeight = 0.3
firewallWeight = 0.3

finalScore = (passwordStrengthScore * passwordStrengthWeight) + (programSecurityScore * programSecurityWeight) + (firewallScore * firewallWeight)

print("Final Security Score: " + str(finalScore))







confidence = int(input("From 0 to 100, how confident are you in your system security? "))
whatToDo = "Unknown"

if confidence >= 90:
    whatToDo = "You're already good. Don't do anything :)"
else:
    if confidence >= 80:
        whatToDo = "Run a basic antivirus scan."
    else:
        if confidence >= 70:
            whatToDo = "Run a complete antivirus scan."
        else:
            if confidence >= 60:
                whatToDo = "Use a trusted third party antivirus and do a scan"
            else:
                whatToDo = "Reinstall your OS"

print("What you should do: " + whatToDo)

