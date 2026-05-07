from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    extracted_text = ""

    if request.method == "POST":

        pdf_file = request.files["resume"]

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

    return render_template("index.html", text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)