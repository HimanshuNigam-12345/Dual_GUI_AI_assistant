import sys
import os
from flask import Flask, render_template, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.prompts import qa_prompts, summary_prompts, creative_prompts
from shared.core import get_ai_response, save_feedback

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        function = request.form["function"]
        variant = request.form["prompt_variant"]
        user_input = request.form["user_input"]

        prompt_dict = {}
        format_key = ""

        if function == "qa":
            prompt_dict = qa_prompts
            format_key = "question"
        elif function == "summary":
            prompt_dict = summary_prompts
            format_key = "text"
        elif function == "creative":
            prompt_dict = creative_prompts
            if variant == "zero_shot":
                format_key = "topic"
            elif variant == "few_shot":
                format_key = "theme"
            else:
                format_key = "hook"

        prompt_template = prompt_dict.get(variant)
        final_prompt = prompt_template.format(**{format_key: user_input})

        response = get_ai_response(final_prompt)
        return render_template("result.html",
                               response=response,
                               function=function,
                               prompt=final_prompt)

    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def feedback():
    func = request.form["function"]
    prompt = request.form["prompt"]
    helpful = request.form["helpful"] == "yes"
    note = request.form.get("note", "")
    save_feedback(func, prompt, helpful, note)
    return "Feedback saved! <a href='/'>Back</a>"

if __name__ == "__main__":

    app.run(debug=True)
