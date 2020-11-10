# Server setup
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Routes

# R001
@app.route('/')
def go_home():
    return render_template('home.html')

@app.route('/newSubscriber', methods=['POST'])
def new_subscriber():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    radio = request.form['radio']
    return redirect('/')

# R002
@app.route('/aboutus')
def go_aboutus():
    return render_template('aboutus.html')

# R003
@app.route('/updates')
def go_updates():
    return render_template('updates.html')

#  Server setup 
if __name__=="__main__":    
    app.run(host="localhost", port=5000, debug=True)
