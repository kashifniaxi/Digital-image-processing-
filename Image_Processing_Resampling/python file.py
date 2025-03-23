import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1. Using Python, create grayscale image of resolution 400 x 400 pixels such that all even number
# columns are black (0), and all odd columns are white (255). 
img1 = []
for i in range(400):
    temp = []
    for j in range(400):
        if j%2==0:
            temp.append(0)
        else:
            temp.append(255)
    img1.append(temp)

img = np.array(img1)
if img.dtype != np.uint8:
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
cv2.imwrite('color_img.jpg', img)
cv2.imshow("image", img)
cv2.waitKey()
# 2. Resize this image to 200x200, and comment on the output. What do you observe?
downsampled_img = cv2.resize(img, (200, 200))

# Display the downsampled image
cv2.imshow("Downsampled Image", downsampled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# 3. Design your own algorithm and resize again such that the image details are retained in the
# output image.
def downsample(img):
    for i in range(len(img)):
        temp = img[i]
        j = 0 
        k = 0
        while k <len(temp)-1:
            if j %2==0:
                img[i][j] = max(img[i][k],img[i][k+1])
            else:
                img[i][j] = min(img[i][k],img[i][k+1])
            k+=2
    # img = np.array(img)
    img = img[::2, :200]
    img = np.array(img)
    if img.dtype != np.uint8:
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    cv2.imwrite('color_img.jpg', img)
    cv2.imshow("image", img)
    cv2.waitKey()

downsample(img.copy())



# 4. Create a new image of size 400x400, but this time first 2 columns are black, then two columns
# are white, and this pattern continues. 
img1 = []
for i in range(400):
    temp = []
    for j in range(200):
        if j%2==0:
            temp.append(0)
            temp.append(0)
        else:
            temp.append(255)
            temp.append(255)
    img1.append(temp)
img = np.array(img1, dtype=np.uint8)  # Specify the dtype here

# Check if the dtype is correct
if img.dtype != np.uint8:
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Save the image with a valid file extension
cv2.imwrite('2black2whitepixelImage.png', img) 
cv2.imshow("image", img)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows() 
# 5. Will the algorithm you designed in part 3 work with this new image? If not, how can you improve
# it so that it works for both images.

downsample(img.copy())

#builtin resize to comapre with part 5 resized image
downsampled_img = cv2.resize(img, (200, 200), interpolation=cv2.INTER_AREA)

# Display the downsampled image
cv2.imshow("Downsampled Image", downsampled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import numpy as np
# 6. Interpolate the image created in part 1, by a factor of 2, and by a factor of 3, using the built-in
# functions with bilinear. Quadratic, and cubic parameters, and then compare and discuss the
# results
# Interpolation factors
factor_2 = (img.shape[1] * 2, img.shape[0] * 2)  # 2x size (width, height)
factor_3 = (img.shape[1] * 3, img.shape[0] * 3)  # 3x size (width, height)

# Bilinear Interpolation
bilinear_2x = cv2.resize(img, factor_2, interpolation=cv2.INTER_LINEAR)
bilinear_3x = cv2.resize(img, factor_3, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('bilinear2xbuilt_in.png', bilinear_2x)
# Display the image
cv2.imshow("Bilinear 2x Image", bilinear_2x)
cv2.waitKey(0)

# Cubic Interpolation (Quadratic is generally part of cubic interpolation in OpenCV)
cubic_2x = cv2.resize(img, factor_2, interpolation=cv2.INTER_CUBIC)
cubic_3x = cv2.resize(img, factor_3, interpolation=cv2.INTER_CUBIC)

# Plot and compare results for 2x and 3x factors
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.imshow(bilinear_2x, cmap='gray')
plt.title('Bilinear 2x')

plt.subplot(2, 3, 2)
plt.imshow(cubic_2x, cmap='gray')
plt.title('Cubic 2x')

plt.subplot(2, 3, 3)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(2, 3, 4)
plt.imshow(bilinear_3x, cmap='gray')
plt.title('Bilinear 3x')

plt.subplot(2, 3, 5)
plt.imshow(cubic_3x, cmap='gray')
plt.title('Cubic 3x')

plt.tight_layout()
plt.show()
# 7. Now Implement your own bilinear interpolation function and resize the same input image by a
# factor of 2 and 3.

def interpolateby2(img):
    target_length = 800 
    
    i = 0
    while i < len(img) - 1:
        temp2 = []
        for j in range(len(img[i])):
            temp2.append((img[i][j] + img[i+1][j]) / 2)
        img.insert(i+1, temp2)
        i += 2
    img.append(img[-1].copy()) 
        
    for i in range(len(img)):
        j = 0
        temp = img[i].copy()
        while j < len(temp):
            if j < len(temp) - 1:
                temp.insert(j+1,(temp[j] + temp[j + 1]) / 2)
                j += 2
            else:
                temp.append(temp[j])
                break
        if len(temp) != target_length:
            temp = temp[:target_length]  
            print('----')
        img[i] = temp.copy()
    img = np.array(img)
    print("Final shape:", img.shape)
    if img.dtype != np.uint8:
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    cv2.imwrite('bilinear2xAlgo.jpg', img)
    cv2.imshow("image", img)
    cv2.waitKey()
    return img
        
mybilinear = interpolateby2(img1.copy())


def interpolateby3(img):
    target_size = 1200  # Target size for the final image
    print('start')
    # First interpolation step (row-wise)
    i = 0
    while i < len(img)-1:
        temp2 = []
        temp3 = []
        for j in range(len(img[i])):
            temp_val =(img[i][j] + img[i + 1][j]) / 2
            temp2.append(temp_val)
            temp3.append(((temp_val+ img[i + 1][j]) / 2))
        img.insert(i + 1, temp2)  
        img.insert(i +2, temp3) # Insert the interpolated row
        i += 3 # Move one step forward (increment by 1)

    img.append(img[-1].copy())
    img.append(img[-1].copy())  
    new_height = len(img)
    print(f"Height after row interpolation: {new_height}")
    
    for i in range(len(img)):
        temp = img[i].copy()
        temp2 = img[i].copy()
        j = 0
        while j < len(temp):
            if j < len(temp) - 1:

                temp_val = (temp[j] + temp[j + 1]) / 2
                temp.insert(j + 1,temp_val )
                temp.insert(j + 1, (temp_val+ temp[j + 1]) / 2)
                j += 3  
            else:
                temp.append(temp[j])
                temp.append(temp[j])
                break
        if len(temp) > target_size:
            temp = temp[:target_size] 
        elif len(temp) < target_size:
            temp.extend([temp[-1]] * (target_size - len(temp)))  
        
        img[i] = temp.copy()
    img = np.array(img)
    print("Final shape:", img.shape)
    # Normalize and ensure it's uint8 type for saving
    if img.dtype != np.uint8:
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Save and display the image
    cv2.imwrite('bilinear3xAlgo.png', img)  
    cv2.imshow("Interpolated Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
        
mytrilinear = interpolateby3(img1.copy())

#8. Calculate the difference between your output and the bilinear output of the built-in function. Do
# you get a completely zero difference output?

difference_2x = cv2.absdiff(bilinear_2x, mybilinear)
difference_3x = cv2.absdiff(bilinear_3x, mytrilinear)

# Create subplots for comparison
fig, axs = plt.subplots(2, 4, figsize=(16, 12))

# Plotting the images
axs[0, 0].imshow(img1, cmap='gray')
axs[0, 0].set_title('Original Image (400x400)')
axs[0, 0].axis('off')

axs[0, 1].imshow(mybilinear, cmap='gray')
axs[0, 1].set_title('Custom Bilinear (800x800)')
axs[0, 1].axis('off')

axs[0, 2].imshow(bilinear_2x, cmap='gray')
axs[0, 2].set_title('OpenCV Bilinear (800x800)')
axs[0, 2].axis('off')


axs[1, 0].imshow(img1, cmap='gray')
axs[1, 0].set_title('Original Image (400x400)')
axs[1, 0].axis('off')

axs[1, 1].imshow(mytrilinear, cmap='gray')
axs[1, 1].set_title('Custom Trilinear (1200x1200)')
axs[1, 1].axis('off')

axs[1, 2].imshow(bilinear_3x, cmap='gray')
axs[1, 2].set_title('OpenCV Bilinear (1200x1200)')
axs[1, 2].axis('off')


# Adjust layout
plt.tight_layout()
plt.show()