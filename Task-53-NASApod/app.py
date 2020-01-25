import requests
import json
import wget
import traceback
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from os import path
from time import sleep
from datetime import date
from fpdf import FPDF
def generatepdf(title, tentative, desc):
    pdf = FPDF()
    dpath = "./files-apod/"+tentative+".jpg"
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=1, align="C")
    pdf.ln(95)
    pdf.image(name = dpath ,x=55, y=20, h=100)
    pdf.ln()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 5, desc, align="C")
    pdf.output("./files-apod/"+tentative+".pdf")
def getstatement(tentative):
    if tentative != None:
        url = "https://api.nasa.gov/planetary/apod?api_key=DlArxIrdbCsDiAB2mA6Jo4m0PBFrWut8VSnkAQDe&date="+tentative
    else:
        url = "https://api.nasa.gov/planetary/apod?api_key=DlArxIrdbCsDiAB2mA6Jo4m0PBFrWut8VSnkAQDe"
    response = requests.get(url)
    if response.status_code != 200:
        return 1
    else:
        response = response.text
        response = json.loads(response) 
        title = response['title']
        web_url = response['url']       
        exp = response['explanation']
        return (exp,title,web_url)
def downloadstatement(img_url, tentative):
    try:
        wget.download(img_url, 'files-apod/'+tentative+'.jpg')
        return 0
    except Exception:
        traceback.print_exc()
        return 1
app = Flask(__name__)
@app.before_first_request
def check_dir():
    if path.exists("./files-apod") == False:
        os.system("mkdir ./files-apod")
@app.route('/') 
def main():
    return render_template('index.html')
@app.route('/apod')
def pod():
    tentative = request.args.get('date')
    if tentative == None:
        tentative = str(date.today())
    info = getstatement(tentative)
    if info == 1:
        return render_template('error_404.html'),404
    url = info[2]
    title = info[1]
    expl = info[0]
    img_download = "/imagedownload?date=" + tentative
    pdf_download = "/pdfdownload?date=" + tentative
    return render_template('nasapod.html', title=title, desc=expl, img_url=url, pdf_download_url = pdf_download, img_download_url = img_download, tentative=tentative)
@app.route('/imagedownload')
def download_img():
    tentative = request.args.get('date')
    url = getstatement(tentative)
    url = url[2]
    if path.exists("./files-apod/"+tentative+".jpg") == False:
        rcode = downloadstatement(url, tentative)
        if rcode != 0:
            return render_template("error.html"), 500
        else:
            return send_file("./files-apod/"+tentative+".jpg", as_attachment=True)
    else:
        return send_file("./files-apod/"+tentative+".jpg", as_attachment=True)
@app.route('/pdfdownload')
def download_pdf():
    tentative = request.args.get('date')
    img_info = getstatement(tentative)
    url = img_info[2]
    exp = img_info[0]
    title = img_info[1]
    if path.exists("./files-apod/"+tentative+".pdf") == False:

        if path.exists("./files-apod/"+tentative+".jpg") == False:
            rcode = downloadstatement(url, tentative)
            if rcode != 0:
                return render_template("error.html"), 500
            else:
                generatepdf(title, tentative, exp)
                return send_file("./files-apod/"+tentative+".pdf", as_attachment=True)
        else:
            generatepdf(title, tentative, exp)
            return send_file("./files-apod/"+tentative+".pdf", as_attachment=True)
    else:
        return send_file("./files-apod/"+tentative+".pdf", as_attachment=True)

app.run(host='127.0.0.1', port=1337, debug=True)