# Chalao:  python add_more_data.py <extra_yolo_folder> [pothole_class_id]
# Extra YOLO dataset (images + .txt labels) ko train/val/test me 70/15/15 baant kar jod deta hai.
# Naam clash na ho isliye file names ke aage prefix lagta hai. Sirf pothole class ki lines rakhta hai (class 0 bana kar).
import sys, random
from pathlib import Path
if len(sys.argv) < 2:
    sys.exit("Usage: python add_more_data.py <extra_yolo_folder> [pothole_class_id]")
src, cls = Path(sys.argv[1]), (sys.argv[2] if len(sys.argv) > 2 else '0')
dst = Path('sadak_project/data'); tag = src.name.replace(' ', '_')[:12]
imgs = [p for p in src.rglob('*') if p.suffix.lower() in ('.jpg', '.jpeg', '.png')]
pairs = []
for im in imgs:
    for lb in (im.with_suffix('.txt'),
               im.parent.parent/'labels'/(im.stem + '.txt'),
               im.parent.parent.parent/'labels'/im.parent.name/(im.stem + '.txt')):
        if lb.exists():
            pairs.append((im, lb)); break
random.Random(7).shuffle(pairs); n = len(pairs); a, b = int(.7*n), int(.85*n)
for k, items in {'train': pairs[:a], 'val': pairs[a:b], 'test': pairs[b:]}.items():
    for im, lb in items:
        name = f'{tag}_{im.stem}'
        lines = [l for l in lb.read_text().splitlines() if l.split() and l.split()[0] == cls]
        (dst/k/'images'/(name + im.suffix)).write_bytes(im.read_bytes())
        (dst/k/'labels'/(name + '.txt')).write_text('\n'.join('0 ' + ' '.join(l.split()[1:]) for l in lines))
print('Joda gaya:', n, 'images')
