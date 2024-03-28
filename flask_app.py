from flask import Flask, request, jsonify
from flask_cors import CORS
import facebook
import instagram


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/get/social/post', methods=['POST'])
def start_bot():
    # print("hello")
    data = request.get_json()
    print(data)

    platform = data['platform']
    search_data = data['search_data']
    location = data['location']

    if location != "":
        search_index = search_data + " in " + location
    else:
        search_index = search_data

    
    if platform == "facebook":
        response_data = facebook.run(search_index)
    if platform == "instagram":
        response_data = instagram.run(search_index)
    

    
    print(response_data)
    return response_data


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=80)