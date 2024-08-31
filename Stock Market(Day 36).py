import requests
import json
import datetime
import tkinter
from tkinter import messagebox
from datetime import timedelta

news_api_key = "52223c3dccd44a08810bc213af8da0ed"
api = "XZNJPIODY281OXWS"

window = tkinter.Tk()
window.minsize(width = 500, height = 600)
window.title("Stock Market")
window.config(bg = "#2B3E50")

symbol_label = tkinter.Label()
symbol_label.config(text = "Symbol: ", bg = "#2B3E50", fg = "white", font = ("Courier", 13, "bold"))
symbol_label.grid(column = 1, row = 1, padx = 10, pady = 10)

symbol_text = tkinter.Text()
symbol_text.focus()
symbol_text.config(width = 13, height =1 )
symbol_text.grid(column = 2, row = 1)
symbol = symbol_text.get("1.0", tkinter.END)

headline_label = tkinter.Label()

parameters_news = {"apiKey": news_api_key, "country": "in"}
news = requests.get(url = "https://newsapi.org/v2/top-headlines", params = parameters_news)
articles = news.json()

all_articles = articles["articles"][:19]
titles = [f"Headline: {article['title']}" for article in all_articles]
i = 0
def news(i):
    headline_label.config(text = f"{titles[i]}", font = ("Courier" ,9,"normal"), width = 90, height = 4, wraplength = 400, highlightthickness=1, highlightbackground= "black")
    headline_label.grid(column = 1, row = 0, columnspan = 4, padx=  5, pady = 5)
    if i>= 19:
        i = 0
    window.after(5000, lambda:news(i+1))

news(i)

def get_date(file, date_text, symbol):
    date = date_text.get("1.0", tkinter.END).strip()
    if not date:
        messagebox.showinfo(title="Alert!", message="Please enter a date.")
        return
    try: 
        closee = file["Time Series (Daily)"][f"{str(date)}"]["4. close"]
        openn = file["Time Series (Daily)"][f"{str(date)}"]["1. open"]
        high = file["Time Series (Daily)"][f"{str(date)}"]["2. high"]
        low = file["Time Series (Daily)"][f"{str(date)}"]["3. low"]
    except KeyError as e:
        messagebox.showinfo(title="Alert!", message="Data not available for the selected dates.")
        return

    text_label2 = tkinter.Label()
    text_label2.config(text = f"Date: {date}\nTimezone: US/Eastern\n\nSymbol: {symbol.upper()}\nOpen: {openn}\nHigh: {high}\nLow: {low}\nClose: {closee}\n", font = ("Courier" ,9,"normal"), width = 45, highlightthickness = 2, highlightbackground = "black")
    text_label2.grid(column = 1, row = 6, columnspan = 2, padx = 5, pady = 5)

def get_stocks():
    symbol = symbol_text.get("1.0", tkinter.END).strip()
    parameters = {"function":"TIME_SERIES_DAILY", "symbol":symbol.upper(), "apikey":api}

    resp = requests.get(url = "https://www.alphavantage.co/query", params = parameters)
    if not symbol:
        symbol_text.delete("1.0", tkinter.END)
        messagebox.showinfo(title="Alert!", message="Please enter a symbol.")
        return
        
    file = resp.json()
    today = datetime.datetime.today().date()
    yesterday = today - datetime.timedelta(days = 1)
    day_before_yesterday = today - datetime.timedelta(days = 2)
    try:
        close_yesterday = file["Time Series (Daily)"][str(yesterday)]["4. close"]
        close_before_yesterday = file["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
    except KeyError:
        messagebox.showinfo(title="Alert!", message="Enter a valid symbol.")
        return

            
    difference = abs(float(close_yesterday) - float(close_before_yesterday))
    percent = (0.75/float(close_before_yesterday)) * 100

    text_label = tkinter.Label()
    text_label.config(text = f"Today's Date: {today}\nTimezone: US/Eastern\n\nSymbol: {symbol.upper()}\nClosing (yesterday): {close_yesterday}\nClosing (Day before yesterday): {close_before_yesterday}\nDifference: {difference:5f}\nPercent: {percent:2f}%", font = ("Courier" ,9,"normal"),width = 45, highlightthickness = 2, highlightbackground = "black")
    text_label.grid(column = 1, row = 3, columnspan = 2, padx = 5, pady = 5)

    response = messagebox.askyesno(title = "Question", message = "Do you want to check the stock data of a particular day?")
    if response:
        date_label = tkinter.Label()
        date_label.config(text = "Date: ", fg = "white", bg = "#2B3E50", font = ("Courier", 13, "bold"))
        date_label.grid(column = 1, row = 4)

        date_text = tkinter.Text()
        date_text.focus()
        date_text.config(width = 13, height = 1)
        date_text.grid(column = 2, row = 4)

        get_date_button = tkinter.Button(text = "Get Data", command = lambda : get_date(file, date_text, symbol))
        get_date_button.config(bg = "white", font = ("Courier", 10, "bold"))
        get_date_button.grid(column = 1, row = 5, columnspan = 2)
                          
    if percent > 0:

        parameters_news = {"apiKey": news_api_key, "q": symbol.upper()}
        news = requests.get(url = "https://newsapi.org/v2/everything", params = parameters_news)
        articles = news.json()
        three_articles = articles["articles"][:3]

        name = three_articles[0]["source"]["name"]
        art = three_articles[0]["title"]
        des = three_articles[0]["description"]

        name1 = three_articles[1]["source"]["name"]
        art1 = three_articles[1]["title"]
        des1 = three_articles[1]["description"]

        name2 = three_articles[2]["source"]["name"]
        art2 = three_articles[2]["title"]
        des2 = three_articles[2]["description"]

        art_label = tkinter.Label()
        art_label.config(text = "Some Related News", fg = "white", bg = "#2B3E50", font = ("Courier", 13, "bold"), highlightthickness=2, highlightbackground="white")
        art_label.grid(column = 3, row = 1, columnspan = 3)

        article_label = tkinter.Label()
        article_label.config(text = f"Name: {name.title()}\nTitle: {art}\nDescription: {des} \n\nName: {name1.title()}\nTitle: {art1}\nDescription: {des1}\n\nName: {name2.title()}\nTitle: {art2}\nDescription: {des2}", width = 45, wraplength = 320, font = ("Courier" ,9,"normal"), highlightthickness = 2, highlightbackground = "black")
        article_label.grid(column = 3, row = 2, columnspan = 3, rowspan = 6, pady = 10, padx = 10)

button = tkinter.Button(text = "Get Stocks", command = get_stocks)
button.config(bg = "white", font = ("Courier", 10, "bold"))
button.grid(column = 1, row = 2, columnspan = 2)



window.mainloop()