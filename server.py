# Server setup
from flask import Flask, render_template
app = Flask(__name__)

# Routes

# R001
@app.route('/')
def go_home():
    return render_template('home.html')

#  Server setup 
if __name__=="__main__":    
    app.run(debug=True)
