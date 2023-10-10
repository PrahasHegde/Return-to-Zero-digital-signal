import matplotlib.pyplot as plt

def encode(data):
    encoded_data = []
    if data[0] == '0':
        encoded_data.append(-1)
    else:
        encoded_data.append(1)
    for i in data:
        if i == '0':
            encoded_data.append(-1)
            encoded_data.append(0)
        elif i == '1':
            encoded_data.append(1)
            encoded_data.append(0)
        else:
            print('invalid input')
    return encoded_data


data = input('enter the data: ')

y = encode(data=data)

x = [i for i in range(len(y))]
plt.step(x ,y)
plt.xlabel('time')
plt.ylabel('voltage')
plt.title('RZ encoding')
print(y)
print(x)
plt.show()
