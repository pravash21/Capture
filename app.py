from flask import Flask, request, render_template, url_for
from Main import img_gen , pdf_gen , delete
from apscheduler.schedulers.background  import BackgroundScheduler

app = Flask(__name__, static_url_path='/static')
# app.debug = True

time_diff = 5 #minutes

def sensor():
    delete(val='img',time = time_diff)
    delete(val='pdf',time = time_diff)

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=time_diff)
sched.start()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_link():
    link = request.form['link']
    img_name = img_gen(link)
    pdf_name = pdf_gen(img_name)
    save=1
    return render_template("index.html", img_name=img_name,save=save, pdf_name=pdf_name)

if __name__ == '__main__':
    app.run()