from .Cart import CART

def cart(request):
    return{'cart':CART(request)}