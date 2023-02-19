# fp = r"C:\Users\USER\Desktop\laborratehero\GIS\shops_test.csv"
import csv
from .models import Shop, ZipCodes
from django.contrib.gis.geos import Point
import random

# python manage.py shell
# from shops.models import Shop
# from shops.load import load_shop
# (r"C:\Users\USER\Desktop\laborratehero\backend\faker_shops_tilder.csv")

def load_shop(fp):
  with open(fp, 'r') as file:
    data = csv.reader(file, delimiter='`')
    line_count = 0
    for row in data:
      if line_count == 0:
        print(row)
        line_count += 1
      else:
        line_count += 1
        business_name = row[1]
        lat_y = float(row[2])
        lon_x =  float(row[3])
        physical_address = row[4]
        business_phone = row[5][:10]
        body_sheet_metal = row[6]
        aluminum_body = row[7]
        refinish_labour = row[8]
        aluminum_structure = row[9]
        structural = row[10]
        carbon_fibre = row[11]
        frame = row[12]
        fibre_glass = row[13]
        mechanical = row[14]
        paint_materials = row[15]
        luxury_body = row[16]
        luxury_refinish = row[17]
        luxury_frame = row[18]
        luxury_mechanical = row[19]
        inside_storage = row[20]
        outside_storage = row[21]
        four_wheel_alignment = row[22]
        luxury_structural = random.randint(50, 250)
        pre_scan = row[23]
        post_scan = row[24]
        loc_4326 = Point(x=lon_x, y=lat_y, srid=4326)
        loc_1324 = loc_4326.transform(3857, clone=True) # EPSG:3857 is web mercator
        s = Shop(business_name=business_name,
                 lat=lat_y,
                lon=lon_x,
                physical_address = physical_address,
                business_phone = business_phone,
                body_sheet_metal = body_sheet_metal,
                aluminum_body = aluminum_body,
                refinish_labour = refinish_labour,
                aluminum_structure  = aluminum_structure,
                structural  = structural,
                carbon_fibre  = carbon_fibre,
                frame = frame,
                fibre_glass = fibre_glass,
                mechanical  = mechanical,
                paint_materials = paint_materials,
                luxury_body = luxury_body,
                luxury_refinish = luxury_refinish,
                luxury_frame  = luxury_frame,
                luxury_mechanical = luxury_mechanical,
                inside_storage  = inside_storage,
                outside_storage = outside_storage,
                four_wheel_alignment  = four_wheel_alignment,
                pre_scan  = pre_scan,
                post_scan   = post_scan,
                luxury_structural=luxury_structural,
                geom=loc_4326, 
                geom_m=loc_1324)
        s.save()
        print(f"{s.business_name} {s.post_scan}")

def load_postal_codes(fp):
  with open(fp, 'r') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
      if row[0] == 'POSTAL_CODE':
        continue
      else:
        x=float(row[5])
        y=float(row[4])
        x = round(x, 6)
        y= round(y,6)
        point = Point(x=x, y=y, srid=4326).transform(3857, clone=True)
        z = ZipCodes(ZIP=row[0], lat=y, lon=x, geom=point)
        print(z)
        z.save()
    print('done')