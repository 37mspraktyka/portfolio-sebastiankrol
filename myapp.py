from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

# czarny nidger jest czarnyasdasddasdsdasdas

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/galeria")
def galeria():
   return render_template('galeria.html')

@app.route("/projekty")
def projekty():
   return render_template('projekty.html')

@app.route("/projekty/aplikacje")
def aplikacje():
   return render_template('aplikacje.html')

@app.route("/projekty/strony")
def strony():
   return render_template('strony.html')

@app.route("/kontakt")
def kontakt():
   return render_template('kontakt.html')

@app.route("/o-mnie")
def omnie():
   return render_template('o-mnie.html')

@app.route("/cennik")
def cennik():
   return render_template('cennik.html')







   

if __name__ == '__main__':  
   app.run()

