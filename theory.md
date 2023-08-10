### What does SDLC stand for? ###
Software Development Life Cycle.

### What exception is thrown when you divide a number by 0 ###
ZeroDivisionError

### What is the git command that moves code from the local repository to the remote repository? ###
git push 

### What does NULL represent in a database ###
It is a marker to indicate a non-existing value, acting as a placeholder for an unknown value.

### Name 2 responsibilities of the Scrum Master ###
**A scrum master helps keep the development team organised, allowing for projects to be undergone in order of priority so that all tasks are completed on time** e.g. longer tasks may be started earlier and require more developers, but shorter tasks may be assigned inbetween to a single/few developers. They ensure that there is a flow.

**They can act as a bridge between product management and development through clear communication, which aids in the development process.** If developers have a clear idea of what is needed from them, they can correctly fulfill the needs that the client requires. This mitigates any risks of mistranslation, where the scrum developer can communicate with both product management and developers. This can be related to API, the API acts as the middle man between the server and internet, whereas the scrum developer is the middle man between the developers and the client.

### Name 2 debugging methods and when you would use them ###
Interactive debugging commonly uses breakpoints which can be inserted in an IDE e.g. visual studio code. The developer may choose to add variables to the watch list and see how they change over time. This is very useful as spotting a mistake **may** fix the issue entirely e.g. an incorrect assigment of a variable will be carried down the code and impact the remaining code. 

Print debugging is where print statements are used throughout code to investigate the changes occuring, usually in a function. However, this is harder to understand compared to interactive debugging as it is more difficult to see which variables are which in the code. If there is a function with many loops, and each loop has multiple print statements, it can be difficult to follow.

### Errors and debugging ###
TypeError: '>=' not supported between instances of 'int' and 'str' may occur if one argument is a string and the other is an integer (or even float). Ideally, one can put if float(cash_given) >= float(price) which would eradicate this issue. However, we can use a try, except block if we want to use exception handling. 
        
    def can_pay(price, cash_given):
      #cash_given = round(float(cash_given),2)
      #price = round(float(cash_given),2) 
      #commented conversions recommended instead of try: except:
      try:
        if cash_given >= price:
          return True
        else:
          return False
      except TypeError:
        return "Invalid input type, use numerical data types"
  
Another issue is that if we do not convert to a numerical data type when the values are strings, the comparison is incorrect. The comparison is of the ascii values e.g. if we use "100" as price and "45" as cash_given, the function returns true because the ascii value of 45 is greater than 100. 

Also, we do not need else: as the only alternative to >= is <. 
The most optional solution is:
    
    def can_pay(price, cash_given):
        if round(float(cash_given),2) >= round(float(price),2):
            return True
        return False
     
This is rather important when using inputs because if the values ar obtained from input(), they will always be strings.

### What is git branching? Explain its uses ###
Git branching is a way for the developer to make changes with specific purpose and multiple branches can be used for the same repository. An example is that the developer may have a branch for "nav bar adjustments" which requires a lot of changes if the developer is changing a theme for example. This keeps the changes seperate from main. There may also be a branch for "dark theme" where there is a dark theme implemented. You would want "dark theme" and "nav bar adjustments" changes to be separate. What if the developer is happy with the nav bar adjustments, but the dark theme implementations are all wrong? In the same branch, can also be main, then the developer would have to scan through the code and possibly delete the dark theme adjustments, then commit the nav bar adjustments. It is more efficient to keep these separate. Committing the branch is the developer saying "I am happy with the changes, I am ready to commit to them", committing to main would be "I am happy with integrating these changes into the finished product and there are no collisions with pre-existing code". 

### Design a restaurant ordering system ###

**Key requirements:**
Front end:
- User can see the menu
- User can make selections of what they want to order and account for modifications e.g. removal of ingredients 
- User can make adjustments e.g. change items if they don't want to order them
- User can track their order
- Good and clear UI if an app or website
- Different staff can see different information e.g. chefs need table name and orders, but waiting staff may see different information such as the total price of the bill
- Possibility to reserve a table, but also cancel if needed
Back end:
- Statistics can be seen e.g. in a database, to figure out which items are popular and which items are not, this can help business
- 
**What are your main considerations or problems?**
- The system must be able to handle lots of users and not crash when peak is reached
- Good security to ensure that credit/debit card information is not stolen, possibly encryption
- Good UI and interactability so the user can navigate their way through the website
- 
**What components or tools would you potentially use?**
- Database management e.g. SQL to monitor statistics refer to point 8
- Integration of payment e.g. paypal
- Cyber security developer may be able to assist in security and ensuring that bank details and information are safe
- UI and web development (is the mobile site compatible? Does the website look suitable?)
- Tracking tools e.g. https://linksoftwarellc.com/blog/customer-order-tracking/

