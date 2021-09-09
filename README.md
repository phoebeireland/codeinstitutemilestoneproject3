# Rate Venture

* [Link to deployed website](https://rateventure.herokuapp.com/)
* [Link to github repository](https://github.com/phoebeireland/codeinstitutemilestoneproject3)


# Contents

1. UX
2. The Website
3. Testing the Site
4. Deployment
5. Credits


# UX

## The Project- Purpose and Business Goals

This Website aims to create a space in which users who are enthusiastic about the outdoors can find reputable companies and converse with other users on an exclusive forum. The Website is accessible to those who have accounts and those who do not. The only difference between the experiences of a user who has an account and is logged in versus a user who has yet to register an account is the visibility of the forum page and the contact page, which is hidden to users who are not logged into the site.

## User Stories
A New User to the site wants:
1. 
2. 
3. 

A Returning User to the site wants:
1. 
2. 
3. 
4. 

## Design Choices

The overall feel of the Website should be nature-loving but not rustic. It is a site for adventure enthusiasts who enjoy a more rugged outdoors experience but want a clean look for a website.

### Font

The font used on this Website is Hahmlet. It was found on Google Fonts and was chosen for its easy-to-read quality while still different from Times New Roman or another frequently used font.


### Colours

The main colours used on the site are:
* `#e3f2fd` for the background colour on the footer and the navbar
* `ghostwhite` for the main text colour in the shaded boxes 
* `rgba(0, 0, 0, 0.473)` for the colour of the shaded boxes
* `rgb(7, 179, 1)` for the colour that the footer links turn when users hover over them with the cursor


### Styling

The Website aims to promote an outdoors feeling, so the background for all of the pages is that of a mountainside. The text boxes are in semi-transparent cards. This is because the text still needs to be easily readable by any user, but I did not want to have a substantial block that would hide the background image.


## Wireframe Designs
Provided additional information regarding the wireframes below each picture. Refer to them to explain where a wireframe may differ from the published product or for choices behind the designs.


### Homepage
![Wireframe of the Homepage](static/images/homepagewireframe.jpg "wireframe of the main hopmepage for the site")

This image shows the initial idea for the main page of the website. This is the page that the users would see if they were not logged in or they did not yet have an account.
The homepage would only change slightly if the user did have an account and was logged in- ie. the two card boxes with information and buttons would change accordingly if a user was logged into their account. In addition, the navbar at the top would also display slightly different options depending on whether the user was logged in or not. 


### About Page
![Wireframe of the About page](static/images/aboutpagewireframe.jpg "wireframe of the about page")

This image shows the inital idea for the about page. This is the page that explains to the unregistered/ not logged in user what the site is about and also offers some testimonials from users who have enjoyed the website. As is noticable, this design in the final product differs from the initial concept with the addition of the user accounts and a condensed paragraph regarding the site. Rather than allow it to fill the whole page, I moved it to the top left section, and added in a scenic picture to the right of the description. 


### Join Us Page
![Wireframe of the Join Us page](static/images/joinuspagewireframe.jpg "wireframe of the join us page")

This image is the idea for the join us page. All in all, the page didn't change that much from the original concept to the executed version. THe only slight differenct would be the text at the top of the page before the form starts. 

### Login Page
![Wireframe of the Login page](static/images/loginpagewireframe.jpg "wireframe of the join us page")

This image is the idea for the login us page. All in all, the page didn't change that much from the original concept to the executed version. THe only slight differenct would be the text at the top of the page before the form starts. 

### Forum Page
![Wireframe of the Forum page](static/images/forumpagewireframe.jpg "wireframe of the forum page")

This images is the idea for the forum page. It didn't really change that much from the initial design. The only difference would be the addition of the Create Post section in the deployed page that is not in the wireframe. 

### Companies Page
![Wireframe of the Compmanies page](static/images/companiespagewireframe.jpg "wireframe of the companies page")

This image is of the inital idea for the Companies page. The design was relatively simple and the finished product resembles the wireframe. 

### Register Companies Page
![Wireframe of the Register Companies page](static/images/registercompaniespagewireframe.jpg "wireframe of the register companies page")

Ths image is the idea for the Register Company form page. In the end, I decided to simplify the form by ommitting te checklist that is shown in the image. It made more sense to take that section out, as it was complicating the form in an unnecessary way for the user. This function was satisfied by the comment box in which the company looking ot register could specify for themselves what services they offered. 

### Contact Us Page
![Wireframe of the Contact us page](static/images/contactuspagewireframe.jpg "wireframe of the contact us page")

This is the wireframe for the contact us page. The form ended up being exactly the same on the deployed website as it is in the picture above. 


# Features
* 
* 

### The Home Page
* 
* 
* 
* 
* 

### The About Page
* 
* 

### The Forum Page
* 
* 
* 
* 
* 
* 
* 

# Testing the Site


All HTML pages and CSS files were tested using the HTML and CSS Validator from W3.
* Link to the [HTML Validator](https://validator.w3.org./) used
* Link to the [CSS Validator](https://jigsaw.w3.org/css-validator/) used

As the HTML pages on VSCode were written with Flask notation, to test the HTML pages, I opened each page in the browser and right-clicked top open the Inspect Page, and then copied over the HTML code that the page presented there. This got around the issue the HTML validator was having with the presence of Flask notation on the VSCode page.

## Manual Testing

Using the Chrome Inspect tool, the following aspects of the website were tested:
* 
* 
* 
* 
* 

The EmailJS extenstion was tested using a sample email address and sample message.
* The result of this test was that the EmailJS service sent an email to the connected email address saying that a message was submitted.
* Also, an Auto-Reply email was successfully sent to the email address provied in the form. 


## Small Problems (that were fixed)
* For some reason, the background image was being really difficult and was refusing to fit the page. This was eventually fixed by adding a couple of lines to the css code relating to the background image size (cover), background-repeat (no-repeat) and background-attachment (fixed).
* The login button was not loading the correct function, so the posts were not showing up on the forum when the page was loaded through the login button. This was fixed by making the login function call the function `get_posts` rather than `forum`. 
* On the Forum page, initially all of the forum posts were being written into one card. After some tinkering, the posts were on their own carsd, but they were being nested- so the first post contained the second post that was in its own card, which held the third post which was in its own card an so on. This was fixed by moving the `{% endfor %}`, `{% else %}`, No Results line and the `{% endif %}` outside of the card div.
* ON the Forum page, the Delete and Edit buttons were not showing up. This was momentarily fixed by changing `post.created_by` to `posts.created_by`, which then lead to the buttons always showing up regardless of whether the logged in user had created the post or not. This was fixed by returning to `post.created_by` and instead changing the `session.user` to `session.username`, since `username` was the term used in the `app.py` file, instead of `user`. 
* The Edit Post function was able to be accessed by a user who knew the `post_id` of a post regardless of whether or not they were the author of that post. This was fixed with a bit of defensive programming, wherein I added an `if statement` to both the `editpost` function and the `deletepost` function that checked the creator of the post and if it matched the `session["username"]`, then the edit post form would be opened. If they did not match, then the user would get a message saying that they were not the creator of the post, and therefore were unable to edit the post, and the page would simply reload. 
* The Footer refused to stay at the bottom of the page on pages where there was not a lot of content. This was fixed by Googling, and landing on [this page](https://dev.to/nehalahmadkhan/how-to-make-footer-stick-to-bottom-of-web-page-3i14). As shown on the page, adding `min-height: 100vh`, `display:flex`, `flex-direction:column` and `margin-top:auto` to the `body` and `footer` styles in `style.css` fixed the problem. 


# Deployment
The Website was created in Visual Studio Code, version controlled with Git and hosted on Heroku.

Steps to publish website to Heroku:
1. On Heroku, press "Create a New App"
2. On the new page, type in the app name and select the region for the app. Keep in mind that the app name must be completely original. Then press "Create".
3. Once the page has loaded, under the "Deploy" menu, select "Connect to GitHub", and enter the name of the repository to connect it to Heroku. 
4. Once it is connected, either choose "Automatic deploys" or "Manual deploy" and choose the branch that Heroku will deploy from. 
5. Make sure that there is a Procfile in the root of the directory. If there is not, create a new file and name it `Procfile`, making sure that the first letter is capitalised, otherwise Heroku will not register the file correctly. 
6. Within the Procfile, type: `web: python app.py`. This will tell Heroku exactly what the process type is (in this case it's `web`) and what the command is (`python app.py`)
7. Once the Procfile is created and filled in, push the change to the branch on GitHub that was specified as being the branch to deploy from. If automatic deploys were enabled, Heroku will automatically deploy the changes any time alterations are made to the deployed branch. If Manual deploys were used, you will have to manually deploy every time a large change is made. 
8. Another necessary step is to add the information that is in the `env.py` file to the "Config Vars" section in Heroku. This is necessray, because since the `env.py` file is in a `.gitignore`, it is ignored by GitHub, and therefore is not accessible to Heroku.
9. To add the information to the Config Vars, open the "Settings" section on the app page. Once opened, scroll down to the "Config Vars" area and click on "Reveal Config Vars".
10. Here, you will see two text boxes that say "Key" and "Value" respectively. Into the "Key" side, enter `SECRET_KEY`, `IP`, `PORT`, `MONGO_URI` and `MONGO_DBNAME`. On the "Value" side of each pair, enter the value stated in the `env.py` file and press the "add" button to add each pair. 
11. Once all of the steps are complete, Heroku should be able to publish the website. 

Steps to publish website to GitHub Pages:
1. On the main page of the repository, click settings.
2. Go to the GitHub Pages section on the menu bar to the left.
3. In the Source section, click "None" and change the selected branch to "main". 
4. Leave the following option as (root), and click "Save"
5. Once the repository is published, a link to the website will be shown in the GitHub Pages section. 

To Clone this repository using IDE Terminal:
1. Navigate locally to the directory in which you want to save the repository.
2. On the main page of the repository, click the "Code" button, and copy the HTTPS address.
3. In the terminal, run the command: 'git clone' followed by the HTTPS address.
4. The project will now be saved to the desired directory. 

To Clone this repository using Visual Studio Code:
1. Open a new window in VSCode.
2. On the main page of the repository, click the "Code" button, and copy the HTTPS address.
3. Back in VSCode, under "Start" click "clone repository" and paste the link into the textbox that pops up.
4. Navigate into the folder that you want the repository to be saved into, and "Select Repository Location".
5. The repository will now be saved to the selected location.


# Credits

Created by Phoebe Ireland

The content of this website was created by Phoebe Ireland, with the exception of the following:
* [Google Fonts](https://fonts.google.com/)
  * Used to apply the Hahmlet font to all pages
* [Unsplash](https://unsplash.com/)
  * Used for the images found on the site
* [Bootstrap](https://getbootstrap.com/)
  * Used to create the Navbar and the footer
* [favicon.io](https://favicon.io/)
  * Used to create the favicon
* [jQuery](https://jquery.com/)
  * Uses jQuery for various Bootstrap functions 
* Code Institute's Task Manager Project
  * Used to model most of the code for the site.
* [Emailjs](https://www.emailjs.com/)
  * Used to connect the contact form to an email service. This is the main instance of JavaScript on the website.
* [Balsamiq](https://balsamiq.com/)
  * Used to create the wireframes.


   All of the content that was taken from other sources was altered to fit the use of this website where necessary.

A special thank you to my mentor for helping me though the project, and pointing out my (numerous) mistakes. 