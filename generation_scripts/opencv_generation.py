import cv2
import numpy as np
import torch

# Function to generate a random RGB color
def random_color():
    """
    Generates a random RGB color tuple.

    Outputs:
        tuple: A tuple representing an RGB color, e.g., (R, G, B).
    """
    return tuple(torch.randint(0, 256, size=(3,), dtype=torch.uint8).tolist())

# Function to generate images using OpenCV
def opencv_generation(num_images, img_size, shapes):
    """
    Generates and saves images with random primitive shapes.

    Inputs:
        num_images (int): The number of images to generate.
        img_size (int): The size of the square image (width and height).
        shapes (list): A list of shape names to choose from (e.g., 'circle', 'rectangle', 'triangle').

    Outputs:
        None
    """
    # Loop through and generate images
    for i in range(num_images):
        # Create a new blank image
        img = np.zeros((img_size, img_size, 3), dtype=np.uint8)

        # Select a random shape and color
        shape = np.random.choice(shapes)
        color = random_color()

        # Draw the selected shape on the image
        if shape == 'circle':
            center = (img_size // 2, img_size // 2)
            radius = np.random.randint(50, 100)
            cv2.circle(img, center, radius, color, -1)
        elif shape == 'rectangle':
            pt1 = (np.random.randint(0, img_size // 2), np.random.randint(0, img_size // 2))
            pt2 = (np.random.randint(img_size // 2, img_size), np.random.randint(img_size // 2, img_size))
            cv2.rectangle(img, pt1, pt2, color, -1)
        elif shape == 'triangle':
            pt1 = (np.random.randint(0, img_size), np.random.randint(0, img_size // 2))
            pt2 = (np.random.randint(0, img_size // 2), np.random.randint(img_size // 2, img_size))
            pt3 = (np.random.randint(img_size // 2, img_size), np.random.randint(img_size // 2, img_size))
            pts = np.array([pt1, pt2, pt3], np.int32)
            cv2.fillPoly(img, [pts], color)

        # Save the generated image
        cv2.imwrite(f'OPENCV_primitive_shapes/{shape}/{i}.jpg', img)
