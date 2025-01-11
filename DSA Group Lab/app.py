from flask import Flask, request, jsonify, render_template
from linked_list import LinkedList
from stack import infix_to_postfix_conversion
from queues import Queue

app = Flask(__name__)
linked_list = LinkedList()
queue = Queue()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/linkedlist')
def linkedlist():
    return render_template('linkedlist.html')

@app.route('/stack')
def stack():
    return render_template('stack.html')

@app.route('/queues')
def queues():
    return render_template('queues.html')

@app.route('/add', methods=['POST'])
def add_node():
    data = request.form['data']
    linked_list.append(data)
    return jsonify({'status': 'success', 'list': linked_list.display()})

@app.route('/remove_beginning', methods=['POST'])
def remove_beginning():
    removed_data = linked_list.remove_beginning()
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    removed_data = linked_list.remove_at_end()
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/remove_at', methods=['POST'])
def remove_at():
    data = request.form['data']
    removed_data = linked_list.remove_at(data)
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/display', methods=['GET'])
def display_list():
    return jsonify({'list': linked_list.display()})

@app.route('/infix_to_postfix', methods=['POST'])
def infix_to_postfix():
    data = request.get_json()
    infix = data.get('expression', '')
    try:
        postfix, steps = infix_to_postfix_conversion(infix.replace(" ", ""))
        return jsonify({'postfix': postfix, 'steps': steps})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.json.get('value')
    if data:
        queue.enqueue(data)
        return jsonify({"message": "Value enqueued successfully", "queue": queue.display()})
    return jsonify({"error": "No value provided"}), 400

@app.route('/dequeue', methods=['POST'])
def dequeue():
    removed_value = queue.dequeue()
    if removed_value is not None:
        return jsonify({"message": "Value dequeued successfully", "removed_value": removed_value, "queue": queue.display()})
    return jsonify({"error": "Queue is empty"}), 400

@app.route('/display', methods=['GET'])
def display():
    return jsonify({"queue": queue.display()})

@app.route('/peek', methods=['GET'])
def peek():
    front_value = queue.peek()
    if front_value is not None:
        return jsonify({"message": "Front value retrieved", "front_value": front_value})
    return jsonify({"error": "Queue is empty"}), 400

if __name__ == '__main__':
    app.run(debug=True)
