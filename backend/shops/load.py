# fp = r"C:\Users\USER\Desktop\laborratehero\GIS\shops_test.csv"
import csv
from .models import Shop, ZipCodes
from django.contrib.gis.geos import Point


def load_shop(fp):
  with open(fp, 'r') as file:
    data = csv.reader(file)
    i = 0
    for row in data:
      if row[0] == 'id':
        print(row)
      else:
        name=row[1]
        lat_y, lon_x = float(row[2]), float(row[3])
        loc_4326 = Point(x=lon_x, y=lat_y, srid=4326)
        loc_1324 = loc_4326.transform(3857, clone=True) # EPSG:3857 is web mercator
        s = Shop(name=name, lat=lat_y, lon=lon_x , geom=loc_4326, geom_m=loc_1324)
        s.save()
        print(s.geom_m)

def load_zip_codes(fp):
  with open(fp, 'r') as file:
    data = csv.reader(file)
    for row in data:
      if row[0] == 'ZIP':
        continue
      else:
        x=float(row[2])
        y=float(row[1])
        x = round(x, 6)
        y= round(y,6)
        point = Point(x=x, y=y, srid=4326)
        point.transform(3857)
        z = ZipCodes(ZIP=row[0],
        lat=row[1], lon=row[2], geom=point)
        print(z)
        z.save()
    print('done')