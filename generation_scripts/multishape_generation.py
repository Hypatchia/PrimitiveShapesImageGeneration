from PIL import Image, ImageDraw
import os

def MultishapeGeneration(dataset_size, save_dir, image_size):
    """
    Generate a dataset of images containing multiple shapes and save them to the specified directory.

    Inputs:
    - dataset_size (int): The number of images to generate.
    - save_dir (str): The directory where the generated images will be saved.
    - image_size (tuple): A tuple specifying the dimensions (width, height) of the generated images.

    Outputs:
    None
    """
    # Generate and save images
    for i in range(dataset_size):
        # Create a black image with a white background
        image = Image.new("RGB", image_size, (255, 255, 255))

        # Generate rectangles
        for _ in range(5):
            pt1, pt2, color = generate_rectangle(image_size)
            draw = ImageDraw.Draw(image)
            draw.rectangle((pt1, pt2), fill=color)

        # Generate triangles
        for _ in range(5):
            pt1, pt2, pt3, color = generate_triangle(image_size)
            draw = ImageDraw.Draw(image)
            draw.polygon((pt1, pt2, pt3), fill=color)

        # Generate ellipses
        for _ in range(5):
            center, axes, angle, color = generate_ellipse(image_size)
            draw = ImageDraw.Draw(image)
            draw.ellipse(((center[0] - axes[0], center[1] - axes[1]), (center[0] + axes[0], center[1] + axes[1]),
                        fill=color, outline=color)

        # Save the generated image
        image_filename = os.path.join(save_dir, f"shape_{i + 1}.png")
        image.save(image_filename)

    print(f"Generated images saved to directory: {save_dir}")
