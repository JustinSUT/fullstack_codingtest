import cv2

def draw_bounding_boxes(image, detections):
    """
    Draws bounding boxes and overlays text on the image.

    Args:
        image (np.array): The input image.
        detections (list): List of dictionaries with label and bbox.

    Returns:
        np.array: Annotated image.
    """
    for detection in detections:
        label = detection["label"]
        bbox = detection["bbox"]  # (x1, y1, x2, y2)
        
        # Draw bounding box
        color = (0, 255, 0)  # Green color
        thickness = 2
        cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, thickness)

        # Overlay label
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        text_color = (255, 255, 255)  # White color
        text_bg_color = (0, 0, 255)  # Red color for text background
        text_size, _ = cv2.getTextSize(label, font, font_scale, 1)
        
        # Background rectangle for text
        text_x = bbox[0]
        text_y = bbox[1] - 10
        cv2.rectangle(
            image,
            (text_x, text_y - text_size[1] - 2),
            (text_x + text_size[0] + 2, text_y + 2),
            text_bg_color,
            -1
        )
        # Put text
        cv2.putText(image, label, (text_x, text_y), font, font_scale, text_color, 1)

    return image
