#Changes made by: Daniel Fernandes(M00908452)
greeting = input("Hello, possible pirate! What's the password?") #closing of inverted comma was missing
if greeting in ["Arrr!"]: #The password is stricly Arrr! so we use a for loop to check for the word in a list. But if we use a string it will just check for matching letters.
	print("Go away, pirate.")
else: #was missing an else statement
        print("Greetings, hater of pirates!") #added indentation
