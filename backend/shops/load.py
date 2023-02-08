fp = r"C:\Users\USER\Desktop\laborratehero\GIS\shops_test.csv"
import csv
from .models import Shop
from django.contrib.gis.geos import GEOSGeometry


with open(fp, 'r') as file:
  csvreader = csv.reader(file)
  i = 0
  for row in csvreader:
    if row[0] == 'WKT':
      print(row)
      i += 1
    else:
      s = Shop.objects.get(id=i)
      los_angeles_epsg = 26911
      s.geom_m = s.geom.transform(los_angeles_epsg, clone=True)
      s.save()
      print(s.geom_m)
      i += 1
      # a = Shop(name=row[4], lat=round(float(row[2]), 2),
      #           lon=round(float(row[3]), 2) ,geom=row[0],
      #            geom_m=GEOSGeometry(f'SRID=26911;{row[0]}'))
      # print(a.geom, a.geom_m)
      # a.save()

# fp = r"C:\Users\USER\Desktop\laborratehero\GIS\us_zipcodes.csv"
# import csv
# from .models import ZipCodes
# from django.contrib.gis.geos import GEOSGeometry, Point

# with open(fp, 'r') as file:
#   data = csv.reader(file)
#   for row in data:
#     if row[0] == 'ZIP':
#       continue
#     else:
#       x=float(row[2])
#       y=float(row[1])
#       x = round(x, 6)
#       y= round(y,6)
#       point = Point(x=x, y=y, srid=4326)
#       los_angeles_srid = 26911
#       point.transform(los_angeles_srid)
#       z = ZipCodes(ZIP=row[0],
#       lat=row[1], lon=row[2], geom=point)
#       z.save()
#   print('done')