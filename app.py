from flask import Flask, render_template
import cleaning

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def testing_function():
    print("Estamos testeando 1,2,3")

if __name__ == "__main__":
    app.run()
