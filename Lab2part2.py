def calculate_bmi (height, weight):
    print ("Height = ", height)
    print ("Weight = ", weight)
    BMI = (weight) / (height**2)
    print ("Your BMI IS:", BMI)
    if (BMI<=18.5):
        print ("YOU skinny ahh")
    elif(BMI<=24.5):
        print ("YOU normal ahh ")
    else:
        print ("FATTY PATTY")
calculate_bmi(weight =0, height=1.73)

