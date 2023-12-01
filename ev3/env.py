
data = {}

def load():

    global data

    try:
        f = open(".env", "r")
    except:
        print("Error: .env file does not exist")

    for line in f:

        line = line.split('=')

        if len(line) > 1:

            data[str(line[0])] = str(line[1]).strip()

def get(key):

    global data

    if key in data:

        return data[key]

    else:

        return ''

load()
