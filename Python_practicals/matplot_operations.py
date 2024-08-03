import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6]
y = [10,20,15,30,35,20]

# line plot
plt.plot(x,y,marker="+")
plt.xlabel("Month")
plt.ylabel("Salary in K")
plt.title("saurabh salary")
plt.show()

# Bar plot
plt.bar(x,y,color="red")
plt.xlabel("Month")
plt.ylabel("Salary in K")
plt.title("saurabh salary")
plt.show()

# histogram
ages = [1,1,2,3,3,5,7,8,9,10,
        10,11,11,13,13,15,16,
        17,18,18,18,19,20,21,
        21,23,24,24,25,25,25,
        25,26,26,26,27,27,27,
        27,27,29,30,30,31,33,
        34,34,34,35,36,36,37,
        37,38,38,39,40,41,41,
        42,43,44,45,45,46,47,
        48,48,49,50,51,52,53,
        54,55,55,56,57,58,60,
        61,63,64,65,66,68,70,
        71,72,74,75,77,81,83,
        84,87,89,90,90,91,]
b = [10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins=b,edgecolor='r',bottom=5,histtype="step",rwidth=0.1)
plt.xlabel("age")
plt.ylabel("no. of representatives")
plt.title("age distribution")
plt.show()

# pie chart
manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Others']
market_share = [30, 25, 18, 12, 15]
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']
plt.pie(market_share, labels=manufacturers, colors=colors, autopct='%1.1f%%')
plt.title('Smartphone Market Share')
plt.show()

# scatter plot
study_hours = [2, 3, 1, 4, 3, 5, 2, 6, 5, 7]
exam_scores = [65, 75, 60, 80, 70, 85, 70, 90, 88, 92]
plt.scatter(study_hours, exam_scores, c='green', marker='o', label='Student Data')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Study Hours vs. Exam Scores')
plt.legend()
plt.grid(True)
plt.show()

# subplot method-1(shows multiple graphs in a plot)
students = ['Jhon', 'Smith', 'Marry', 'Rose', 'Devid']
math_scores = [85, 92, 78, 88, 90]
science_scores = [76, 88, 92, 80, 78]
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].bar(students, math_scores, color='b')
axs[0].set_title('Math Scores')
axs[0].set_xlabel('Students')
axs[0].set_ylabel('Score')
axs[1].bar(students, science_scores, color='g')
axs[1].set_title('Science Scores')
axs[1].set_xlabel('Students')
axs[1].set_ylabel('Score')
plt.tight_layout()
plt.show()

# subplot method-2
x = [10,20,30,40,50,60,70,80,90]
y = [1,2,3,4,5,6,7,8,9]
plt.subplot(2,2,1)
plt.plot(x,y,color="g")

plt.subplot(2,2,2)
plt.pie([1],colors="r") #[1] is to pass a blank pie circle

plt.subplot(2,2,3)
a = [20,40,60]
plt.pie(a)

plt.subplot(2,2,4)
a1 = ["a","b","c","d"]
a2 = [20,40,60,80]
plt.bar(a1,a2)

plt.show()

# Adding general text
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y)
plt.title('plot with general text')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.text(2,8,'language',fontsize=10,color='white', bbox=dict(facecolor='red'))
plt.annotate("Java", xy=(4, 7), xytext=(2, 10),arrowprops=dict(facecolor='yellow', shrink=0.1), fontsize=12, color='red')
plt.legend(["Java"], loc=5, facecolor="yellow", edgecolor="red", framealpha=0.9, shadow=True)
plt.show()

# xlim and ylim are used to set the limits of x and y axis
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y)
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()

# saving figure
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y)
plt.title('sample plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('sample_plot.png')
plt.show()