import numpy as np

def test_masks_img2(H, H_Alt):

    errors = False
    if H.shape != (30*40, 30*40):
        errors = True
        print('H shape is incorrect: H.shape = {}'.format(H.shape))
    try:
        np.linalg.inv(H)
    except np.linalg.LinAlgError:
        errors = True
        print('H is not invertible')

    if H_Alt.shape != (30*40, 30*40):
        errors = True
        print('H_Alt shape is incorrect: H_Alt.shpae = {}'.format(H_Alt.shape))
    try:
        np.linalg.inv(H_Alt)
    except np.linalg.LinAlgError:
        errors = True
        print('H_Alt is not invertible')
    if (errors):
        print("\nPlease fix any errors before moving on.")
    else:
        print("H and H_Alt are the correct dimension and are both invertible. Proceed to the next step")
