import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(2)


print("Capturing background... Please stay out of the frame.")
for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)
print("Background captured!")

selected_hsv = None
drawing = False
manual_mask = None
points = []

def handle_mouse(event, x, y, flags, param):
    global drawing, points, manual_mask, selected_hsv

    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            # Ctrl+Click → Select color
            pixel = frame[y, x]
            hsv_pixel = cv2.cvtColor(np.uint8([[pixel]]), cv2.COLOR_BGR2HSV)[0][0]
            selected_hsv = hsv_pixel
            print(f"[Color Picked] HSV: {selected_hsv}")
        else:
            # Normal click → Draw
            drawing = True
            points = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        points.append((x, y))
        cv2.line(manual_mask, points[-2], points[-1], 255, 5)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points.append((x, y))
        cv2.line(manual_mask, points[-2], points[-1], 255, 5)

cv2.namedWindow("Invisibility Cloak")
cv2.setMouseCallback("Invisibility Cloak", handle_mouse)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if manual_mask is None:
        manual_mask = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)

    color_mask = np.zeros_like(manual_mask)

    
    if selected_hsv is not None:
        h, s, v = map(int, selected_hsv)
        sensitivity = 20

        lower = np.array([max(0, h - sensitivity), max(50, s - 50), max(50, v - 50)], dtype=np.uint8)
        upper = np.array([min(179, h + sensitivity), min(255, s + 50), min(255, v + 50)], dtype=np.uint8)

        color_mask = cv2.inRange(hsv, lower, upper)
        color_mask = cv2.GaussianBlur(color_mask, (5, 5), 0)
        color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)
        color_mask = cv2.dilate(color_mask, np.ones((3, 3), np.uint8), iterations=1)

    # Combine both masks
    combined_mask = cv2.bitwise_or(manual_mask, color_mask)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8), iterations=1)

    inverse_mask = cv2.bitwise_not(combined_mask)

    cloak_area = cv2.bitwise_and(background, background, mask=combined_mask)
    normal_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    final_output = cv2.addWeighted(cloak_area, 1, normal_area, 1, 0)

    
    cv2.putText(final_output, "CTRL+Click = Pick Color | Draw = Manual | 'c'=Clear | 'q'=Quit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Invisibility Cloak", final_output)

     key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        manual_mask = np.zeros_like(manual_mask)
        print("[Cleared] Manual drawing mask")

cap.release()
cv2.destroyAllWindows()

   
