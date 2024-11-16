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

# [GET] url/hello?username=David&age=22

# [POST] url/hello_post form_data = {"username": "David"}

if __name__ == "__main__":
    app.run()