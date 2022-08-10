#
# Checks the input data to make sure it is valid
#
#

import os

possibleArguments = ['-a'
        ,'--all'
        ,'--color'
        ,'-d'
        ,'-F'
        ,'-i'
        ,'-l'
        ,'-la'
        ,'-lh'
        ,'-ls'
        ,'-r'
        ,'-R'
        ,'-s'
        ,'-S'
        ,'-t'
        ,'-X']

#
# Makes sure that the input path is actually
# a path on the system and not anything else to avoid code injection or invalid paths.
#
def isValidPath(data):
    if not 'path' in data:
        return (False, "There is no path key in the input JSON", 400)
    if not os.path.isdir(data['path']):
        return (False, "The path you have entered " +data['path'] + " is not a valid path on this system.", 400)
    return (True, '')

#
# Checks the argument field that its valid.
# Only accept arguments which are in the list in order to
# avoid any code injection or such hacks.
#
def isValidArgument(data):
    if not 'arguments' in data:
        return (True, '')
    if not isinstance(data['arguments'], list):
        return (False, 'arguments key in the JSON does not point to a list',400)
    for arg in data['arguments']:
        if not arg in possibleArguments:
            return (False, 'one of the input arguments \'' + arg + '\' were not one of the arguments allowed for ls.', 400)
    return (True,'')

#
#Method for all data validation
#
def inputValidation(data):
    pathValidation = isValidPath(data)
    if not pathValidation[0]:
        return pathValidation
    return isValidArgument(data)
