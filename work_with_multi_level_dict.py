#a new new library for you, just like turtle or math, it is a standard python library
#it is used for pretty print, in this case we use it to print a multi-level dict
import pprint

def daily_earning_spening_dictionary(file_path):
    transaction_file = open(file_path, "r")
    #initialize the dict
    daily_summary = {}

    #loop through each line in the file, you knew this, I ciopied from your code
    for line in transaction_file:
        #we know each line has three fields, so we split them into three variables and give each a meaningful name
        (person, date, amount) = line.split(',')

        #first you to to check whether the person is in the dict, and handle different
        if person in daily_summary: #the person is already in the dict
            #next we need to check whether that date already exists for that person
            if date in daily_summary[person]: 
                #notice the syntax we used to reference an element in a dict of dict? pretty straight forward right?
                #the date already exist, so we add
                daily_summary[person][date] += float(amount) 
            else:
                #the date is not there, so this is the first time this date appeared for this person
                #we can not add, instead just initialize it
                daily_summary[person][date] = float(amount) 
        #look at the matching if above, this else means this person is not in the dict, so we initialize
        else:
            daily_summary[person] = {date: float(amount)}
    #always a good behabit to close what you opened, look professional
    transaction_file.close()
    #return the dict we formed
    return daily_summary

#get the dict back from the function call and saved it to a variable
daily_summary = daily_earning_spening_dictionary("data/transactions.txt")
#initialize the pretty printer, set the indent to 4, you will see what it does when you run the program
pretty_printer = pprint.PrettyPrinter(indent=4)
#actually print the dict
pretty_printer.pprint(daily_summary)

#this is the usual print, just want to show you the difference compared to pretty print
#pretty printer is much better right? help you to actually understand what is in the dict
print(daily_summary)    