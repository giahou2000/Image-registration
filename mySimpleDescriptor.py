def myLocalDescriptor(I, p, rhom, rhoM, rhostep, N):

    height, width = I.shape[:2]

    # watch out for points p near the vertices of the image
    if p[0] < rhoM:
        d = []
    elif p[0] > (width - rhoM):
        d = []
    elif p[1] < rhoM:
        d = []
    elif p[1] > height - rhoM:
        d = []
    else:
        d = [0, 3, 4]

    return d