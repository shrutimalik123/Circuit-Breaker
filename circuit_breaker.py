import random
import time
import os

def circuit_breaker():
    # 1. Game Setup
    sequence = []
    level = 1
    alive = True

    print("--- ⚡ CIRCUIT BREAKER ⚡ ---")
    print("Memorize the sequence to override the system.")
    time.sleep(2)

    # 2. Game Loop
    while alive:
        # Add a new random signal to the sequence
        sequence.append(random.randint(1, 9))
        
        # Display the sequence to the player
        print(f"\n🚀 LEVEL {level} - INCOMING SIGNAL:")
        time.sleep(1)
        
        for signal in sequence:
            print(f" > {signal}", end="", flush=True)
            time.sleep(0.8) # Wait 0.8s between numbers
        
        # Clear the screen (standard for Windows/Mac/Linux)
        # Note: In some terminals, this just prints many empty lines
        print("\n" * 50)
        
        # 3. Input Buffer Logic
        print("--- OVERRIDE INITIATED ---")
        for i in range(len(sequence)):
            try:
                user_input = int(input(f"Signal {i+1}/{len(sequence)}: "))
                if user_input != sequence[i]:
                    print(f"\n❌ ACCESS DENIED! Signal mismatch.")
                    alive = False
                    break
            except ValueError:
                print("\n❌ SYSTEM ERROR: Non-numeric signal detected.")
                alive = False
                break
        
        if alive:
            print("✅ CIRCUIT OVERRIDDEN! Preparing next level...")
            level += 1
            time.sleep(1.5)

    # 4. Final Result
    print(f"\n🏁 SYSTEM SHUTDOWN | Final Level: {level}")
    print(f"The correct sequence was: {sequence}")

circuit_breaker()
