from fastai.vision import *

folder = 'soccer'
file = 'urls_soccer.csv'

path = Path('data/sports')
dest = path/folder
dest.mkdir(parents=True, exist_ok=True)

folder = 'tennis'
file = 'urls_tennis.csv'

path = Path('data/sports')
dest = path/folder
dest.mkdir(parents=True, exist_ok=True)

folder = 'football'
file = 'urls_football.csv'

path = Path('data/sports')
dest = path/file
dest.mkdir(parents=True, exist_ok=True)

path.ls()


# download images
#classes = ['soccer', 'tennis', 'football']
#download_images(path/file, dest, max_pics=200)

# If you have problems download, try with `max_workers=0` to see exceptions:
#download_images(path/file, dest, max_pics=20, max_workers=0)

#for c in classes:
#    print(c)
#    verify_images(path/c, delete=True, max_size=500)

