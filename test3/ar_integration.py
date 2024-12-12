import cv2
import numpy as np
from utils.image_utils import draw_bounding_boxes

# Path for input and output
INPUT_PATH = "assets/input_images/"
OUTPUT_PATH = "assets/output_images/"

def main():
    # Example input image and detection results
    images = ["shelf1.jpg", "shelf2.jpg"]
    detection_results = {
        "shelf1.jpg": [
            {"label": "Product A", "bbox": (50, 50, 200, 200)},
            {"label": "Product B", "bbox": (250, 100, 400, 300)},
        ],
        "shelf2.jpg": [
            {"label": "Product C", "bbox": (30, 30, 180, 180)},
            {"label": "Product D", "bbox": (200, 50, 350, 250)},
        ],
    }

    for image_name in images:
        # Load image
        image_path = INPUT_PATH + image_name
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error: Could not load image {image_name}")
            continue

        # Apply bounding boxes and text overlay
        detections = detection_results.get(image_name, [])
        annotated_image = draw_bounding_boxes(image, detections)

        # Save the output
        output_path = OUTPUT_PATH + image_name.replace(".jpg", "_output.jpg")
        cv2.imwrite(output_path, annotated_image)
        print(f"Processed {image_name} and saved to {output_path}")


if __name__ == "__main__":
    main()
