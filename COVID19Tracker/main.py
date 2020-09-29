import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading

def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_details():
    ls = []
    dict = {}
    res_dct = {}
    details = ""
    url = 'https://ncov2019.live/'
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'lxml')
    temp_confirmed = bs.find("div", class_="container--wrap bg-navy-4").find("table").find_all("tr")
    for block in temp_confirmed:
        for para in block.find_all('p', recursive=False):
            ls.append(para.text.strip())
    def Convert(ls):
        res_dct = {ls[i]: ls[i + 1] for i in range(0, len(ls), 2)}
        return res_dct
    dict = Convert(ls)
    for x, y in dict.items():
        details = details + y + " : " + x + "\n\n";
    return details
#Function to refresh
def refresh():
    newdata = get_corona_details()
    print("Refreshing...")
    mainLabel['text'] = newdata
#Function for notify
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID-19 cases of WORLD",
            message=get_corona_details(),
            timeout=10,
            app_icon='covid.ico'
        )
        time.sleep(30)
#Creating GUI:
root = tk.Tk()
root.geometry("600x500")
root.iconbitmap("covid.ico")
root.title("CORONA GLOBAL DATA TRACKER")
root.configure(background="white")
f = ("poppins", 10, "bold")
banner = tk.PhotoImage(file="covid.png")
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()
mainLabel = tk.Label(root, text=get_corona_details(), font=f, bg="white")
mainLabel.pack()
reBtn = tk.Button(root, text="REFRESH", font=f, relief="solid", command=refresh)
reBtn.pack()
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()
root.mainloop()
