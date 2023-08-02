from application.salary import calculate_salary
from application.db.people import get_employees

import datetime
import pytz


if __name__ == '__main__':
    
   time_zone = pytz.timezone('Asia/Vladivostok')
   date_now = datetime.datetime.now(time_zone)
   print(f'Текущая дата и время {date_now}')
    
   while True:

      command = input ("Введите команду:")
      
      if command == '1':
          print (calculate_salary(command))
          
      elif command == '2':
          print (get_employees (command))
         
      elif command == '3':    
          break