import webbrowser

def search(title):
    result = title
    print(f"you are searching for {result}")
    webbrowser.open(title)
    return result
