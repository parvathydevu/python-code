class Car(object): 
      ## double underscore is dunder  variables
      #A constructor is a data or methods inside __ init__ method automatically execute the code when it calls.
      #Constructor
      def __init__(self, brand, model, year, mileage=0):
            #mileage is odometer value-Km driven
            self.brand= brand
            self.model=  model
            self.year= year
            self.mileage= mileage
        #member function
      def drive(self, distance):
            self.mileage+=distance
      def display_Info(self):
            print("\n")
            print("-"*80)
            print("Brand of car:".ljust(20),'|',self.brand)
            print("model of car:".ljust(20),'|',self.model)
            print("year:".ljust(20),'|',self.year)
            print("Mileage of car:".ljust(20),'|',self.mileage) 

if __name__=="__main__":
      c1= Car("Toyota", "Corolla", "2020")
      c1.drive(400)
      c1.display_Info()

