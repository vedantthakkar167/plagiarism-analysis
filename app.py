from flask import Flask, render_template, request
from plagiarism_checker import plagiarism_checker
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check', methods=['POST'])
def check_plagiarism():
    text_to_check = request.form['text_to_check']

    result=plagiarism_checker(text_to_check)
        
    return render_template('index.html', plagiarism_results=result)


if __name__ == '__main__':
    app.run(debug=True)
