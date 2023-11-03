


def record(urls):
    history = []
    urls_list = urls.split(' => ')
    for website in urls_list:
        if website  in history:
            history.remove(website)
        history.append(website)
    history.reverse()
    return history


def getHistory(History):
    if len(History) < 1:
        return ""
    websites_list = history[0]
    for i in range(1,len(history)):
        websites_list += (' => ' + history[i])

    return websites_list
    
urls_list = "msn.com => google.com => facebook.com => google.com"
history = record(urls_list)
print('urls_visited:', urls_list)
print('history:', getHistory(history))

        
    