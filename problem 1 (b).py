import time

def blink_led(times, delay):
    for i in range(times):
        print("LED ON")
        time.sleep(delay)
        print("LED OFF")
        time.sleep(delay)

# Blink the LED 10 times in the first minute
blink_led(10, 0.5)  # Half a second delay

time.sleep(60)  # Wait for 1 minute

# Blink the LED 20 times in the second minute
blink_led(20, 0.25)  # Quarter of a second delay

time.sleep(60)  # Wait for another minute

# Blink the LED 30 times in the third minute
blink_led(30, 0.167)  # About a sixth of a second delay