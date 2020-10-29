import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env    
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


#link to about.html
@app.route("/about")
def about():
    data=[]
    with open("data/company.json","r") as json_data: #r means read only
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    members = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                members = obj
    return render_template("member.html", member=members)

#link to contact.html
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        #print(request.form.get("name")) #get only name from the form and print in the terminal, method 1
        #print(request.form ["email"]) #get only email from the form and print in the terminal, method 2
        flash("Thanks {}, we have received your message.".format(request.form.get("name"))) #this is a flash message which disappears after refreshing the page
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__=="__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)
        ##never submit a project with debug=True!!!