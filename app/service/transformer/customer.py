import string

class CustomerTransformer:
    def transform(self, customer):
        return {
            "firstname": customer.first_name if customer.first_name else None,
            "lastname": customer.last_name if customer.last_name else None,
            "email": customer.email if customer.email else None,
            "externalId": customer.id,
            "phone": self.normalizePhone(customer.billing.phone) if customer.billing and customer.billing.phone else None
        }

    def normalizePhone(self, phone: string) -> string:
        return phone.translate(str.maketrans('', '', string.whitespace))
