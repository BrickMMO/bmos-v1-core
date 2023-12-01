
data = {}

def load():

    global data

    try:
        f = open(".config", "r")
    except:
        print("Error: .env file does not exist")

    for line in f:

        line = line.split('=')

        if len(line) > 1:

            data[str(line[0])] = str(line[1]).strip()

            # exec("global " + str(data[0]))
            # exec("" + str(data[0]) + " = \"" + str(data[1]).strip() + "\"")

def get(key):

    global data

    if key in data:

        return data[key]

    else:

        return ''

def set(key, value):

    global data

    data[key] = value
    write()

def unset(key, value):

    global data

    if key in data:

        data.pop(key)
        write()

def write():

    global data

    try:
        f = open(".config", "w")
    except:
        print("Error: .env file does not exist")

    for key, value in data.items():

        f.write(key + "=" +  value)

load()
