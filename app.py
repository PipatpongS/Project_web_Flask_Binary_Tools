from flask import Flask, render_template, request
import binary_tool as bt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        data = request.form.get("user_input")
        mode = request.form.get("mode")
        
        if mode == "to_binary":
            res_list = bt.text_to_binary(data)
            result = " ".join(res_list) 
            
        elif mode == "to_text":
            binary_list = data.strip().split()           
            result = bt.binary_to_text(binary_list)
            
    return render_template("index.html", result_show=result)

if __name__ == "__main__":
    app.run(debug=True)