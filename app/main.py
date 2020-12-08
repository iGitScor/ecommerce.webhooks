from fastapi import FastAPI

from domain.customer import WooCustomer
from service.transformer.customer import CustomerTransformer

app = FastAPI()

@app.post("/hook/v1/customer/create")
async def customer_create(customer: WooCustomer):
    apiCustomer = CustomerTransformer().transform(customer = customer)
    return {"apiCustomer": apiCustomer, "wooCustomer": customer}