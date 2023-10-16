import cv2
import numpy as np

  
# Function to generate a random RGB color
def random_color():
  """
  Generates a random values color tuple.
  input : none.
  output : tuple representing a color .
  
  """
  return tuple(torch.randint(0,256,size=(3,),dtype=torch.uint8).tolist())
    
def opencv_generation(num_images, img_size, shapes):
    """
    Generate images of random shapes using OpenCV and save them to the file system.

    Inputs:
    - num_images (int): The number of images to generate.
    - img_size (int): The size (width and height) of the images in pixels.
    - shapes (list): A list of shape names to choose from (e.g., ['circle', 'rectangle', 'triangle']).

    Outputs:
    None
    """

    # Loop through and generate images
    for i in range(num_images):
        # Create a new blank image
        img = np.zeros((img_size, img_size, 3), dtype=np.uint8)

        # Select a random shape and color
        shape = np.random.choice(shapes)
        color = random_color()  # Assumes a function random_color() generates random colors

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

        # Save the generated image to the file system
        cv2.imwrite(f'OPENCV_generated_shapes/{shape}/{i}.jpg', img)
