from flask import Flask, request, jsonify
from flasgger import Swagger
import os
from youtube_upload_automation import upload_video_api

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/upload', methods=['POST'])
def upload():
    """
    Upload a video to YouTube and schedule it
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The video file to upload
      - name: title
        in: formData
        type: string
        required: true
        description: Video title
      - name: description
        in: formData
        type: string
        required: true
        description: Video description
      - name: tags
        in: formData
        type: string
        required: false
        description: Tags separated by "|"
      - name: scheduled_time
        in: formData
        type: string
        required: true
        description: Time to publish (e.g., 2025-07-14 21:00:00)
    responses:
      200:
        description: Upload successful
    """
    file = request.files['file']
    title = request.form['title']
    description = request.form['description']
    tags = request.form.get('tags', '').split('|')
    scheduled_time = request.form['scheduled_time']

    temp_path = f"temp_{file.filename}"
    file.save(temp_path)

    try:
        video_id = upload_video_api(temp_path, title, description, tags, scheduled_time)
        os.remove(temp_path)
        return jsonify({"status": "success", "video_id": video_id})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
