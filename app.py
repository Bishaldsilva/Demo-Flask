from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        # Get input numbers from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
    except ValueError:
        result = "Invalid input. Please enter valid numbers."
    
    # Display the result on the same page
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
