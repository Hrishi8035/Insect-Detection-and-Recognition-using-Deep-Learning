from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_detection')
def detect_objects_route():
    process = subprocess.Popen(["python", "detect.py", "--weights", "insect.pt", "--img", "640", "--conf", "0.45", "--source", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        return jsonify({'error': 'Failed to start detection process', 'stderr': stderr.decode()})
    return jsonify({'message': 'Detection started successfully!', 'stdout': stdout.decode()})

if __name__ == "__main__":
    app.run(debug=True)
