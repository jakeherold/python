## Dice Roller

### Goals
* Inputs that account for the various common dice types in D&D (done!)
* Outputs the sum of all dice (done!)

* Suggested CLI Alias: 
        * alias roll="python3 [insert the absolute filepath here]/roll.py"  

### What I learned

1. Command line arguements are super useful and suprising not difficult with sys.argv. But, don't forget to slice off that index 0 goober. 
2. Python 2 and Python 3 are REALLY different. It's important to know which one of them is running on the command line you're messing with. 
3. Ubuntu Subsystem for Windows 10 (USW) requires you to specify python3, because Linux currently defaults to python 2. Notably, this is being changed in some of the new distro version releases. (Shoutout to Michael Adkins on that account)
4. Trying to get USW to run git commands once you've turned on 2-factor is difficult. Investing in SSH key configurations is well worth your time. 
5. Drink plenty of water. 

###To-do
1. Logic-check user input
2. Handle errors more gracefully