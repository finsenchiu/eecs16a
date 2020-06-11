def testing(H, H_Alt):
  
    htest = ''
    halttest = ''
    if H.shape != (30*40, 30*40):
        htest = 'H shape is incorrect'
    if H_Alt.shape != (30*40, 30*40):
        halttest = 'H_Alt shape is incorrect, please fix'
    print(htest)
    print(halttest)
    if not htest and not halttest:
        print('Your matrix shapes are correct.')
