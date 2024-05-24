from smartphone import Smartphone

s1=Smartphone("Apple", "iPhone 14 Pro", "+79162345678")
s2=Smartphone("Samsung", "Galaxy S23 Ultra", "+79991234567")
s3=Smartphone("Xiaomi", "Redmi Note 12 Pro", "+79129876543")
s4=Smartphone("OPPO", "Find X6", "+79956543210")
s5=Smartphone("OnePlus", "OnePlus 11", "+79387418562")

catalog = [ s1, s2, s3, s4, s5]

for s in catalog:
    print(f"<{s.pBrand}> - <{s.pModel}>. <{s.pNumber}>")