from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    extracted_text = ""
    score = 0
    suggestions = []

    if request.method == "POST":

        pdf_file = request.files["resume"]

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

        text = extracted_text.lower()

        if "python" in text:
            score += 20

        if "java" in text:
            score += 20

        if "machine learning" in text:
            score += 20

        if "communication" in text:
            score += 20

        if "teamwork" in text:
            score += 20

        if "projects" not in text:
            suggestions.append("Add Projects Section")

        if "internship" not in text:
            suggestions.append("Add Internship Experience")

    return render_template(
        "index.html",
        text=extracted_text,
        score=score,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)