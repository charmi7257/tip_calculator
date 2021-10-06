
print ("Welcome to the tip calculator")
bill = float(input ("What was the total bill? $"))
tip_p = int(input ("what percentage tip would you like to give? 10, 12, 15? "))
n = int(input ("how many people to split the bill? "))
tip = (bill * tip_p) / 100
total = bill + tip
Pay = total / n 
Pay = (bill / n) * (1 + tip_p/100) 
Pay = "{:.2f}".format(Pay)
print (f"Each person has to pay : ${Pay}")