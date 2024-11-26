from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    command = data.get('command', '')
    try:
        # Run the command using subprocess
        result = subprocess.check_output(['python', '-c', command], stderr=subprocess.STDOUT, text=True)
        return jsonify({'result': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output})

if __name__ == '__main__':
    app.run(debug=True)