import pandas as pd

import matplotlib.pyplot as plt

lwd=pd.read_csv("notes.csv")


print("Nigeria is a country on the west side of Africa. It has many natural landmarks and wildlife reserves. It inhabits more than 250 ethnic groups and has more than 500 speaking languages, including English. \n")

input("Press return to continue! \n")

print("Literacy is the ability to read and write. But is a common problem in the country of Nigeria. According to The United Nations Children’s Fund (UNICEF) it is said that '75 percent of Nigerian children, aged between seven and 14 years, cannot read a simple sentence or solve a basic mathematics problem.'' \n")

input("Press return to continue \n")

print("This must be considered as a national issue because children who cannot read or write will end up failing making efficient decisions or understanding simple concepts that they may face in their lives. \n")

print("The national literacy rate in Nigeria is 48.9. The male literacy rate is 55.2, while the female literacy rate is 42.5. (source-Kingmakers Africa) \n")

print("Now, what are some ways to solve this issue? \n")

input("Press return to continue! \n")

print("Promotin literacy programs in schools in Nigeria.")
print("Fostering the love of learning in the children at schools.")
print("Using technology to enhance and promote learning. ")
print("Addressing the factors that contribute to low literacy rates.\n")

print("There are so many ways to combat illiteracy in many countries including Nigeria, and advocating for education to the people.")

# this is for the figure size
plt.figure(figsize=(8, 6))  


# Plotting the national literacy rate
plt.bar('Total', lwd['literacy_rate_total'], color='blue', label='Total')


# Plotting male literacy rate
plt.bar('Male', lwd['literacy_rate_male'], color='green', label='Male')


# Plotting female literacy rate
plt.bar('Female', lwd['literacy_rate_female'], color='red', label='Female')

plt.title('Literacy Rates in Nigeria (2023)')
plt.ylabel('Literacy Rate (%)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

