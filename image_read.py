from skimage import io
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import square
from skimage.color import label2rgb, rgb2gray

def get_sequence(filename):
    image = io.imread(filename)
    image = rgb2gray(image)
    b_and_w = image > threshold_otsu(image)
    labeled = label(b_and_w)
    bar_dims = [r.bbox for r in regionprops(labeled)]
    bar_dims.sort(key=lambda x: x[1], reverse=False)
    spotify_logo = bar_dims[0]
    max_height = spotify_logo[2] - spotify_logo[0]
    sequence = []
    for bar in bar_dims[1:]:
        height = bar[2] - bar[0]
        ratio = height / max_height
        if ratio < 0.25:
            sequence.append(0)
        elif ratio < 0.33:
            sequence.append(1)
        elif ratio < 0.46:
            sequence.append(2)
        elif ratio < 0.5625:
            sequence.append(3)
        elif ratio < 0.677:
            sequence.append(4)
        elif ratio < 0.8:
            sequence.append(5)
        elif ratio < 0.9:
            sequence.append(6)
        elif ratio < 1.1:
            sequence.append(7)
        else:
            raise ValueError('ratio is too high')
    return sequence