from flask import Flask, render_template, redirect, request, session 
app=Flask(__name__)
app.secret_key="mysecretkeyfordojosurvey"

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Here we add propertes to session to store
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    # NEVER RENDER A TEMPLATE ON A POST REQUEST..instead redirect
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)