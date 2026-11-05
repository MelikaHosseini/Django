from store.models import Bookable
import datetime
class Reciept():
    def __init__(self, request):
        self.event = request.event

        reciept = self.event.get('session_key')

        if 'session_key' not in request.session:
            booking = self.event['session_key'] = {}

        self.receipt = receipt   

    def add(self, booking, quantity):
            booking_id = str(booking.id)

            if booking_id in self.reciept:
                 pass
            else:
               #   self.cart[booking_id] = {'price': str(booking.price)}
               self.reciept[booking_id] = int(booking_id)  
            self.session.modified = True     

    def __len__(self):
         return len(self.cart)  

    def get_bookings(self):
         booking_ids = self.receipt.keys()
         bookings = Receipt.objects.filter(id__in=booking_ids)  
         return bookings 
     
    def update(self, booking):
         booking_id = str(booking)
         receipts_list = self.receipt
         receipts_list[booking_id] =  booking_id
         self.event.modified = True

         updated = self.cart
         return updated
