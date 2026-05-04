from rich.console import Console
from rich_gradient import Gradient
import sys
import validator
import suggestions
import time

banner = '''
@@@@@@@    @@@@@@    @@@@@@    @@@@@@   @@@  @@@  @@@   @@@@@@   @@@@@@@   @@@@@@@  
@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@   @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@ 
@@!  @@@  @@!  @@@  !@@       !@@       @@!  @@!  @@!  @@!  @@@  @@!  @@@  @@!  @@@ 
!@!  @!@  !@!  @!@  !@!       !@!       !@!  !@!  !@!  !@!  @!@  !@!  @!@  !@!  @!@ 
@!@@!@!   @!@!@!@!  !!@@!!    !!@@!!    @!!  !!@  @!@  @!@  !@!  @!@!!@!   @!@  !@! 
!!@!!!    !!!@!!!!   !!@!!!    !!@!!!   !@!  !!!  !@!  !@!  !!!  !!@!@!    !@!  !!! 
!!:       !!:  !!!       !:!       !:!  !!:  !!:  !!:  !!:  !!!  !!: :!!   !!:  !!! 
:!:       :!:  !:!      !:!       !:!   :!:  :!:  :!:  :!:  !:!  :!:  !:!  :!:  !:! 
 ::       ::   :::  :::: ::   :::: ::    :::: :: :::   ::::: ::  ::   :::   :::: :: 
 :         :   : :  :: : :    :: : :      :: :  : :     : :  :    :   : :  :: :  :  
                                                                                    
                                                                                    
 @@@@@@@  @@@  @@@  @@@@@@@@   @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@                 
@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@                
!@@       @@!  @@@  @@!       !@@       @@!  !@@  @@!       @@!  @@@                
!@!       !@!  @!@  !@!       !@!       !@!  @!!  !@!       !@!  @!@                
!@!       @!@!@!@!  @!!!:!    !@!       @!@@!@!   @!!!:!    @!@!!@!                 
!!!       !!!@!!!!  !!!!!:    !!!       !!@!!!    !!!!!:    !!@!@!                  
:!!       !!:  !!!  !!:       :!!       !!: :!!   !!:       !!: :!!                 
:!:       :!:  !:!  :!:       :!:       :!:  !:!  :!:       :!:  !:!                
 ::: :::  ::   :::   :: ::::   ::: :::   ::  :::   :: ::::  ::   :::                
 :: :: :   :   : :  : :: ::    :: :: :   :   :::  : :: ::    :   : :   

'''

console = Console()
console.print(Gradient(banner, colors=['red', 'blue', 'purple']))

print('''Enter your password in the box and the script will:

1. Analyze the strength of your password.
2. Give you suggestions to do a better password.
3. Do a password entropy.
      
Remember:
      
* The password must be valid text.
* The password should not have spaces.
* Minimum length is 5, maximum length is 64.
* Extra: The password must have valid (printable) characters.
      ''')

def GetStrengthTable(password):
    suggest = suggestions.Suggest(password)
    suggest.append()
    suggest.show_table()

    print('Press Ctrl+C to exit...')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

def main():
    print('Enter a password to review.')
    try:
        while True:
            password = input('>>> ')
            validate = validator.Validate(password)
        
            if not validate.is_valid():
                print('''
Password is not valid:
    1. Must be valid text.
    2. Should not have spaces.
    3. Minimum length is 5, maximum length is 64.
    4. Must have valid characters.
                      ''')
            
            else:
                break
    except KeyboardInterrupt:
        sys.exit()
    
    print()
    GetStrengthTable(password)

if __name__ == '__main__':
    main()