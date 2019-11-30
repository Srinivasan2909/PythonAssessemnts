f=open("C:\\Users\\ssrinivas209\\Desktop\\Phython\\Python-Assessements\\day3-Assessements\\BreakingintochunksAssingment\\imagechunk.jpg", "rb")
chunk=1024
i=1
while True:
    data=f.read(chunk)
    if not data:
        break
    fo=open("chunk"+str(i)+'.jpg','wb')
    i += 1
    fo.write(data)
    fo.close()
