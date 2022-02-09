[View the live project here.](https://andna5980-boutiquecake-v1.herokuapp.com/)

This is the 4th Milestone.
Ecommerce website offering crafted Cakes, cheesecakes and cupcakes.


## User Experience (UX)

### USER STORIES

1. As a first-time visitor, I want to quickly understand the main purpose of the website and how I can benefit 
    from the service provided.

2. As a first-time visitor I want to navigate the page in a ease and clear way.
    
3. As a firt-time visitor I want to get access to content without the need of register os join the service. 

4. As a first-time visitor, I want to be able to see clear explanation of the products and clear prices.

5. As a returning visitor, I would like to be able to filter products so i can see only what i am interested in.
    
6. As a retuning visitor I would like to see new products. 
    
7. As a returning visitor, I would like to be able to create an account where I can see previous purchases. 
    
8. As a frequent user I want the system to save my details like my address for future purchases
      
      
## Structure

The website will present all the produts for non registered users.

- Home Page will present a simple picture of a Xmas theme cupcake.

- Home Page will have a My Account link where users can create an Account or log in option for already registered users.

- A Register Page will ask the user to fill in some details in order to create the account.

- A login / Sign In page will ask registered users to fillin the form with their pre registered details in order to login.

- Non registered users will be able to navigate the website, having access to all the products and purchasing without be registered.

- Non registered users can select a product, read product information aswel as price, modify the quatity amount and add to bag.

- Non registerd users can go to the bag Icon in order to complete the order, this page will inform about the product choose and also gives the user the option of updating the amount of products, this page also informs the user of the total amount to pay.

- Non registered user will be able to complete the order using the Checkout Secure button that will take users to the Checkout Area where users will fill in all the information related to the user; this includes full name, delivery address, and credit cards details. This page will allow users to complete the purchase or adjust the bag, adding or deleting any product.

- Non registered users. will complete purchase and an automated email will be send to the user confirming the purchase, none of the previous details provided by the Non register user will be saved.      


The website will contain 3 pages for users that are registered and are logged.

- Home Page will allow also registered users to log in.

- Registered user can login by clicking in My account area/Log in. 

- Registered users have to provide email address and password in order to access to the site. Once the authentication is done a message of congfirmation appears in the screen.

- Registered Users then have access to My Profile page where purchase history appears but also user information that can be updated.  

- Registered Users then have access to the products and can purchase without re-entering their delivery details. Card details will be always required for security reasons.

- Register Users also have the option of login out by clicking in My Account/Logout.

## Scope

* Boutique Cake is a website that allows customer to buy hand crafted cakes, cupcakes and cheesecakes. Anyone can have acces to it and buy any product without been a register user. We will be using Django framework, the final site will be host in Heroku and will be using the database Heroku Postgress at the same time of AWS Cloud service.

* Users: In order to become a registration, users will be asked to registered their details via the My Account\Register link that appears in the main navbar left side. Once users are registered they can update their details, shipping address and also users can see a purchase history aswel as the current bag with previous products selected ready for checkout.

* Administration: There is administration area where staff/admin can have control over the site. Via administration control, staff/admin can control website products, they can be udated, edit, or deleted. This area also controls all the registered users and their details.


### Database:

This project uses the following Databases.
* SQlite
    * Cloud Base Database to hold categories and products, orders and users.


## Features

### Navbar:
Navigation bar will appear in every page this includes include a search bar, My Account(includes Regiter and Login) and checkout bag, which will inform user of any item ready to purchase.

### My Account
#### Register:
Page link that help users to create an account, they have to provide a some details and a password.

#### Log in:
Page link for already registered users, they can access by providing username/email and password. 

### Log in Users 
### Profile:
Page link that provide user details, under this page users can modify or delete their personal details.

### Logout:
Functionality in the navbar that will allow the logged users to logout/exit the web 

 

       
