import os,random, time

pullData = open("sampleText.txt","w")

def _writin_():  
    start = time.time()
    while True:
        i = random.randint(0,69)
        y = random.randint(0,69)
        pullData.write(str(i)+","+str(y)+os.linesep)
        try:
            end = time.time()
            delta = end-start
            if delta>10:
                return _writin_()

_writin_()