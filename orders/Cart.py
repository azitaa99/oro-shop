from products.models import Product

cart_session_id='cart'

class CART:
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(cart_session_id)
        if not cart:
            cart=self.session[cart_session_id]={}
        self.cart=cart

    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.values():
            item['total_price']=int(item['price'])*item['quantity']
            yield item
    
    def save(self):
        self.session.modified=True

    def add(self,product,quantity):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.price)}
        self.cart[product_id]['quantity']+=quantity
        self.save()

    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[cart_session_id]
        self.save()


