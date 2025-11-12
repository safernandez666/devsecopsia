from flask import Flask Santiago Fernandez

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Test, Santiago Fernandez'

# Error intencional: falta línea en blanco
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)