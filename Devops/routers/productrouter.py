from fastapi import APIRouter , Response
from controller.productcontroller import create_products_controller,get_products_all_controller,get_products_controller,updateProducts_controller,deleteProducts_controller
from model.productModel import Product

prouter = APIRouter(
    prefix="/products",
    tags = ["products"]
)

@prouter.post('/postproduct')
async def create_products(product:Product , response : Response):
    return await create_products_controller(product , response)
# @prouter.post('/postproduct')
# def create_products(product:Product , response : Response):
#     return create_products_controller(product , response)

@prouter.get('/getall')
async def get_products_all(response : Response):
    return await get_products_all_controller(response)


@prouter.get('/getproduct/{productid}')
async def get_products(productid:str,response : Response):
    return await get_products_controller(productid , response)

@prouter.put('/updateproducts/{productid}')
def updateProducts(productid,product :  Product,response : Response):
    return updateProducts_controller(product, response,productid)

@prouter.delete('/updateproducts/{productid}')
async def deleteProucts(productid,product :  Product,response : Response):
    return await deleteProducts_controller(product, response,productid)
