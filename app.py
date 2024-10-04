from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def homepage():
    return render_template("index.html")

@app.route('/math',methods = ['POST'])
def math_opration():
    if(request.method == 'POST'):
       ops = request.form['operation']
       num1 = int(request.form['num1'])
       num2 = int(request.form['num2'])
       
       # addition operation
    if(ops == 'add'):
        r = num1 + num2
        result =  ' the addition of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
       # subtract operation
    if(ops == 'subtract'):
        r = num1 - num2
        result =  ' the subtraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
           # multiply operation
    if(ops == 'multiply'):
        r = num1 * num2
        result =  ' the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
           # divide operation
    if(ops == 'divide'):
        r = num1 / num2
        result =  ' the division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
    
   # Using Postman Tool To Test APIs 
@app.route('/postman_data',methods = ['POST'])
def math_opration1 ():                                    
    if(request.method == 'POST'):
       ops = request.json['operation']
       num1 = int(request.json['num1'])
       num2 = int(request.json['num2'])
       
       # addition operation
    if(ops == 'add'):
        r = num1 + num2
        result =  ' the addition of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
       # subtract operation
    if(ops == 'subtract'):
        r = num1 - num2
        result =  ' the subtraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
           # multiply operation
    if(ops == 'multiply'):
        r = num1 * num2
        result =  ' the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)
    
           # divide operation
    if(ops == 'divide'):
        r = num1 / num2
        result =  ' the division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)  
    
    return jsonify(result) #jsonify use to give result in json form

if __name__ == '__main__':
    app.run(debug=True)