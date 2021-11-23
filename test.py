import requests
import tkinter as tk


def getNews():
    api_key = "5d374ef51f894a239e419b28258803fe"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)

window = tk.Tk()
window.geometry("900x600")
window.title("Dan Diaconescu News")

button = tk.Button(window, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(window, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

window.mainloop()