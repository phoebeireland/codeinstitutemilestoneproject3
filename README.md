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

## The Project- Purpose and Buisness Goals



## User Stories
As a New User to the site, I want:
1. 
2. 
3. 

As a Returning User to the site, I want:
1. 
2. 
3. 
4. 

## Design Choices

The overall feel of the website should be outdoorsy, but not rustic. It's a site for adventure enthusiasts who enjoy a more rugged experience outdoors, but who want a clean look for a website. 

### Font

The font used on this website is Hahmlet. It was found on Google Fonts, and was chosen for its easy-to-read quality, while still being different than just Times New Roman or another frequently used font.


### Colours

The main colours used on the site are:
* `#e3f2fd` for the background colour on the footer and the navbar
* `ghostwhite` for the main text colour in the shaded boxes 
* `rgba(0, 0, 0, 0.473)` for the colour of the shaded boxes
* `rgb(7, 179, 1)` for the colour that the footer links turn when they are hovered over with the cursor


### Styling

The overall look of the website is 


## Wireframe Designs
I have provided additional information reagarding the wireframes below each picture. Please refer to them to explain where a wireframe may differ from the published product, or for choices behind the designs.


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

As the html pages on VSCode were written with Flask notation, to test the HTML pages, I opened each page in the browser and right-clicked top open the Inspect Page, and then copied over the HTML code that the page presented there. 

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
1. 
2. 
3. 

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
  * Used to create the Navbar
* [favicon.io](https://favicon.io/)
  * Used to create the favicon
* [jQuery](https://jquery.com/)
  * Uses jQuery for 
* Code Institute's Task Manager Project
  * Used to model most of the code for the site.
* [Emailjs](https://www.emailjs.com/)
  * Used to connect the contact form to an email service.
* [Balsamiq](https://balsamiq.com/)
  * Used to create the wireframes.


   All of the content that was taken from other sources was altered to fit the use of this website where necessary.

A special thank you to my mentor for helping me though the project, and pointing out my (numerous) mistakes. 