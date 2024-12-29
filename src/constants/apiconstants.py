#apiConstants : class where we Keep all the endpoints
#sstatic method:which can be directly called without making an object of the class

class apiConstants:

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod

    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"
    
    def url_patch_put_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)