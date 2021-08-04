from flask import Flask, render_template

app = Flask(__name__)

    
@app.route('/')
def index():
    name = 'Ankit'
    title = 'Week6 Day1 Homework'
    return render_template('index.html', my_name=name, title=title)

@app.route('/list')
def list():
    Car_list = ['BMW M4', 'Ferrari 458 Speciale A','Pagani Zonda', 'Lamborghini Diablo', 'Ferrari 488 Pista']
    return render_template('list.html', title='list', Car_list=Car_list)

print(app)