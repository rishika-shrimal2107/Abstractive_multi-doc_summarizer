from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the selected document type from the form
        service = request.form["document_type"]

        # Redirect to the respective page based on the selected document type
        return redirect(url_for(service))
    
    return render_template("home.html")

@app.route("/news", methods=["GET", "POST"])
def news():
    if request.method == "POST":
        data = request.form["data"]
        maxL = int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post("https://api-inference.huggingface.co/models/facebook/bart-large-cnn",headers = {"Authorization": f"Bearer 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"},json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })[0]

        return render_template("news.html", result=output["summary_text"])
    else:
        return render_template("news.html")
    
@app.route("/dialogue", methods=["GET", "POST"])
def dialogue():
    if request.method == "POST":
        data = request.form["data"]
        maxL = int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post("https://api-inference.huggingface.co/models/rishitau/pegasus-samsum-model",headers = {"Authorization": f"Bearer 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"},json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })[0]

        return render_template("dialogue.html", result=output["generated_text"])
    else:
        return render_template("dialogue.html")

@app.route("/scientific", methods=["GET", "POST"])
def scientific():
    if request.method == "POST":
        data = request.form["data"]
        maxL = int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post("https://api-inference.huggingface.co/models/haining/scientific_abstract_simplification",headers = {"Authorization": f"Bearer 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"},json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })[0]

        return render_template("scientific.html", result=output["generated_text"])
    else:
        return render_template("scientific.html")
    
    

@app.route("/legal", methods=["GET", "POST"])
def legal():
    if request.method == "POST":
        data = request.form["data"]
        maxL = int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post("https://api-inference.huggingface.co/models/facebook/bart-large-cnn",headers = {"Authorization": f"Bearer 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"},json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })[0]

        return render_template("legal.html", result=output["summary_text"])
    else:
        return render_template("legal.html")
    
@app.route("/general", methods=["GET", "POST"])
def general():  
    if request.method == "POST":
        data = request.form["data"]
        maxL = int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post("https://api-inference.huggingface.co/models/haining/scientific_abstract_simplification",headers = {"Authorization": f"Bearer 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"},json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })[0]

        return render_template("general.html", result=output["generated_text"])
    else:
        return render_template("general.html")
    

@app.route("/medical", methods=["GET", "POST"])
def medical():
    if request.method == "POST":
        data = request.form["data"]
        maxL = int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post("https://api-inference.huggingface.co/models/Falconsai/medical_summarization",headers = {"Authorization": f"Bearer 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"},json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })[0]

        return render_template("medical.html", result=output["summary_text"])
    else:
        return render_template("medical.html")


if __name__ == '__main__':
    app.debug=True
    app.run()

