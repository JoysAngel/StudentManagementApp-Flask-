from flask import Flask, render_template

stud=Flask(__name__)

@stud.route('/')
def stud_login():
    return render_template("studentlogin.html")

@stud.route('/register')
def stud_register():
    return render_template("studentregister.html")

@stud.route('/search')
def stud_search():
    return render_template("studentsearch.html")

@stud.route('/delete')
def stud_delete():
    return render_template("studentdelete.html")

if __name__=="__main__":
    stud.run()
