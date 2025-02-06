from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Database simulation (in-memory storage)
users = {
    "Mahbod": {"password": "0B9U61", "memories": []},
    "AnooshePoor": {"password": "803KUJ", "memories": []},
    "Bayati": {"password": "5WI97C", "memories": []},
    "Biroodian":{"password": "81N734", "memories": []},
    "Pooya":{"password": "53G1PF", "memories": []},
    "MirAl":{"password": "6LA68O", "memories": []},
    "Haghan":{"password": "S32Q54", "memories": []},
     "ArshiaRaminRad":{"password": "R465B6", "memories": []},
     "Parham":{"password": "8ELE84", "memories": []},
     "ParsaRismanch":{"password": "5N6UC8", "memories": []},
     "Sajjadi":{"password": "H922J1", "memories": []},
     "Farhan":{"password": "H5E0H7", "memories": []},
     "Kandez":{"password": "1N980B", "memories": []},
     "Hesam":{"password": "P7C32R", "memories": []},
     "Farhadvand":{"password": "7BXH64", "memories": []},
     "MhmdKashani":{"password": "QPX358", "memories": []},
     "SadraKaka":{"password": "6T94L7", "memories": []},
     "Ata":{"password": "558H28", "memories": []},
     "Hirad":{"password": "30NCR2", "memories": []},
     "MatinMos":{"password": "H64GC1", "memories": []},
     "Nokhbe":{"password": "M622Z0", "memories": []},
     "Valizade":{"password": "HIH847", "memories": []},
     "Yusef": {"password": "Z687Y6", "memories": []},
     "Hashem": {"password": "9E9I55", "memories": []},
     "Yazdi": {"password": "271YSG", "memories": []},
     "Esi": {"password": "6O14OP", "memories": []},
     "Bahman": {"password": "XB4F57", "memories": []},
     "Parvizi": {"password": "38F4FT", "memories": []},
     "Hajizade": {"password": "N13TJ1", "memories": []},
     "AminHasani": {"password": "133B75", "memories": []},
     "Khodamoradi": {"password": "7O2G17", "memories": []},
     "AmirMohammadKhalili": {"password": "0O181U", "memories": []},
     "AliRezae": {"password": "62PH87", "memories": []},
     "Soradeghi": {"password": "HC3Q43", "memories": []},
     "ParsaSoheili": {"password": "5W5L0M", "memories": []},
     "Shahsavari": {"password": "43CG8A", "memories": []},
     "SahraNavard": {"password": "0C26N4", "memories": []},
     "RaminAbd": {"password": "79AM46", "memories": []},
     "Asgar": {"password": "CW366I", "memories": []},
     "Fakhri": {"password": "T47X48", "memories": []},
     "BlackGarden": {"password": "SRB331", "memories": []},
     "NasrAbad": {"password": "Y1W7W0", "memories": []},
     "Modiri": {"password": "241DJ0", "memories": []},
     "SEYED": {"password": "82L47F", "memories": []},
     "ErfanMoghimi": {"password": "9GK47D", "memories": []},
     "Gabriel": {"password": "0P7G35", "memories": []},
     "KasraNaser": {"password": "31661B", "memories": []},
     "AliNoorbakhsh": {"password": "104E48", "memories": []},
     "HadiArabloo": {"password": "305IC1", "memories": []},
     "KasraAhmadi": {"password": "X17O9M", "memories": []},
     "NimaAnoosh": {"password": "6HVO55", "memories": []},
     "Aram": {"password": "7KYS88", "memories": []},
     "Azade": {"password": "R96Y4Q", "memories": []},
     "Radman": {"password": "G232H2", "memories": []},
     "Jazdare": {"password": "F11D44", "memories": []},
     "Javazi": {"password": "7NJI52", "memories": []},
     "HajiHosseini": {"password": "H0X24D", "memories": []},
     "SadraRezae": {"password": "27EI16", "memories": []},
     "Sepehri": {"password": "U9YA87", "memories": []},
     "Shambiz": {"password": "KR7344", "memories": []},
     "Shafizade": {"password": "Q8533D", "memories": []},
     "Taheri": {"password": "387P67", "memories": []},
     "Golmakan": {"password": "79N0E0", "memories": []},
     "Farid": {"password": "382288", "memories": []},
     "NimaHosseini": {"password": "287369", "memories": []},
     "Miri": {"password": "48X9H4", "memories": []},     
     "iliaHossein": {"password": "OD1Q99", "memories": []},
     "Amjad": {"password": "6PJ2K6", "memories": []},
     "Rabbani": {"password": "647JFT", "memories": []},
     "ArianRamezan": {"password": "UM484W", "memories": []},
     "KiarashSakha": {"password": "L1F324", "memories": []},
     "Solgi": {"password": "77PR48", "memories": []},
     "Shariat": {"password": "U8CL30", "memories": []},
     "Farazmand": {"password": "0TYN68", "memories": []},
     "Manooch": {"password": "55YK65", "memories": []},
     "HasanParsa": {"password": "28P6L9", "memories": []},
     "Variji": {"password": "26J6L7", "memories": []},
     "Gabriel": {"password": "29Q6L7", "memories": []},
}

# Define the admin user separately
admin_user = "admin"
admin_password = "adminpass1385"
memories = []  # This will store all the memories globally

# Login page
@app.route("/")
def index():
    return render_template("index.html")

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Check if the user is admin
    if username == admin_user and password == admin_password:
        return jsonify({"message": "Login successful", "username": username, "role": "admin"})
    
    if username in users and users[username]["password"] == password:
        return jsonify({"message": "Login successful", "username": username, "role": "user"})
    
    return jsonify({"message": "Invalid username or password"}), 401

# Add memory endpoint
@app.route("/add-memory", methods=["POST"])
def add_memory():
    data = request.json
    username = data.get("username")
    memory = data.get("memory")

    if username in users or username == admin_user:
        memory_id = len(memories) + 1  # Create a unique ID for each memory
        memories.append({"id": memory_id, "username": username, "memory": memory})
        return jsonify({"message": "Memory added successfully"})
    return jsonify({"message": "User not found"}), 404

# Get all memories endpoint
@app.route("/get-memories", methods=["GET"])
def get_memories():
    return jsonify({"memories": memories})

# Edit memory endpoint (only for the user's own memory or admin)
@app.route("/edit-memory", methods=["POST"])
def edit_memory():
    data = request.json
    memory_id = data.get("memoryId")
    new_memory = data.get("newMemory")
    username = data.get("username")
    
    for memory in memories:
        if memory['id'] == memory_id and (memory['username'] == username or username == admin_user):
            memory['memory'] = new_memory
            return jsonify({"message": "Memory updated successfully"})
    
    return jsonify({"message": "Failed to update memory"}), 400

# Delete memory endpoint (only for the user's own memory or admin)
@app.route("/delete-memory", methods=["POST"])
def delete_memory():
    data = request.json
    memory_id = data.get("memoryId")
    username = data.get("username")
    
    global memories

    # If the user is admin, delete any memory
    if username == admin_user:
        memories = [memory for memory in memories if memory['id'] != memory_id]
    # Otherwise, only allow the user to delete their own memory
    elif username in users:
        memories = [memory for memory in memories if memory['id'] != memory_id or memory['username'] != username]

    return jsonify({"message": "Memory deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
    