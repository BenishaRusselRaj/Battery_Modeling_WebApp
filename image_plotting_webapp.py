# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:02:17 2025

@author: IITM
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mysql.connector
import os
from dotenv import load_dotenv


#%%
def plot_image():
    load_dotenv()
    img_path = r"D:\Benisha\Farhan\Battery_Modeling_Web_Application\Scripts_render_flask\static"
    myDBconn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "dt_model_6ah_cell")
        )

    query = 'SELECT * FROM sample_data;'
    
    data = pd.read_sql(query, myDBconn)
    
    
    
    matplotlib.use('agg')
    plt.figure()
    plt.plot(range(len(data)), data.loc[:,'Cell_1':'Cell_14'])
    plt.ylabel('Voltage (V)', size = 10, fontweight = 'bold')
    plt.title('Cell Voltage-changed', fontweight = 'bold')
    plt.grid(linestyle = 'dotted')
    plt.savefig(img_path+'\cellV_plot.png', dpi =1500)
    plt.close()
    
    plt.figure()
    plt.plot(range(len(data)), data['Mean_V'])
    plt.ylabel('Voltage (V)', size = 10, fontweight = 'bold')
    plt.title('Average Voltage', fontweight = 'bold')
    plt.grid(linestyle = 'dotted')
    plt.savefig(img_path+'\meanV_plot.png', dpi =1500)
    plt.close()
    
    plt.figure()
    plt.plot(range(len(data)), data['Max_V'])
    plt.ylabel('Voltage (V)', size = 10, fontweight = 'bold')
    plt.title('Maximum Voltage', fontweight = 'bold')
    plt.grid(linestyle = 'dotted')
    plt.savefig(img_path+'\maxV_plot.png', dpi =1500)
    plt.close()
    
    plt.figure()
    plt.plot(range(len(data)), data['Min_V'])
    plt.ylabel('Voltage (V)', size = 10, fontweight = 'bold')
    plt.title('Minimum Voltage', fontweight = 'bold')
    plt.grid(linestyle = 'dotted')
    plt.savefig(img_path+'\minV_plot.png', dpi =1500)
    plt.close()
    
    myDBconn.close()
    