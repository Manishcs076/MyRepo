def TOH(nod,Startpeg = 1, Endpeg = 3):
    if nod:
        TOH(nod-1,Startpeg, 6-Startpeg-Endpeg)
        print ("Move disk %d from %d to peg %d"%(nod,Startpeg,Endpeg))
        TOH(nod-1,6-Startpeg-Endpeg,Endpeg)
TOH(nod=4)