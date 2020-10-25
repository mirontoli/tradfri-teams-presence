from O365.utils import ApiComponent

class Presence(ApiComponent):
    _endpoints = {'my_presence': '/presence'}

    def __init__(self, *, parent=None, con=None, **kwargs):
        # connection is only needed if you want to communicate with the api provider
        self.con = parent.con if parent else con
        protocol = parent.protocol if parent else kwargs.get('protocol')
        main_resource = 'ME' #parent.main_resource

        super().__init__(protocol=protocol, main_resource=main_resource)

    def get_my_presence(self):

        # self.build_url just merges the protocol service_url with the enpoint passed as a parameter
        # to change the service_url implement your own protocol inherinting from Protocol Class
        url = self.build_url(self._endpoints.get('my_presence'))  

        my_params = {}

        response = self.con.get(url, params=my_params)  # note the use of the connection here.
        # TODO error handling
        data = response.json()
        availability = data.get('availability')
        print(availability)
        return availability
