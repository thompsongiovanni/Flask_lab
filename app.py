from flask import Flask, render_template
app = Flask(__name__)             

@app.route("/")                   
def hello():                      
    return render_template("index.html")     

@app.route("/about")
def about():
    name = request.arg.get('name')
    return render_template("about.html", aboutName = name)    

@app.route("/<name>")              
def hello_name(name):              
    return "Hello " + name   

if __name__ == "__main__":        
    app.run(debug=True)                            