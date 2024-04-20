from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:

        # Получаем изображение в формате base64 из запроса
        image_base64 = request.json.get('image_base64')

        # Декодируем base64 в бинарные данные изображения
        image_data = base64.b64decode(image_base64)

        # Создаем объект изображения из бинарных данных
        image = Image.open(BytesIO(image_data))

        # Делаем что-то с изображением (например, сохраняем его или обрабатываем)
        image.save('uploaded_image2.png')  # Сохраняем изображение в файл

        # Возвращаем успешный ответ
        return jsonify({'message': 'Image received and saved successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
