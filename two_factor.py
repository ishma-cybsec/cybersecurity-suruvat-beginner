# otp_local.py
# Simple local OTP generator & verifier (works in Python 3.x)
# - Generates a 6-digit OTP (preserves leading zeros)
# - Expires after expiry_seconds
# - Allows max_attempts tries
# Author: ishma-cybsec

import secrets
import time

OTP_LENGTH = 6
EXPIRY_SECONDS = 30    # how long OTP is valid
MAX_ATTEMPTS = 3       # allowed attempts before denial

def generate_otp(length=OTP_LENGTH):
    """Generate a secure numeric OTP as a zero-padded string."""
    # secrets.randbelow(10**length) returns an int in [0, 10^length - 1]
    return f"{secrets.randbelow(10**length):0{length}d}"

def main():
    print("=== Local OTP Generator / Verifier ===")
    otp = generate_otp()
    created_at = time.time()
    print(f"\nGenerated OTP (valid for {EXPIRY_SECONDS} seconds): {otp}")
    # Note: in a real system you would send this by email/SMS; here we display it.

    attempts_left = MAX_ATTEMPTS
    while attempts_left > 0:
        user_input = input("\nEnter the 6-digit OTP: ").strip()

        # Check expiry first
        if time.time() - created_at > EXPIRY_SECONDS:
            print("❌ OTP expired. Access denied.")
            return

        # Preserve leading zeros by comparing strings
        if user_input == otp:
            print("✅ Access granted.")
            return
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"❌ Incorrect OTP. Attempts left: {attempts_left}")
            else:
                print("❌ Incorrect OTP. No attempts left. Access denied.")
                return

if __name__ == "__main__":
    main()


