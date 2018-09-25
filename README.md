# Recipe Cookbook

In this project I wanted to create a simple yet functional website for storing and viewing recipes. 
The website uses MongoDB to store all recipe and user data, Python to access the database and Flask as a framework for the frontend so the user can access the data. 
Once a user registers on the site with a username, first name, last name and email address, their password they input is encrypted using bcrypt. 
The session is stored in the browser so they are free to close the page until they click the logout button.
Once logged in they are allowed to create recipes and view recipes from other users as well as their own.
 
## UX
 
This site is intended for anyone from single mothers to bachelors living alone who would like to look up new and exciting recipes to make at home or just store their own recipes for others to use.

Mockups can be found in the /mockup/ folder in this Git repo.

User Stories:
- As a mother, I would like to try new recipes, so that my child has a diverse palate growing up.
- As a single guy living alone, I would love to find recipes that are simple and easy to cook.
- As a person with average skills in cooking, I'm looking for recipes to broaden my knowledge.
- As a grandmother, I'm looking for a site to store all my recipes for everyone to enjoy as much as I did.

## Features

- User Login System - Users must register an account when first entering the site to be able to use it. Information needed is Username, First Name, Last Name, and Email. The password provided by the user is then encrypted with bcrypt.
- Create Recipe - Users can create recipes from the 'Create Recipe' link at the top, information stored within the MongoDB includes Recipe Name, Description, Prep Time, Cook Time, Ingredients, Instructions, Image URL, and the Author.
- Edit Recipe - Users can edit any previously made recipe by simply going to the recipe page and clicking the 'Edit' button or going to their Profile page where a list of their created recipes will show up once they have made some.
- Delete Recipe - If a user would like to delete a recipe, they can go to their Profile page again and a delete button will be next to the recipe name along with the View and Edit buttons.
- Browse recipes - There is a 'Master List' of all the recipes in the database accessed from the 'Recipes' button in the navigation bar on top. The home page has a list of categories if the user would like to look for a specific type of food.

## Technologies Used

- [Flask](http://flask.pocoo.org/)
    - Flask was used for the Back End.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Materialize CSS](https://materializecss.com/)
    - The Materialize framework is utilized to give the end user a pleasant UI to work with.
- [Materialize Icons](https://google.github.io/material-design-icons/#icon-font-for-the-web)
    - Materialize Icons are provided my Google as part of their Material Design suit.
- [Hover.CSS](http://ianlunn.github.io/Hover/)
    - Hover CSS was used for A little extra feedback for the user.
- [easyPaginate](https://st3ph.github.io/jquery.easyPaginate/)
    - Pagination is used for the list of recipes and the list of user created recipes.

## Testing

I tested all features manually during the process of making the site. The following are some examples of the tests.

1. Registering a User
    1. Click 'Sign up here' text on home page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with the input valid and verify form gets submitted correctly with no errors 

2. Login/Logout System
    1. Navigate to login screen
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with the input valid and verify user gets logged on correctly with no errors
    4. Once logged in, click the "Logout" button and verify user gets redirected to login page

3. Creating A Recipe
    1. Click 'Create Recipe' button in navigation bar
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with the input valid and verify recipe gets created with no errors

4. Editing a Recipe
    1. Click 'Edit' button on a recipe or from User Page
    2. Verify all recipe information has been input into the form fields and everything is editable
    3. Click 'Save Edit' button and verify the edit goes through

## Deployment

The project is deployed on Heroku, you can reach it by going to this [link](https://flask-recipe.herokuapp.com)

Use the following credentials in order to test the different recipe features eg. Editing and Deleting
Username: JohnDoe
Password: password


## Credits

### Content
- The recipes were mostly sourced from Google but mainly from [AllRecipes](https://allrecipes.co.uk)

### Media
- The pictures used on this site were sourced from Google's image search. Users can and are expected to provide a url for any recipe uploaded.

### Acknowledgements

- I received inspiration for this project primarily from allrecipes.com and myriad of other recipe sites out there.