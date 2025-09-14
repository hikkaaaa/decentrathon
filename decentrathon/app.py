#application itself - Flask object
from flask import Flask, render_template, request
#Flask - for API deployment (and for running a server on local machine)
#render_template - to render a frontend (to link frontend with this back )

app = Flask(__name__) #create a Flask app

@app.route('/', methods = ['GET']) #'/' means a typical URL
def hello_word():
    return render_template('index.html')
#you dont have to say ./templates/index.html because:
#By default, Flask is configured to look for templates 
#in a folder called templates/, 
# which must be in the same directory as your app.py file


#1. get the image
#2. save it into a folder
#3. do all the preprocessing
@app.route('/', methods = ['POST'])
def predict(): 
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename #will return the name of the file that user uploads
    imagefile.save(image_path)

    return render_template("result.html")

if __name__ == '__main__': 
    app.run(port = 8000, debug = True) #run the server 