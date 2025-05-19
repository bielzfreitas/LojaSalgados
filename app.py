from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/salgados', methods=['GET'])
def get_salgados():
    salgados = [
        {'id': 1, 'name': 'Coxinha', 'price': 5.00},
        {'id': 2, 'name': 'Pão de Queijo', 'price': 3.00},
        {'id': 3, 'name': 'Kibe', 'price': 4.00},
        {'id': 4, 'name': 'Empada', 'price': 6.00}
    ]
    return jsonify(salgados)

if __name__ == '__main__':
    app.run(debug=True)