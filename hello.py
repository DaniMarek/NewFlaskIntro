from flask import Flask, render_template
# from flask import Flask #import Flask to allow us to create our app
app=Flask(__name__) #Global variable _name_ tells Flask whether or not we are running the file
@app.route('/') #The '@' symbol designates a 'decorator' which attaches the following. Function to the '/' route. This means that whenever we send a request to. localhost:5000/ we will run the following 'hello_world' function
def hello_world():
	print "Hello World!"
	return render_template('index.html') #render the template and return it!
	# return 'Hello World!' #Return the string 'Hello World!' as a response
@app.route('/success')
# this indicates what will be displayed or run when url /success is initiated
def success():
	return render_template('success.html')
app.run(debug=True)  #Run the app in debug mode