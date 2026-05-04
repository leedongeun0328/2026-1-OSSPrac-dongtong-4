from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    names = request.form.getlist('name[]')
    student_numbers = request.form.getlist('StudentNumber[]')

    return render_template('result.html', students=zip(names, student_numbers))

@app.route('/contact')
def contact_info():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)