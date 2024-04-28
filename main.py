#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/', methods=['POST'])
def process_form2():
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_discord=button_discord)

@app.route('/', methods=['POST'])
def process_form3():
    button_html = request.form.get('button_html')
    return render_template('index.html', button_html=button_html)

@app.route('/', methods=['POST'])
def process_form4():
    button_db = request.form.get('button_db')
    return render_template('https://github.com/rfgfgfgfgf/diary-project.git', button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)
