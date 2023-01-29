from flask import Flask, render_template, redirect, request, session 
app=Flask(__name__)
app.secret_key="mysecretkeyfordojosurvey"

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/new_user', methods=['POST'])
def new_user():
    print('Got Post Info')
    print(request.form) 
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
    print ('Showing the User Info From the Form')
    print (request.form)
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)