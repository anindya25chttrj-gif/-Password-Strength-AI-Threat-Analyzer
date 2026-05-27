def analyze_password(password):
    # Base security score
    score = 0
    feedback = []

    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (Minimum 8 characters needed).")

    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Missing numbers (0-9).")

    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("Missing special characters (e.g., @, #, $).")


    print("\n--- SECURITY REPORT ---")
    if score == 3:
        print("STATUS: SECURE (Low Risk)")
    elif score == 2:
        print("STATUS: VULNERABLE (Medium Risk)")
    else:
        print("STATUS: CRITICAL (High Risk Level)")
        
    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print(f"- {item}")


user_input = input("Enter a password to test security: ")
analyze_password(user_input)