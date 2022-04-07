import sqlite3
from flask import Flask, render_template, request

data = sqlite3.connect("studentdata.db", check_same_thread=False)
table = data.execute("select name from sqlite_master where type='table' and name= 'student'").fetchall()
if table != []:
    print("Table already exists")

else:
    data.execute('''create table student(
                                    id integer primary key autoincrement,
                                    Name text,
                                    Branch text,
                                    Admno integer,
                                    rollno integer,
                                    DOB text,
                                    Semester text,
                                    password text                                   
                                    ); ''')
    print("table executed")

stud = Flask(__name__)


@stud.route("/")
def stud_login():
    return render_template("studentlogin.html")


@stud.route("/register", methods=["GET", "POST"])
def stud_register():
    if request.method == "POST":
        getName = request.form["name"]
        getBranch = request.form["branch"]
        getAdmno = request.form["admno"]
        getrollno = request.form["rollno"]
        getDOB = request.form["dob"]
        getSemester = request.form["sem"]
        getpassword = request.form["pass"]
        getconfirmpassword = request.form["cnfpass"]
        print(getName)
        print(getBranch)
        print(getAdmno)
        print(getrollno)
        print(getDOB)
        print(getSemester)
        print(getpassword)
        print(getconfirmpassword)
        try:
            query = "insert into student(Name,branch,rollno,admno,DOB,password,Semester) values('" + getName + "','" + getBranch + "'," + getrollno + "," + getAdmno + ",'" + getDOB + "','" + getpassword + "','" + getSemester + "')"
            print(query)
            data.execute(query)
            data.commit()
            data.close()
            print("data added to database")
        except Exception as err:
            print("error occurred", err)
    return render_template("studentregister.html")


@stud.route("/search")
def stud_search():
    return render_template("studentsearch.html")


@stud.route("/delete")
def stud_delete():
    return render_template("studentdelete.html")

@stud.route("/viewall")
def stud_view():
    cursor = data.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    result=cursor.fetchall()
    return render_template("studentviewall.html",students=result)

if __name__ == "__main__":
    stud.run()
