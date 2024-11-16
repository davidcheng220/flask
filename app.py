from flask import Flask

app = Flask(__name__)
app.debug = True

# url
@app.route("/")
def home():
    return "<h1>hello</h1>"

# url/<username>  example url/David url/Ted
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
@app.route("/api/v2/department/dep_id/<dep_id>/emp_id/<emp_id>")
def get_employee(dep_id, emp_id):
    query_sql = """
    SELECT 
        emp_name,
        emp_id,
        emp_seat
    FROM emp
    WHERE emp_id = '{emp_id}' and dep_id = '{dep_id}'
    """
    # db.connect=query_sql
    return {
        "emp_name": "Daivd Cheng",
        "emp_id": "123",
        "emp_seat": "A9"
    }
# [GET] url/hello?username=David&age=22


# [POST] url/hello_post form_data = {"username": "David"}

if __name__ == "__main__":
    app.run()