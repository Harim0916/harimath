from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process the submitted answers and return the results
        submitted_answers = request.form.to_dict()
        correct_answers = {
            'q1': 'b',
            'q2': 'b'
        }
        score = 0
        for question, answer in submitted_answers.items():
            if answer == correct_answers[question]:
                score += 1
        results = {
            'score': score,
            'total': len(correct_answers)
        }
        return jsonify(results)
    else:
        # Render the quiz page
        return render_template('index.html')

if __name__ == '__main__':
     app.run('0.0.0.0', port=5000, debug=True)