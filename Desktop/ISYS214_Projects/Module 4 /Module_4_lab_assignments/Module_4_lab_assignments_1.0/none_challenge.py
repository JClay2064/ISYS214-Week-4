def is_year_leap(year):
      if(year % 4 == 0):
            if(year % 100 == 0):
                  if(year % 400 == 0):
                        return True
                  else:
                        return False
            else:
                  return True
      else:
            return False
            


# Checks if the month is between 1 and 12 
# (or) (year) is a positive number
def days_in_month(year, month):
      if month < 1 or month > 12 or year < 1:
            return None




def day_of_year(year, month, day):
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))