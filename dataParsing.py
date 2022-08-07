import os 
def isValidPath(data):
    if not 'path' in data:
        return (False, "There is no path argument in the input", 400)
    if not os.path.isdir(data['path']):
        return (False, "The path you have entered " +data['path'] + " is not a valid path on this system.", 400)
    return (True, '')
    
