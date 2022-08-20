from collight.models.customer import Customer
from collight.models.order import Order

class OrderTools:

    @staticmethod
    def AgeFilter(item):        
        aux = Order.objects.all().filter(items=item)
        total = len(aux)
        counter = {
            'até 18':0,
            'entre 18 e 30':0,
            'entre 30 e 45':0,
            'mais de 45':0,
        }
        
        for _ in aux:
            if int(_.customer.age) < 19:
                counter['até 18'] += 100/total
            elif int(_.customer.age) < 31 :
                counter['entre 18 e 30'] += 100/total
            elif int(_.customer.age) < 46:
                counter['entre 30 e 45'] += 100/total
            else:
                counter['mais de 45'] += 100/total
                
        return  
    

            
    
    


