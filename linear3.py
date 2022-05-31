# ID-C181202
# Name-Umma Aymon

x = [39, 25, 29, 35, 32, 27, 37]
y = [37, 18, 20, 25, 25, 20, 30]
n = 7
sumOfx = sum(x)
sumOfy = sum(y)
mean_x = sumOfx / float(n)
mean_y = sumOfy / float(n)
#print(sumOfx)
#print(sumOfy)
sumOfxx = 0
sumOfxy = 0
for i in range(len(x)):
    sumOfxx += x[i] * x[i]
#print(sumOfxx)
for i in range(len(x)):
    sumOfxy += x[i] * y[i]
#print(sumOfxy)
up = 0.0
up = sumOfxy - ((sumOfx * sumOfy) / float(n))
down = 0.0
down = sumOfxx - ((sumOfx * sumOfx) / float(n))
b = 0.0
b = up / down
#print(b)
a = 0.0
a = mean_y - (b * mean_x)
#print(a)
#(b)	Predict the age of wife whose husband’s age in 45 years.
predicted_age = a + (b * 45)
#print(predicted_age)
print('Coefficients: a = %.3f, b = %.3f' % (a, b))
print('Predicted Age: y = %.2f years' % (predicted_age))
