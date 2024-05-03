# from flask import Flask, render_template, request
# import easyocr

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/upload', methods=['POST'])
# def upload():
#     # Check if a file was uploaded
#     if 'file' not in request.files:
#         return render_template('index.html', error='No file uploaded')

#     file = request.files['file']

#     # Perform OCR on the uploaded image
#     reader = easyocr.Reader(['kn'])
#     result = reader.readtext(file.stream)

#     # Extract Kannada text from the OCR result
#     kannada_text = ' '.join([entry[1] for entry in result])

#     return render_template('index.html', kannada_text=kannada_text)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import os
import easyocr

from speech_to_txt import get_large_audio_transcription_fixed_interval

app = Flask(__name__,static_url_path='/static')

# Configure EasyOCR reader for English
reader = easyocr.Reader(['en'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image_upload', methods=['POST'])
def image_upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file:
        # Save the uploaded image
        image_path = os.path.join('uploads', file.filename)
        file.save(image_path)

        reader = easyocr.Reader(['kn'])
        result = reader.readtext(image_path)

        # Extract Kannada text from the OCR result
        extracted_text = ' '.join([entry[1] for entry in result])

        # # Perform OCR on the uploaded image
        # result = reader.readtext(image_path)

        # # Extract text from the OCR result
        # extracted_text = ' '.join([entry[1] for entry in result])

        return render_template('index.html', message='Text extracted:', extracted_text=extracted_text)
    
@app.route('/voice_upload', methods=['POST'])
def voice_upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file:
        # Save the uploaded image
        voice_path = os.path.join('uploads', file.filename)
        file.save(voice_path)
        result=get_large_audio_transcription_fixed_interval(voice_path, minutes=1/6)

        # Extract Kannada text from the OCR result
        extracted_text = result

        # # Perform OCR on the uploaded image
        # result = reader.readtext(image_path)

        # # Extract text from the OCR result
        # extracted_text = ' '.join([entry[1] for entry in result])

        return render_template('index.html', message='Text extracted:', extracted_text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
