#RZ waveform

#Return-to-zero (RZ or RTZ) describes a line code used in telecommunications signals in which the signal drops (returns) to zero between each pulse.
# This takes place even if a number of consecutive 0s or 1s occur in the signal

import numpy as np
import matplotlib.pyplot as plt

# user_input  = input("Enter your array: ") #input array
# data = list(user_input)


def generateRZ(data):
    rz_code = []
    for bit in data:
        if bit == 1 :
            rz_code.extend([1,0])
        else:
            rz_code.extend([-1,0,0])
            
    return rz_code



    


 #main
data = [1,0,1,1,0,1]




rz_signal = generateRZ(data)

t= np.linspace(0,len(data)-1,len(rz_signal))

#PLOT
print(len(data))
print(len(rz_signal))
print(len(t))
print((data))
print((rz_signal))
print((t))

plt.step(t, rz_signal, where='post')

# plt.plot=(t,rz_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('RZ wave') 
# plt.ylim(-0.5,1.5)


plt.grid(True)
plt.show()