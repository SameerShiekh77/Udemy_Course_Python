import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1500,2000,5000,1000]
# plt.plot(x,y)
# plt.show()

legend = ["January","Feburary","March","April"]
plt.xticks(x,legend)
# plt.plot(x,y)
# plt.show()


# bar chat
plt.bar(x,y)
plt.title("Monthly Income")
plt.ylabel("Sales in Pak")
plt.xlabel("Months")
plt.show()