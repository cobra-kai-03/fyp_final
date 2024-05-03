# import cv2
# import easyocr
# import matplotlib.pyplot as plt
# import numpy as np

# # read image
# image_path = 'test6.png'

# img = cv2.imread(image_path)

# # instance text detector
# reader = easyocr.Reader(['kn'], gpu=False)

# # detect text on image
# text_ = reader.readtext(img)

# threshold = 0.25
# # draw bbox and text
# for t_, t in enumerate(text_):
#     print('text:',t)

#     bbox, text, score = t

#     if score > threshold:
#         cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
#         cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

import easyocr
# Initialize the OCR reader with the language parameter set to 'kn' for Kannada
reader = easyocr.Reader(['kn'])

# Load the Kannada image
image_path = 'test2.jpg'

# Perform OCR on the image
result = reader.readtext(image_path)

# Extract text from the OCR result
kannada_text = ' '.join([entry[1] for entry in result])

# Print the extracted Kannada text
print("Extracted Kannada Text:", kannada_text)