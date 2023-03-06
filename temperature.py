class Temperature:
    def __init__(self,celcius,fahr):
        self.celcius=celcius
        self.fahr=fahr
    def convertFahrenheit(self):
        fans=(self.celcius*9/5)+32
        print(self.celcius,"celcius=",fans,"fahrenheit")
    def convertCelcius(self):
        cans=(self.fahr-32)*5/9
        print(self.fahr,"fahrenheit=",cans,"celcius")
celcius=float(input("Enter the temperature in celcius: "))
fahr=float(input("Enter the temperature in fahrenheit: "))
ct=Temperature(celcius,fahr)
ct.convertFahrenheit()
ct.convertCelcius()