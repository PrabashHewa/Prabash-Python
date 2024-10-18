study_benefits = float(input("Enter the amount of the study benefits: "))
index_raise = 1.17
raised_benefits = study_benefits * (1 + index_raise / 100)

print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be",raised_benefits ,"euros")
double_raised_benefits = raised_benefits * (1 + index_raise / 100)
print("and if there was another index raise, the study")
print("benefits would be as much as", double_raised_benefits ,"euros")