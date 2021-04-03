from flask import Flask, send_from_directory, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/api/logs")
def get_All_Log():
    import os
    all_log_file = []
    for x in os.popen('ls log/').readlines():
        all_log_file.append("log/"+x.replace('\n', ''))
    tasks = []
    for log in all_log_file:
        f = open(log, 'r')
        logs_detal = f.read()
        f.close()
        f = open(log, 'r')
        logs_detal_array = f.readlines()[1].split(" ",1)
        f.close()
        tasks.append(
            {
                'name': logs_detal_array[1],
                'date': logs_detal_array[0], 
                'log': logs_detal
             }
        )


                    
    return jsonify(
        tasks = tasks
    )

# @app.route("/api/stop")
# def stop_app():
#     from subprocess import PIPE,Popen
#     screens = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
#     for screen in screens:
#         Popen(['screen', '-S', screen, '-X','quit'],stderr=PIPE,stdout=PIPE) 
#     Popen(['rm', '-R', 'audio/'],stderr=PIPE,stdout=PIPE) 
#     Popen(['rm', '-R', 'log/'],stderr=PIPE,stdout=PIPE) 
#     Popen(['mkdir', 'audio/'],stderr=PIPE,stdout=PIPE) 
#     Popen(['mkdir', 'log/'],stderr=PIPE,stdout=PIPE) 
#     return jsonify(
#         status = "ok"
#     )




# @app.route("/api/start")
# def start_App():
#     from subprocess import PIPE,Popen
#     process = Popen(['python3', 'main.py'],stderr=PIPE,stdout=PIPE) 
#     return jsonify(
#         status = "ok"
#     )



@app.route('/log/<path:path>')
def send_js(path):
    return send_from_directory('log', path)


app.run(host="0.0.0.0", port=8000)

