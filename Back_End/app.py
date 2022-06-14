from flask import Flask, render_template, request

# For getting image data
# import pickle
# import numpy as np 

# load model.py
# model = pickle.load(open('filename.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def Landing():
    return render_template('Landing.html')


# get image data
@app.route('/upload', methods = ['POST'])
def Upload():
    pass

# show image using model
@app.route('/items', methods = ['POST'])
def Items():
    pass

# show image using model
@app.route('/register', methods = ['POST'])
def Register():
    pass

# show image using model
@app.route('/login', methods = ['POST'])
def Login():
    pass

# show image using model
@app.route('/closet', methods = ['POST'])
def Closet():
    pass



if __name__ == "__main__" :
    app.run()
