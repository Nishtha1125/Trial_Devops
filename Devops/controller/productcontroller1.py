from fastapi import Response
from model.productModel import Product

products = []
id = 0

def get_products_all_controller(response : Response):
    print('Data-->',products)
    response.status_code = 200
    return{"message":"product get Successfully",'Products' : products}


def create_products_controller(product:Product , response : Response):
    global id 
    try:
        id +=1
        product.id = id
        products.append(product)
        response.status_code = 201
        return{
            "message":"product created Successfully",
            "product":product}
    except Exception as e: #exeption nu name aapyu k exeption as 'e' km k exeption bau type na aave 'e' ni jagyae kai pan name aapi sakay
        print(e)
        response.status_code = 201
        return{"message":str(e),'isSuccess': False}

def get_products_controller(productid:int,response : Response):
    try:
        response.status_code = 200
        for product in products:
            if product.id == productid:
                return{"message":product,'isSuccess': True}

        response.status_code = 404
        return{'message':'product Not found','isSuccess': False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{"message":'Error Fetching product','isSuccess': False}

def updateProducts_controller(productid,product :  Product,response : Response):
    try:
        idx = 0
        for index in range(0,len(products),1):
            if products[index] == productid:
                idx = index

        products[idx] = product
    except Exception as e:
        print(e)
        response.status_code = 500
        return{"message":'Error Fetching product','isSuccess': False}