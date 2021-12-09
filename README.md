# Creator Studio Inc

Creator studio inc is a portfolio website alongside a store, where the users of the page can look at the art that has been created and purchase anything that they feel will suit their needs. I created this website so that the user owner easily can change the services and the styles of the website. To feel in control of the site in a way that a static website could never achieve.
The site provides many ways for the user to contact the owner with any request that they have.
The styles section of the page is an easy way for the owner to publish the designs created. The user has a smooth checkout experience with help of stripe.


![Landing Page Gallery](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/landing-page-gallery.png)

## Features 

#### Landing Page / Home Page
- In the section of the page, I have created a gallery for the user of the page to be drawn in by the design. With an obvious call to action button in the middle of the page.
    - ### Main Navigation
    - ![Navbar](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/navbar.png)
    
    - #### Footer
    - ![Footer](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/footer.png)

#### About Page
- Here I've made a simple about me section, where the user of the page can read about who the owner is am and what kind of work the owner loves to do.
- ![About me]()

#### Contact 
- A simple form for the user to send an email to the owner of the page.
- ![Contact form](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/contact-form.png)

#### Services
- In the area of the page, the user can browse between the different services which the owner has to offer. As well as see a fixed price for the services provided.
- Below the services page there are testimonials from the previous work that the owner has done.
- ![Services](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/services.png)
- ![Testamonials](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/services-testamonials.png)

#### Styles
- Here the owner can easily upload finished styles to the page. The user of the page can have a look and make a purchase easily with the help of stripe checkout.
- By uploading the owner of the site can navigate to the navigation bar of the page where they will find the button my profile. When pressed there is a dropdown menu with the option to either add a new style or where the owner can add a new service to the page.
- ![Styles](https://github.com/jacobmolsby93/Milestone-5/blob/3fec33b72ec7b106cc94d34ff092a7febe800923/media/styles.png)

#### Shopping bag
- After the user has browsed around in the style section, and selected something that they want to buy. They can then go to the shopping bag the see what items have been selected.
- In the shopping bag the user has the option of deleting products that have been selected.


#### My profile
- In this area of the page, the user can see what they have ordered. As well as update the profile information of the user.

 
#### Signup 
- If the user of the page is not a member of the site. They can easily signup to the page and make purchases and do the things mentioned above.
- The complete authentication system is done with the help of Django-allauth.


#### Emailing
- The emailing services of the page are several. There is email functionality when ordering services, where the user of the page emails the owner.
- There is an email form on contacts where the user of the page can email the owner of the page if they have any projects that are outside the scope of the page.
- There is an email confirmation that is sent when the user of the page has ordered something from the shop styles section.
- Lastly, anyone that visits the site can signup for a newsletter in the footer of the page. This function is made possible with the help of MailChimp


### Features Left to Implement

- #### A Blog posting system for the owner to update the users of what's happening on the page in a personalized way.

## Testing 

Fixed message container, on small devices. was too wide for small devices.

fixed add to bag buttons on all screen sizes

fixed about me img link, had accidentally put a trailing comma 

fixing the navigation bar for mobile devices and getting the dropdown menus to work as I wanted.
Took some work to make the finished product look like it does.

The hamburger menu icon on mobile screens. I could not get the background color of the drop-down menu to the one I wanted.
but fixed it by trying it out on the inspect page.

On the style detail page, when going from large screens to smaller screens I had issues with the margins and the two columns aligning up when stacked on top of each other.

Had complications when trying to save the user information to the actual profile. Had to go through the code several times before realizing I had forgotten to implement a part of the code.

All the images of the page when uploaded to amazon aws generated a new name for themselves in the deployed project so the images could not be found.
I solved this firstly by importing all the pictures again on the deployed page, through the admin panel.
The images that hardcoded into the site I found the solution was to put {{ MEDIA_URL }}imng.png, which I didn't do in any of the places.


Had a lot of issues with the emailing of the page. It was my Gmail account which I connected that didn't work for some reason.
I troubleshot this over and over again for several hours until I came to this conclusion.

The webhook handler I have used is from the boutique ado walkthrough, with some small modifications. but implementing it into my project
required troubleshooting of the handler as well as the actual webhook. I got it to work after finally I realized that my workspace had to
be public before the webhook handler could connect to the actual page.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-azure-loon-noxkcxbz.ws-us21.gitpod.io%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F8000-azure-loon-noxkcxbz.ws-us21.gitpod.io%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=)
  - But some warnings, but the CSS code has been altered to pass through the test

### Unfixed Bugs
- There is one bug when sliding between screen sizes which I have tried to fix 

## Deployment

The site was deployed using Heroku.
To deploy the site to Heroku these are the steps that you have to take for the deployment to be successful.
- First, you need to create a Heroku app on the Heroku page after you have logged in. And choose the region that's closest to you.
- Once you have created the application, You need to head over to resources and add the Postgres database.
- When the Postgres database has been added you 
- for Postgres to work in the workspace you need to install dj_database_url and psycopg2-binary with a pip install.
- Then import dj_database_url in settings.py.
- After all that you have to assign the database variable the dj_database_url.parse to your Postgres database.
- Then set all the crucial variables into environment variables in Heroku, such as secret keys database keys, and such.
- Once this is complete, a Procfile is needed to tell Heroku to create a web dyno. Which will run gunicorn and serve the Django app.
- Then add the hostname of the Heroku app to allowed hosts in settings.py, along with the localhost used for Gitpod.
- With this complete, now it's time to add the changes to GitHub and push it to finalize the changes.
- In Heroku, connect the git repository to the Heroku application to deploy the application.
- At this stage the application has no connection to any of the static files. To access the static files, we need to connect a separate web service called Amazon Aws.
- In amazon, create an account. When the account is created. Create an S3 bucket to store the static files from.
- In the bucket turn on static website hosting.
- In the permission tab, set up the cors config. Which is going to set the required access between the Heroku app and the bucket created.
- After that add a bucket policy in the policy generator.
- Then head to the IAM management page.
- Create a group for the user to live in.
- Create an access policy, granting access to the S3 bucket created.
- Create a user, then assign the user to the group.
- Download the csv file to get the access key and secret access key to assign them to the evironment varibles in heroku.
- Now we need connect the S3 bucket to django, by installing boto3 and django-storages.
- pip3 freeze > requirements.txt
- Add storages to installed apps.
- Add the appropriate settings to the settings.py file.
- Now djano will collect the static files and upload them to S3.
- In the bucket. Create a folder called media, and upload all the media files related to the page.
- With all this complete the website is now deployed with static files ready and media files uploaded.

## Credits 

- #### Code credit
- Footer from here -- https://jsfiddle.net/bootstrapious/m215fdnw
- navbar base from the Boutique Ado.
- Toasts - Code institute // bootstrap
- HTML layout on toasts - Code institute, Boutique Ado
- Html layout on - main-nav // mobile-top-header - Code Institute, Boutique Ado
- Parts of the Views - Code Institute, Boutique Ado.
- UserProfile model - Code Institute, Boutique Ado.
- Order model - Code Institute, Boutique Ado.
- Checkout app - Large parts taken from Boutique Ado
- Webhook files - taken from Code Institute, Boutique Ado.
- Gallery on the home page, Love Running Code Institute.
- Complete Bag application - Boutique Ado 

### Content 

- All the content has been written by me.
- In the Testimonail part of the page. In the code, I just realized i have missspelt it.
 
### Media

#### Styles
All Graphic design images are taken from the page - https://stock.adobe.com/.

#### About me page
About me image is taken from pexels - https://www.pexels.com/sv-se/foto/svartvitt-mode-man-person-1040880/

#### Services 
Testimonial image yellow background from pexels - https://www.pexels.com/sv-se/foto/kvinna-ogon-modell-ansikte-415829/
Testimonial image girl jeans jacket from pexels - https://www.pexels.com/sv-se/foto/mode-kvinna-ung-tittar-1130626/
Testimonial image guy blue t-shirt from pexels - https://www.pexels.com/sv-se/foto/man-person-ansikte-staende-2379004/
Testimonial image girl black t-shirt from pexels - https://www.pexels.com/sv-se/foto/mode-person-hander-kvinna-1024311/

#### Gallery images.

I have lost the documentation where I have written down the links. Been trying to find from where I downloaded them.
Can't find it. I know it's from pexels and from adobe, but I can't find the links.
