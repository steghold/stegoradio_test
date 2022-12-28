from flask import Flask
import time

app = Flask(__name__)


@app.route('/api/current_metadata')
def current():
    current_timestamp = int(time.time()) - 20000

    data = {
        'name': 'Master of Puppets',
        'artist': 'Metallica',
        'start_timestamp': current_timestamp,
        'artwork_URL': 'https://upload.wikimedia.org/wikipedia/en/b/b2/Metallica_-_Master_of_Puppets_cover.jpg'
    }

    return data, 200


@app.route('/api/current_data')
def stream_opus():
    chunk_size = 64

    def generate():
        with open('out.m4a', 'rb') as f:
            while True:
                b = f.read(chunk_size)
                if b:
                    yield b
                else:
                    break

    return app.response_class(generate(), mimetype='audio/mp4')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
