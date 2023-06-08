import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


### function to generate key using a chaotic map for an eccryption process

def keygen(x, r, size):
    key =[]
    for i in range(size):
       x = r*x*(1-x)
       key.append(int(x*pow(10, 16)%256))

    return key
 
#print(keygen(0.01, 3.915, 10))


# reading the image
img = mpimg.imread('test1_cryptography.jpg')

plt.imshow(img)
plt.show()

# generate chaotic key
height = img.shape[0]
width = img.shape[1]
key = keygen(0.01, 3.95, height * width)  
#print(key)

# Encryption-diffusion with XOR
z = 0
enimg = np.zeros(shape=[height, width, 3], dtype=np.uint8)  
for i in range(height):
    for j in range(width):
        # pixel value is XORed with key
        enimg[i, j] = img[i, j] ^ key[z] #error
        z = z + 1

plt.imshow(enimg)
plt.show()
plt.imsave("encrypted.jpg", enimg)

# Decryption
z = 0
decimg = np.zeros(shape=[height, width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        # pixel value is XORed with key
        decimg[i, j] = enimg[i, j] ^ key[z]
        z += 1

plt.imshow(decimg)
plt.imsave("decrypted.jpg", decimg)
