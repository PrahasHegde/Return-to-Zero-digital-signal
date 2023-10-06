import numpy as np
import matplotlib.pyplot as plt

# Get user input for the binary sequence (0s and 1s)
binary_sequence = input("Enter a binary sequence (e.g., 010101): ")

# Define signal parameters
bit_duration = 1.0  # Duration of each bit in seconds
bit_rate = 1 / bit_duration  # Bit rate in bits per second

# Create a time array for the signal
t = np.linspace(0, len(binary_sequence) * bit_duration, len(binary_sequence) * 1000)

# Initialize an empty signal
signal = np.zeros_like(t)

# Create the RZ signal based on the binary input
for i, bit in enumerate(binary_sequence):
    bit_start = i * bit_duration
    bit_middle = bit_start + bit_duration / 2

    if bit == '1':
        # Set the signal to a positive pulse for '1'
        signal[(t >= bit_start) & (t <= bit_middle)] = 1
    elif bit == '0':
        # Set the signal to zero for '0'
        signal[(t >= bit_start) & (t <= bit_middle)] = 0

# Plot the RZ signal
plt.plot(t, signal)
plt.title("Return to Zero (RZ) Digital Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
# plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.show()
