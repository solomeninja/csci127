#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  Solome' Spotts

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""

def monthString(n):
    if n == 1:
        return("January"):
      elif n == 2:
               return("February")
      elif n == 3:
               return("March")
      elif n == 4:
               return("April")
      elif n == 5:
               return("May")
      elif n == 6:
               return("June")
      elif n == 7:
               return("July")
      elif n == 8:
               return("August")
      elif n == 9:
               return("September")
      elif n == 10:
               return("October")
      elif n == 11:
               return("November")
      elif n == 12:
               return("December")
               
            

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
