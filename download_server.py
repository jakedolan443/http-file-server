from flask import Flask, render_template
import os

app = Flask(__name__)
run_path = os.getcwd()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    full_path = "{}/static/{}".format(run_path, path)
    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        data = [path,[]]
        for f in files:
            data[1].append({"path":"{}/{}".format(path, f), "end":f, "size":os.path.getsize("{}/{}".format(full_path, f))})
            if os.path.isdir("{}/{}".format(full_path, f)):
                data[1][-1]['size'] = "-"
        return render_template('index.html', data=data)
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run()
