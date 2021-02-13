from flask import Flask,render_template

app = Flask(__name__)

allposts = [
    {
        'title':'iPhone 13 is not coming out',
        'content':'Apple officialy says iPhone 13 is replaced by iPhone Tera'
    },
    {
        'title':'Apple Car is out',
        'content':'Apple releases its first electric car starting form $50,000 USD'
    },

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=allposts)

@app.route('/home/<string:name>')
def home(name):
    return "Hello " + str(name)




if __name__ == '__main__':
    app.run(debug=True)