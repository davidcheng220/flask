from flask import Flask, request, render_template
from utils import testfun
import model

app = Flask(__name__)

# url
@app.route("/")
def home():
    return "<h1>hello</h1>"

# url/<username>  example url/David or url/Ted
@app.route("/<username>")
def name(username):
    return f"Hello {username}"
    # output_html = f"""
    # <h1>
    #     Hello {username}
    # </h1>
    # """
    # return output_html

#[GET] url/api/v2/department/dep_id/<dep_id>/emp_id/<emp_id> 
# setting up for string
@app.route("/api/v2/department/dep_id/<string:dep_id>/emp_id/<int:emp_id>")
def get_employee(dep_id: str, emp_id: int):
    query_sql = """
    SELECT 
        emp_name,
        emp_id,
        emp_seat
    FROM emp
    WHERE emp_id = '{emp_id}' and dep_id = '{dep_id}'
    """
    # print(type(dep_id))
    # print(type(emp_id))
    # db.connect=query_sql
    return {
        "emp_name": "Daivd Cheng",
        "emp_id": "123",
        "emp_seat": "A9"
    }

# import request
# [GET] url/hello?username=David&age=22
@app.route("/wobuzhidao")
def wobuzhidao():
    username = request.args.get("username")
    age = request.args.get("age")
    
    # if username is None:
    #     return f"what is your name"
    if not username:
        return "What is your name?"
    if not age:
        return "What is you age?"
    return f"Hello, {username}, age is {age}"



# [POST] url/hello_post form_data = {"username": "David"}
@app.route("/hello_post", methods=["GET","POST"])
def hello_post():
    username = ""
    form_html = """
    <form method="post" action="/hello_post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <input type="submit" value="Submit">
    </form>
    """
    # get request methods 
    request_method = request.method
    print(request_method)
    # get form element named username
    username = request.form.get("username")

    if request_method == "POST":
        form_html += f"""
        <h1>
            Hello, {username} 
        </h1>
        """ 
    return form_html

# url/two_sum/<int:x>/<int:y>
@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int):
    return str(testfun(x,y))

@app.route('/hello_post2', methods=['GET', 'POST'])
def hello_post2():
    if request.method == 'GET':
        return render_template('hello_post.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        return render_template('hello_post.html',
                               username=username,
                               request_method='post')

# get staff form sql and label data in board
@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


# open internal access
if __name__ == "__main__":
    # add debug mode
    app.run(debug=True, host="0.0.0.0", port=5000)