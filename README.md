File contains three classes:
Shop: which handles shop information by adding the user, greeting them and allowing them to exit
Shop exception: which uses FundsError
User: which handles user information such as money, basket, viewing shelves, making selections and eventually checking out (or leaving)

The user is asked for their name, and the game continues until either the user is kicked from violating purchase requirements, entering an incorrect exit answer, leaving or checking out.

When the user adds or removes items, the balance and basket are updated. They cannot add items that do not exist, exceed the balance or are out of stock, and they cannnot remove items that they do not have in their basket

Checkout is for purchases (basket must have contents)
Leaving the shop means that the user exits and no purchases are made.
