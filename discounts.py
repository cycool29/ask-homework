class VIP888:
    name = "VIP888"
    value = 5
    
class VIP999:
    name = "VIP999"
    value = 10
    
    
def check_discount(code):
    for item in VIP888, VIP999:
        if item.name == code:
            return item.value