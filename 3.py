import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria Checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%).")

    # Strength Rating
    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Moderate 🧐"
    else:
        strength = "Weak 😟"

    return strength, feedback

# Sample usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("\nSuggestions to improve your password:")
        for tip in suggestions:
            print(f"- {tip}")
