# Import Libraries
import time
# Setup Variables
msg = "Text*Pad" # Print The Message Here
l = len(msg) # Find The Total Amount Of The Lenght Of The Message.
num = l*2 # Set The Size Automatically
n = num//2
# Start Printing The Start Of The Heart
print()
for i in range(n):
    print(" "*(n-i-1) + "* "*(i+1), end="") # Converted 4 lines to 1 single statement.
    if num%2 == 0:
        for j in range(2*(n-i-1)):
            print(" ", end="")
    else:
        for j in range(2*(n-i-1)+1):
            print(" ", end="")
    for j in range(i+1):
        print("* ", end="")

    print()

# Print The Message
print("* "*((num-i)//2) + " ".join(msg) + " *"*((num-i)//2))
# Print The Remaining Body Of The Heart
for i in range(num, 0, -1):
    print(" "*(num-i) + "* "*(i)) # Converted 5 lines to 1 single statement.

# Print Version Updates
print('''
 Version 1.0 - {
   Started TextPad Foundation
   Created Dark Mode & Scrollbar
   Added confirmation while closing
 }
 
 Version 1.1 - {
   Created About window
 }
 
 Version 1.2 - {
  Created Find window
  Fixed bugs in About & Find window
  Improved design of UI
 }

 Version 1.3 - {
  Replaced Button Frame with Menu widget
  Added Copy & Paste buttons 
 }
 
 Version 1.4 - {
  Created Fullscreen toggle
  Added Line and Column Label 
 }

 Version 1.5 - {
  Added Keyboard Shortcuts
  Improved Save Option
 }

 Version 1.6 - {
  Added font selection
  Added memory (chache)
 }
 ''')
input("Press ENTER to exit.")
exit()
