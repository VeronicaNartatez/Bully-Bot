#generates compliments

def GetPhrases():
    file = open("RandomPhrases.txt","r")

    readfile = file.read()

    return readfile.split("\n")



    
