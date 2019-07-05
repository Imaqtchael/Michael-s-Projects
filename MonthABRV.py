months_abv = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
month_inp = input("Your month:\n")
while month_inp not in months_abv:
    month_inp = input("Please type your month!: ")
print(months_abv.get(month_inp))