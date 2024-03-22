from abc import ABC,abstractmethod 

class PaymentGateway(ABC):
    @abstractmethod
    def payment_transaction(self,amount):
        pass 

class PayPal(PaymentGateway):
    def payment_transaction(self, amount):
        return f"Processing payment of ${amount} via PayPal."
    
class Stripe(PaymentGateway):
    def payment_transaction(self, amount):
        return f"Processing payment of ${amount} via Stripe."

class RazorPay(PaymentGateway):
    def payment_transaction(self, amount):
        return f"Processing payment of ${amount} via Razorpay." 
    
# factory class 
    
class PaymentMethod:
    def paymentapi(self,payemntgateway):
        if payemntgateway=='paypal':
            return PayPal()
        elif payemntgateway=='stripe':
            return Stripe()
        elif payemntgateway=='razorpay':
            return RazorPay()
        else:
            ValueError('invalid option')

obj=PaymentMethod()
payment_gateway_type=input('Enter the gateway type')
amt=int(input('enter the amount'))

gateway=obj.paymentapi(payment_gateway_type)
print(gateway.payment_transaction(amt)) 
s
