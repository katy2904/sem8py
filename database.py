
def into_db(file, data):
    with open(file, 'a') as f:
        f.write(data)

def from_db(file):
    with open(file, 'r') as f:
        data = f.read().split(',')
    return data