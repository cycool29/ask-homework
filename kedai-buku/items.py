class BukuRujukan:
    name = "Buku Rujukan"
    price = 15
    code = 8878698
    
class Pensil:
    name = "Pensil"
    price = 3
    code = 8878699
    
class Pembaris:
    name = "Pembaris"
    price = 2
    code = 8878700
    
class Pemadam:
    name =  "Pemadam"
    price = 3
    code = 8878701

class KadManila:
    name = "Kad Manila"
    price = 1
    code =  8878702
    
class Peta:
    name = "Peta"
    price = 5
    code = 8878703
    
class BukuLatihan:
    name = "Buku Latihan"
    price = 10
    code = 8878704

class Pen:
    name = "Pen"
    price = 4
    code = 8878705

class KotakPensil:
    name = "Kotak Pensil"
    price = 5
    code = 8878706
        

def check_item(code):
    for item in BukuRujukan, Pensil, Pembaris, Pemadam, KadManila, Peta, BukuLatihan, Pen, KotakPensil:
        if item.code == code:
            return item.price, item.name