import random
import string

def load_word_lists():
    adjectives = ["Cool", "Happy", "Brave", "Smart", "Chill", "Mighty", "Lucky", "Bright"]
    nouns = ["Tiger", "Dragon", "Phoenix", "Wolf", "Eagle", "Lion", "Bear", "Shark"]
    return adjectives, nouns

def generate_username(adjectives, nouns, include_numbers=True, include_specials=True, length=8):
    # Choose a random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine adjective and noun
    base_username = adjective + noun

    # Add numbers if required
    if include_numbers:
        number = str(random.randint(10, 99))
        base_username += number

    # Add special characters if required
    if include_specials:
        special_character = random.choice(string.punctuation)
        base_username += special_character

    # Trim or pad the username to meet the desired length
    if len(base_username) > length:
        base_username = base_username[:length]
    elif len(base_username) < length:
        base_username += ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(base_username)))

    return base_username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            file.writelines(username + "\n" for username in usernames)
        print(f"Usernames successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving usernames: {e}")

def main():
    print("Welcome to the Random Username Generator!")

    adjectives, nouns = load_word_lists()
    
    usernames = []

    while True:
        # Get user preferences
        include_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
        include_specials = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"
        length = int(input("Enter the desired length of the username (minimum 5 characters): "))

        # Validate length
        if length < 5:
            print("The username length should be at least 5 characters. Try again.")
            continue

        # Generate a username
        username = generate_username(adjectives, nouns, include_numbers, include_specials, length)
        usernames.append(username)
        print(f"Generated Username: {username}")

        # Ask if the user wants another username
        another = input("Generate another username? (yes/no): ").strip().lower()
        if another != "yes":
            break

    # Save usernames to a file
    save_usernames_to_file(usernames)

    print("Thank you for using the Random Username Generator!")

if __name__ == "__main__":
    main()
