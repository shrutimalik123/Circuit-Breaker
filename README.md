# ⚡ Circuit Breaker - Memory Sequence Sim

A high-stakes memory challenge where you play as a technician attempting to override a failing power grid. The system transmits a sequence of numeric signals that you must memorize and repeat perfectly. With every successful override, the sequence grows longer, testing the limits of your short-term memory and focus.

This project focuses on teaching:
* **Output Pacing:** Using `time.sleep()` to control the rate of information delivery.
* **Stream Control:** Utilizing `flush=True` to ensure real-time terminal updates.
* **Buffer Comparison:** Iterating through a generated list to validate user input against a "Master Sequence."
* **Terminal Management:** Using whitespace manipulation to clear the game state and hide data from the player.

---

## ✨ Features

* **Dynamic Difficulty:** The sequence length increases infinitely until the player makes a mistake.
* **Timed Exposure:** Signals are displayed for less than a second each, forcing rapid memorization.
* **Input Validation:** Built-in error handling to prevent the system from crashing on non-numeric inputs.
* **Clear Screen Logic:** A "Low-Tech" buffer clear that hides the sequence before the player begins their attempt.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `circuit_breaker.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python circuit_breaker.py
    ```

### 3. Gameplay Instructions
1.  **Watch the Screen:** Numbers will appear one by one. Do not type yet!
2.  **Memorize:** Note the order of the signals (1-9).
3.  **Override:** Once the screen clears, type each number in the exact order it appeared, hitting **Enter** after each one.
4.  **Advance:** Successfully complete the sequence to move to the next level.



---

## 🧠 Code Structure Highlights

### Real-Time Signal Streaming
To make the numbers appear one by one on the same line, we use `end=""`. This tells Python not to start a new line, while `flush=True` forces the terminal to show the number immediately rather than waiting for the loop to end.

```python
for signal in sequence:
    print(f" > {signal}", end="", flush=True)
    time.sleep(0.8) # Controls the "beat" of the game
