import os
from flask import Flask, request, render_template, redirect
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
server = Flask(__name__)
system_prompt = "You are the personal assistant of Kangdong Jin!"


def send_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content":system_prompt},
                {"role": "user", "content": prompt}],
            temperature=0
        )
        response_dict = response.model_dump()
        response_message = response_dict["choices"][0]["message"]["content"]
        return response_message
    except Exception as e:
        return e


@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat4o.html', question="NULL", res="Question can't be empty!")
        question = request.form['question']
        print("======================================")
        print("Receive the question:", question)
        res = send_gpt(question)
        print("Q：\n", question)
        print("A：\n", res)

        return render_template('chat4o.html', question=question, res=str(res))
    return render_template('chat4o.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5000)
