# Full Stack Frameworks with Django - Milestone Project 4

![Woola2Shop](https://ucarecdn.com/18c6bb2b-b90c-4e10-802a-b71d47e03772/woolawoola_LOGOS_page_01.png) 
### An ecommerce website for Woola Woola Shop

# Table of Contents
1. Background
2. Objectives
3. Demo
4. Adopted Technology
5. User Stories
6. Development
7. Implementation
8. Testing
9. Deployment
10. Acknowledgement

# 1. Background
Woola Woola is an existing small business entity founded by Jean Tan, a friend of mine. 
It is an accessorized earrings store, which currently has social media presence as its only channel of marketing, 
communication and business transaction. As a strategic planning for future expansion, 
Woola Woola requires an ecommerce website to showcase its business and products and to conduct its business transactions.
This version of the website is an improved version that was built previously for my Project 1. The link to the first version
of the website can be found [here](https://farhansam.github.io/woolawoola/)

# 2. Objectives
* To complete Milestone Project 4 - Full Stack Frameworks with Django
* To build an ecommerce website for a business, with user and payment functionalities
* To build a platform for the business to manage its information and transactions in a database

# 3. Demo
View the end product: [Woola2Shop](https://woola2shop.herokuapp.com/)

# 4. Adopted Technology
* HTML/CSS for UI/UX
* Bootstrap v5.0.x for responsiveness
* Python/django for web framework
* dbsqlite for database in development
* PosgreSQL for database in deployment
* Stackoverflow for coding tips
* Uploadcare for hosting images
* Fontawesome for icons
* Stripe for payment features
* MockFlow for wireframes
* MS Powerpoint for wireframes
* sqldbm for ER diagrams
* Github for version control
* Heroku for deployment

# 5. User Stories
There are 2 main target audiences for the website.  

The first target audience are existing as well as potential customers of Woola Woola.
Some of their user stories are:

1. I want to visit the website of the store
2. I want to know a little bit about the background of the business
3. I want to view the product collections that they have
4. I want to view the products that they are selling
5. I want to purchase their products

The second target audience are the administrator and staff of the business itself. Their user stories are:

1. As the admin, I want full access to the website features and have admin control
2. As the staff handling the website, I want to be able to create, read, update and delete the products that are available

# 6. Development
Wireframe for respective webpages:

1. Home
![](https://ucarecdn.com/10cd4a4f-5429-42c0-a330-cdf96262085d/w_home.png)

2. Shop
![](https://ucarecdn.com/2785d733-6b5d-4e7c-9411-10eba4f79352/w_search.png)

3. Cart
![](https://ucarecdn.com/3d03272a-0864-45c4-9211-105481406a7b/w_cart.png)

Schema Diagram

![](https://ucarecdn.com/2fca9c7f-cd88-40f9-b5e3-7a814ebe4261/schema.png)

# 7. Implementation
Screenshot of actual webpages:

1. Home page
   <br>
   The home page serves to be the central page that connects to all other pages.
   It also serves to answer to the following user stories:
   ```
    1. I want to visit the website of the store
    ```
   ![](https://ucarecdn.com/c43cb1b2-02c8-4918-b58f-65aa1311ee6e/ww_home.png)

2. Shop
   <br>
   This page serves to answer to the following user stories:
   ```
    4. I want to view the products that they are selling
    5. I want to purchase their products
    ```
   ![](https://ucarecdn.com/cc3b3606-ce72-4a5e-a9fe-84bc6f768c30/ww_shop.png)

3. Cart
   <br>
   This page serves to answer to following user stories:
   ```
    5. I want to purchase their products
    ```
   ![](https://ucarecdn.com/f0664a9d-32d9-421f-963c-e605abea73d9/ww_cart.png)
   <br>

4. CRUD
    <br>
   This page serves to answer to following user stories:
   ```
    1. As the admin, I want full access to the website features and have admin control
    2. As the staff handling the website, I want to be able to create, read, update and delete the products that are available
    ```
   ![](https://ucarecdn.com/f27517fe-b334-4772-b364-6021be879d79/ww_create.png)
   <br>



# 8. Testing

## Test Table

| Test Type | Test | Result | Error Fix |
|:---------:|:-------------:|:-------------:|:-------------:|
| Functionality | Test navbar links among all pages | All links work | NA |
| Functionality | Test links on buttons in all pages | Some links do not work | Some render_template or redirect actions do not work due to missing parameters. Troubleshoot and rectified by ensuring correct parameters are passed where needed.|
| Functionality | Test submit/search/update/delete of forms | Form submission work as expected | NA |
| Usability | Test search engine whether string input matches value in database | Search engine works with no issues | NA |
| Usability | Test user input validation by entering invalid condition in input field | Failed due to user able to input unacceptable data | added validation condition to prevent input of unacceptable data |
| Responsiveness | Test responsiveness of button locations when browser is resized using Google Chrome inspect element | Buttons are able to relocate at location that is user-friendly | NA |
| Responsiveness | Test responsiveness of images and columns using Google Chrome inspect element | Images are resized and columns are restacked | NA |
| Data Management | Test whether data is able to be transferred to database when form is submitted  | Data transfer successful | NA |
| Data Management | Checked data relationship by deleting data attached to foreign key | Foreign key data is also affected | NA |

## Bug Testing

HTML files were passed through W3C Nu HTML. Major errors were rectified.
    
CSS file was passed through Jigsaw CSS. No errors found.
   
Python file was passed through PEP8 online checker. Major errors rectified.

# 9. Deployment
* Link to published website: (https://woola2shop.herokuapp.com/)
* Link to source code: (https://git.heroku.com/woola2shop.git)

Github was used for version control, whereas Heroku was used for deployment.
The deployed pages' functionality, usability, responsiveness and data management were tested 
against the development version and both were found to match.

eg. of Development version vs Deployed version
![Development](https://ucarecdn.com/8cd4912c-f408-43bf-b2bf-50b35afd4922/ww_dev.png)
![Deployed](https://ucarecdn.com/690bb8a1-3383-441c-86c6-030fe7590a38/ww_dep.png)

# 10. Acknowledgement
* Trent Global College for providing the platform for learning.
* Code Institute for their TAs, namely:
  * Paul Chor
  * Ace
* [Stackoverflow](https://stackoverflow.com/) for coding tips
* [Bootstrap](https://getbootstrap.com/) for HTML and CSS templates.
* [w3schools](https://www.w3schools.com/) for basic HTML/CSS/Python syntax references.