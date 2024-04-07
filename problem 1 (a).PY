import time
import threading

# Global variable to track the direction of LED blinking
reverse_blinking = False

def blink_led(times, delay):
    for i in range(times):
        if not reverse_blinking:
            print("LED ON")
        else:
            print("LED OFF")
        time.sleep(delay)
        if not reverse_blinking:
            print("LED OFF")
        else:
            print("LED ON")
        time.sleep(delay)

def toggle_reverse_blinking():
    global reverse_blinking
    reverse_blinking = not reverse_blinking

# Create a separate thread to handle user input for toggling
toggle_thread = threading.Thread(target=toggle_reverse_blinking)
toggle_thread.start()

# Blink the LED 30 times in the first minute
blink_led(30, 0.5)  # Half a second delay

time.sleep(60)  # Wait for 1 minute

# Blink the LED 20 times in the second minute
blink_led(20, 0.25)  # Quarter of a second delay

time.sleep(60)  # Wait for another minute

# Blink the LED 10 times in the third minute
blink_led(10, 0.167)  # About a sixth of a second delay