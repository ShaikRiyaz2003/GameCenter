from flask import Flask, jsonify, render_template

app = Flask(__name__,
            static_url_path='')

@app.route('/')
def index():
    games = ['simon', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman', 'tetris', 'pacman','simon', 'tetris', 'pacman','simon', 'tetris', 'pacman']
    return render_template('index.html', games=games)
    # return render_template('pages/index.html')

@app.route('/data')
def get_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)
