# A simple python script that allows the user to convert Celsius to Fahrenhit or Vise-Versa



choice = input("Will you be converting\n1.) C - F\nor\n2.) F - C\n >> ")

# Allow for choice of F-C or C-F
if choice == 1:
   metric_temp = (float(input("Enter the temp in celsius: ")))
   imper_temp = (1.8 * metric_temp) + 32
   print ('Fahrenheit:', imper_temp)

elif choice == 2:
    imper_temp = float(input("Enter the temp in fahrenheit: "))
    metric_temp = (imper_temp - 32) / 1.8
    print ('Celsius:', metric_temp)
