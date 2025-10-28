# password_checker.py
# Author: ishma-cybsec

MIN_LENGTH = 8
SPECIALS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

def check_password(pw: str, min_length: int = MIN_LENGTH, specials: str = SPECIALS):
    """Return (is_valid: bool, failures: list[str], score: int)"""
    failures = []
    score = 0

    if len(pw) < min_length:
        failures.append(f"Password must be at least {min_length} characters long.")
    else:
        score += 1

    if any(c.islower() for c in pw):
        score += 1
    else:
        failures.append("Add at least one lowercase letter (a-z).")

    if any(c.isupper() for c in pw):
        score += 1
    else:
        failures.append("Add at least one uppercase letter (A-Z).")

    if any(c.isdigit() for c in pw):
        score += 1
    else:
        failures.append("Add at least one digit (0-9).")

    if any(c in specials for c in pw):
        score += 1
    else:
        failures.append("Add at least one special character (e.g. @, #, $, %).")

    if " " in pw:
        failures.append("Password must not contain spaces.")

    is_valid = len(failures) == 0
    return is_valid, failures, score


def strength_label(score: int):
    """Convert numeric score to label."""
    if score <= 2:
        return "Weak"
    elif score in (3, 4):
        return "Medium"
    else:
        return "Strong"


def main():
    print("=== Password Checker ===")
    print(f"Rules: >= {MIN_LENGTH} chars, uppercase, lowercase, digit, special char, no spaces.")
    while True:
        pw = input("\nEnter a password to check (or type 'quit' to exit): ")
        if pw.lower() == "quit":
            print("Goodbye!")
            break

        valid, failures, score = check_password(pw)
        label = strength_label(score)

        print(f"\nStrength: {label}  (score {score}/5)")
        if valid:
            print("Password meets all requirements.")
        else:
            print("Password does NOT meet the following requirements:")
            for f in failures:
                print("  -", f)

        print("\nTip: Use 3-4 random words + a digit & symbol, e.g. 'BlueRiver7!'")


if __name__ == "__main__":
    main()

