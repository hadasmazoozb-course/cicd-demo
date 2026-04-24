from flask import Flask

app = Flask(__name__)

def calculate_area(width, height):
    return width * height

@app.route('/')
def home():
    return "Python CI/CD Pipeline is Live!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
