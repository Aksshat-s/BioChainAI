from flask import Flask, render_template, request
from blockchain import Blockchain
import time  # Add this to generate the timestamp


app = Flask(__name__)


# Initialize Blockchain
blockchain = Blockchain()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_data():
    # Get user input from form
    hydration = request.form['hydration']
    sleep = request.form['sleep']
    symptoms = request.form['symptoms']
    stress = request.form['stress']
    notes = request.form['notes']


    user_data = {
        'hydration': hydration,
        'sleep': sleep,
        'symptoms': symptoms,
        'stress': stress,
        'notes': notes
    }


    # Generate a dummy AI summary
    ai_summary = f"Based on the provided physiology and lifestyle data, it appears that the user's hydration is {hydration}, sleep is {sleep} hours, stress level is {stress}, and reported symptoms include {symptoms}. Notes: {notes}. This is an educational summary and not a medical diagnosis."


    # Create a new block and append to blockchain
    blockchain.create_block(user_data, ai_summary, previous_hash=blockchain.chain[-1]['hash'])


    # Render the homepage with the dummy summary and timestamp
    return render_template('index.html', ai_summary=ai_summary, timestamp=time.strftime("%Y-%m-%d %H:%M:%S"))


@app.route('/chain')
def view_chain():
    # Check if blockchain is valid
    is_valid = blockchain.verify_chain()
    return render_template('chain.html', chain=blockchain.chain, is_valid=is_valid)


if __name__ == '__main__':
    app.run(debug=True)