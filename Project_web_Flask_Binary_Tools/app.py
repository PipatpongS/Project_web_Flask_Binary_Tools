from flask import Flask, render_template, request
import binary_tool as bt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        # รับค่าจาก HTML (name="user_input")
        data = request.form.get("user_input")
        mode = request.form.get("mode")
        
        if mode == "to_binary":
            res_list = bt.text_to_binary(data)
            result = " ".join(res_list)
        elif mode == "to_text":
            # (ใส่ Logic การ clean code ของคุณตรงนี้)
            clean_data = "".join(data.strip().split())
            binary_list = [clean_data[i:i+8] for i in range(0, len(clean_data), 8)]
            result = bt.binary_to_text(binary_list)
            
    return render_template("index.html", result_show=result)

if __name__ == "__main__":
    app.run(debug=True)