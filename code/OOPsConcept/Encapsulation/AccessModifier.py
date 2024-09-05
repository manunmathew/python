class A:
    def data_members(self,name,phone,salary):
        self.name = name    # public
        self._phone = phone # protected
        self.__salary = salary # private

    def display (self): # public method

    def _display2(self): # protected

    def __display3(self): # private 
