class ProductObject:

    def __init__(self):
        self.data = {
            "product_id": 0,
            "stock_pcs": 0,
            "price": 0,
            "shop_id": '',
            "vip": 0,
        }


    def set_product_data(self, product_id, stock_pcs, price, shop_id, vip):
        self.data['product_id'] = product_id
        self.data['stock_pcs'] = stock_pcs
        self.data['price'] = price
        self.data['shop_id'] = shop_id
        self.data['vip'] = vip


    def get_product_data(self):
        return self.data
