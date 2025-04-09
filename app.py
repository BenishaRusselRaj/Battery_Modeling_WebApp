# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:01:12 2025

@author: IITM
"""
from flask import Flask, render_template
from image_plotting_webapp import plot_image
from apscheduler.schedulers.background import BackgroundScheduler
import os
import random

#%%
app = Flask(__name__)

#%%

scheduler = BackgroundScheduler()
scheduler.add_job(plot_image, 'interval', minutes = 1)
scheduler.start()

#%%
@app.route("/")

def display_homepage():
    plot_image()
    return render_template("index.html", config = {'RANDOM': random.random()})
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)