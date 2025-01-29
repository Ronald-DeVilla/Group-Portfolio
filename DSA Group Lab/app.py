from flask import Flask, request, jsonify, render_template
from linked_list import LinkedList
from stack import infix_to_postfix_conversion
from queues import Queue
from binary_tree import calculate_node_positions, calculate_lines

app = Flask(__name__)
linked_list = LinkedList()
queue = Queue()


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

@app.route('/train')
def train():
    return render_template('train.html')

@app.route('/binary_tree')
def binary_tree():
    return render_template('binary_tree.html')

@app.route('/sorting')
def sorting():
    return render_template('sorting.html')

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

stations = {
    "LRT1": [
        "Baclaran", "EDSA", "Libertad", "Gil Puyat", "Vito Cruz",
        "Quirino", "Pedro Gil", "United Nations", "Central Terminal",
        "Carriedo", "Doroteo Jose", "Bambang", "Tayuman", "Blumentritt",
        "Abad Santos", "R. Papa", "5th Avenue", "Monumento", "Balintawak",
        "Roosevelt"
    ],
    "LRT2": [
        "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz",
        "Gilmore", "Betty Go-Belmonte", "Cubao", "Anonas",
        "Katipunan", "Santolan", "Marikina", "Antipolo"
    ],
    "MRT": [
        "North Avenue", "Quezon Avenue", "GMA-Kamuning", "Araneta Center-Cubao",
        "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni", "Guadalupe",
        "Buendia", "Ayala", "Magallanes", "Taft Avenue"
    ]
}

@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    return response

@app.route('/stations/<train>', methods=['GET'])
def get_stations(train):
    if train in stations:
        return jsonify({"stations": stations[train]})
    return jsonify({"message": "Train line not found"}), 404

@app.route('/route', methods=['POST'])
def calculate_route():
    data = request.json

    train = data.get("train")
    start = data.get("start")
    target = data.get("target")

    if not (train and start and target):
        return jsonify({"message": "Missing train, start, or target parameter"}), 400

    if train in stations:
        train_stations = stations[train]
        try:
            start_index = train_stations.index(start)
            target_index = train_stations.index(target)
        except ValueError:
            return jsonify({"message": "Invalid start or destination station"}), 400

        if start_index <= target_index:
            route = train_stations[start_index:target_index + 1]
        else:
            route = train_stations[target_index:start_index + 1][::-1]

        return jsonify({"route": route})

    return jsonify({"message": "Train line not found"}), 404

@app.route('/generate-tree', methods=['POST'])
def generate_tree():
    data = request.get_json()
    if not data or 'nodeInput' not in data:
        return jsonify({'error': 'Missing or invalid input'}), 400

    input_values = data['nodeInput'].strip().split()
    
    try:
        
        positions = calculate_node_positions(input_values)
        lines = calculate_lines(positions)
    
    except ValueError:
        return jsonify({'error': 'Invalid input: Node values should be numbers or strings'}), 400

    return jsonify({'nodes': positions, 'lines': lines})

if __name__ == '__main__':
    app.run(debug=True)
