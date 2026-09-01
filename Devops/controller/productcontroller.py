from fastapi import Response
from model.productModel import Product
from dbConnect import productCollection
from bson import ObjectId

products = []
id = 0


async def create_products_controller(product:Product , response : Response):
    try:
        result = await productCollection.insert_one(product.dict())
        product.id = str(result.inserted_id)
        return{
            "message":"product created Successfully",
            "product":product}
    except Exception as e: #exeption nu name aapyu k exeption as 'e' km k exeption bau type na aave 'e' ni jagyae kai pan name aapi sakay
        print(e)
        response.status_code = 201
        return{"message":str(e),'isSuccess': False}

async def get_products_all_controller(response : Response):
    try :
        productss = []
        async for product in productCollection.find():
            product["id"] = str(product["_id"])
            productss.append(Product(**product))
            print('Data-->',productss)
        return{"message":"product get Successfully",'Products' : productss}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{
            "message" : "Error fetching products",
            "isSuccess": False
        }


    
async def get_products_controller(productid:str,response : Response):
    try:
        response.status_code = 200
        product = await productCollection.find_one({"_id": ObjectId(productid)})
        product["id"] = str(product["_id"])
        if product:
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

async def deleteProducts_controller(productid:str,response : Response):
    try:
        result = await productCollection.delete_one({"_id":ObjectId(productid)})
        if result.deleted_count==1:
            response.status_code=200
            return{"message":"Product deleted Successfully","isSuccess":True}
        response.status_code = 404
        return{"message":"Product not found","isSuccess":True}
    except Exception as e :
        print(e)
        response.status_code = 500
        return{"message":"Error deleting product","isSuccess":True}