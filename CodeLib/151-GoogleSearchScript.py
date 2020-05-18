import webbrowser
search_terms = ["list comprehension","Aston Kucher", "You've Got Mail", "Shark Tank"]

for term in search_terms:
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open_new_tab(url)
