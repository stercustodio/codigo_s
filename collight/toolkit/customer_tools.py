from collight.models.customer import Customer
from collight.models.order import Order
from datetime import datetime, timedelta

class CustomerTools:

    @staticmethod
    def OrdersLog(customer):
        return Order.objects.all().filter(customer=customer).filter(created_at__gte = datetime.now()-timedelta(days=30))

    @staticmethod
    def PerfilCustomer(customer:Customer):
        
        orderslog = CustomerTools.OrdersLog(customer)

        amount = 0
        for _ in orderslog:
            amount += _.amount

            if amount < 10000:
                profile = 'brando'
            elif amount < 50000:
                profile = 'moderado'
            else:
                profile = 'agressivo'
        
        return profile
                


