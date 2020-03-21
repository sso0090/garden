# AUTOGENERATED! DO NOT EDIT! File to edit: nbs_dev/01_data.ipynb (unless otherwise specified).

__all__ = ['path', 'path_img', 'train_fnames', 'test_fnames', 'get_items', 'data', 'get_x', 'get_y']

# Cell
from fastai2.vision.all import *

# Cell
from utils import *

# Cell
path = root + "/data"

# Cell
path_img = Path(path+'/jpeg224x224')

# Cell
train_fnames = get_files(path_img/'train', extensions='.tfrec')
test_fnames = get_files(path_img/'val', extensions='.tfrec')

# Cell
data = []
for name in train_fnames+test_fnames:
  r = Reader(str(name), unpack_sample)
  for sample in r:
    data.append([sample['image'][0], sample['class'][0]])

get_x = lambda o: PILImage.create(io.BytesIO(o[0]))
get_y = lambda o: o[1]

def get_items(_): return data