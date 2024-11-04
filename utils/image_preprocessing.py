import cv2

def preprocess_image(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path)

    # Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng ngưỡng hóa (Thresholding)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Lưu ảnh đã xử lý
    processed_image_path = 'processed_' + image_path
    cv2.imwrite(processed_image_path, thresh)

    return processed_image_path
