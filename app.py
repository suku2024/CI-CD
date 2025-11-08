from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form template
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Add Two Numbers</title>
</head>
<body>
    <h2>Enter two numbers to add:</h2>
    <form method="post">
        <input type="number" name="a" required> +
        <input type="number" name="b" required>
        <button type="submit">Add</button>
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def add():
    result = None
    if request.method == "POST":
        a = request.form.get("a", type=int)
        b = request.form.get("b", type=int)
        result = a + b
    return render_template_string(form_html, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
