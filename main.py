import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV file
lwd = pd.read_csv("notes.csv")

# Information printout and user interaction
print("Nigeria is a country on the west side of Africa. It has many natural landmarks and wildlife reserves. It inhabits more than 250 ethnic groups and has more than 500 speaking languages, including English. \n")

input("Press return to continue! \n")

print("Literacy is the ability to read and write, but it is a common problem in the country of Nigeria. According to The United Nations Children’s Fund (UNICEF), '75 percent of Nigerian children, aged between seven and 14 years, cannot read a simple sentence or solve a basic mathematics problem.' \n")

input("Press return to continue \n")

print("This must be considered a national issue because children who cannot read or write will struggle to make efficient decisions or understand simple concepts they may face in their lives. \n")

print("The national literacy rate in Nigeria is 48.9%. The male literacy rate is 55.2%, while the female literacy rate is 42.5%. (source: Kingmakers Africa) \n")

print("Now, what are some ways to solve this issue? \n")

input("Press return to continue! \n")

print("1. Promoting literacy programs in schools in Nigeria.")
print("2.Fostering the love of learning in children at schools.")
print("3.Using technology to enhance and promote learning.")
print("4.Addressing the factors that contribute to low literacy rates.\n")

print("There are many ways to combat illiteracy in countries including Nigeria, and advocating for education is crucial.")

# Preparing data for plotting
categories = ['Total', 'Male', 'Female']
values = [lwd['literacy_rate_total'][0], lwd['literacy_rate_male'][0], lwd['literacy_rate_female'][0]]
colors = ['blue', 'green', 'red']

# Plotting the literacy rates
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=colors)

plt.title('Literacy Rates in Nigeria (2023)')
plt.ylabel('Literacy Rate (%)')
plt.legend(['Total', 'Male', 'Female'])
plt.grid(True)

# Show plot
plt.show()
