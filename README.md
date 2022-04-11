# Creator Studio Inc

Creator studio inc is a portfolio website alongside a store, where the users of the page can look at the art that has been created and purchase anything that they feel will suit their needs. I created this website so that the user owner easily can change the services and the styles of the website. To feel in control of the site in a way that a static website could never achieve.
The site provides many ways for the user to contact the owner with any request that they have.
The styles section of the page is an easy way for the owner to publish the designs created. The user has a smooth checkout experience with help of stripe.

[Deployed Site](https://milestone-5-creator.herokuapp.com/)

[![landing-page.png](https://i.postimg.cc/SxSTXRhQ/landing-page.png)](https://postimg.cc/MvLbNWHg)

## Features 

#### Landing Page / Home Page
- In the section of the page, I have created a gallery for the user of the page to be drawn in by the design. With an obvious call to action button in the middle of the page.
    - ### Main Navigation
    - [![navbar.png](https://i.postimg.cc/V6hQgMzF/navbar.png)](https://postimg.cc/Fd0BsYdf)
    
    - #### Footer
    - [![image](https://www.linkpicture.com/q/footer_1.png)](https://www.linkpicture.com/view.php?img=LPic6250269b4bc7e1047339647)

#### About Page
- Here I've made a simple about me section, where the user of the page can read about who the owner is am and what kind of work the owner loves to do.
- [![about.png](https://i.postimg.cc/XvwkQ031/about.png)](https://postimg.cc/gw2h2Qx3)

#### Contact 
- A simple form for the user to send an email to the owner of the page.
- [![image](https://www.linkpicture.com/q/contact-form.png)](https://www.linkpicture.com/view.php?img=LPic62502673c0f8c122226016)

#### Services
- In the area of the page, the user can browse between the different services which the owner has to offer. As well as see a fixed price for the services provided.
- Below the services page there are testimonials from the previous work that the owner has done.
- [![services.png](https://i.postimg.cc/h47Pw4NG/services.png)](https://postimg.cc/Hjdg8mYG)
- [![testimonials.png](https://i.postimg.cc/xjHn5xbJ/testimonials.png)](https://postimg.cc/PNtgrMyT)
=======
#### Styles
- Here the owner can easily upload finished styles to the page. The user of the page can have a look and make a purchase easily with the help of stripe checkout.
- By uploading the owner of the site can navigate to the navigation bar of the page where they will find the button my profile. When pressed there is a dropdown menu with the option to either add a new style or where the owner can add a new service to the page.
- [![syles.png](https://i.postimg.cc/rFQbNxgR/syles.png)](https://postimg.cc/PPv2tLgd)

#### Shopping bag
- After the user has browsed around in the style section, and selected something that they want to buy. They can then go to the shopping bag the see what items have been selected.
- In the shopping bag the user has the option of deleting products that have been selected.
[![shopping-bag.png](https://i.postimg.cc/44zRVYrp/shopping-bag.png)](https://postimg.cc/fkTPhRWb)

#### Checkout / Payment
- Here the user will have an overview of the items in the bag. Below the overview a form for the actual payment is provided.
[![image](https://www.linkpicture.com/q/checkout.png)](https://www.linkpicture.com/view.php?img=LPic625026016251a1009555617)
[![image](https://www.linkpicture.com/q/checkout-payment.png)](https://www.linkpicture.com/view.php?img=LPic6250265e0717c263972470)

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

USER TESTING 
<br>
User Create Testing
<br>
Testing that new users that arrive on the page have been completed in several ways, implementing a standard testing procedure that ensures users can signup to the page.
No error where found my the newly created user goes to the user profile page. Ensures that the post_save method on user creation has been successful.

User Profile Testing
<br>
The user can add and update information on the user profile page. the post success returns success every time. New and updated information will overwrite previously added information.

User Profile Order History
<br>
If the user has made an order the user will see their previous orders on the order history page of the website. The order corresponds with the correct user and order history. Confirmed with the email confirmation sent when an order is placed.

User Make Order Testing
<br>
The user can successfully make an order on any of the styles that are posted by the store owner. When a payment has been completed the order is marked with the status code of 200 on stripe and an order confirmation email is sent. The order as stated above is shown on the user profile page if the user that made the order has made an account.

User Signup Newsletter
<br>
Anyone can signup for the newsletter, you don't have to be authenticated to do so. The service used is Mailchimp. A welcome email is sent to newly registered newsletter contacts.
This has been tested with my email and the process turns out successful every time.

User Send Email Test
<br>
The user can choose to send an email through one of the many contact forms on the page. Either through the service request forms or the normal contact form. The email is received by me every time and a successful post is shown in the terminal. This has been tested through multiple browsers and emails.

User Request Service Test<br>
The user can pick one of the 4 services that the page provides, Each service has a separate contact form making each form a unique subject. For the owner, this is more convenient. This has been tested by sending multiple emails through the services and verifying that the subjects do change on different service requests.

ADMIN TESTING <br>
Admin Add Service Testing<br>
The admin of the page can add new services. This has been tested by adding new services and seeing that everything is working. The service image works to upload every time and the data is correct when uploading. Each new service gets its request form as assigned in the models.

Admin Edit Service Testing<br>
The admin can choose to edit existing forms by being signed in. Simply by pressing edit when the user is a superuser. This has been tested by editing the information on each of the services that are provided multiple times.

Admin Delete Service Testing<br>
The delete view is working on the different services, it is the same as the editing service. A link will only show when the user is a superuser. When delete is pressed the service is deleted from the database, and no longer shown on the page.

Admin Add Style Testing<br>
The admin can as well as additional services, add new styles to the page, similar to the way above. when the user is a superuser the user has the option to see service management and style management. where you are redirected to a form to add new styles. This is done by manually entering information such as name price and description.

Admin Edit Style Testing<br>
Similar to the editing service, editing a style has the same principle. Has been tested editing the different styles on the page. Updating the information is successfully every time, the new information that is entered shows up in the correct style.

Admin Delete Style Testing<br>
Deleting a style is similar to editing, A button right next to edit style is only shown if the user is a superuser. With a press, the admin can delete the style. This has been tested many times by adding new styles with random data to den delete the style just added.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmilestone-5-creator.herokuapp.com%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/validator?lang=sv&profile=css3svg&uri=https%3A%2F%2Fmilestone-5-creator.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)
  - But some warnings, but the CSS code has been altered to pass through the test

### Unfixed Bugs

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

#### __Wireframes__
A complete view of the wireframes used to complete the project from a front-end perspective.
- Landing Page 
<br>

  [![image](https://www.linkpicture.com/q/portfolio-home-page.png)](https://www.linkpicture.com/view.php?img=LPic62501cb8500a7496651114)

- About me page
<br>

  [![image](https://www.linkpicture.com/q/about-me-page.png)](https://www.linkpicture.com/view.php?img=LPic62501c622c1ef732493847)

- Contact Page
<br>

  [![image](https://www.linkpicture.com/q/contact-page.png)](https://www.linkpicture.com/view.php?img=LPic62501d2ec92ae934128890)

- Service Page
<br>

  [![image](https://www.linkpicture.com/q/services-page.png)](https://www.linkpicture.com/view.php?img=LPic62501db00c2df556366973)

- Style Page
<br>
  
  [![image](https://www.linkpicture.com/q/shop-styles-page.png)](https://www.linkpicture.com/view.php?img=LPic62501de37c9f61365817146)

Note:
<br>
  Some Changes have been made to the actual page due to better cross device functionality.

#### __Database Schema__
  [![database-schema5.png](https://i.postimg.cc/QNnbFzFL/database-schema5.png)](https://postimg.cc/t7WPf2dD)

#### __Styles__
All Graphic design images are taken from the page - https://stock.adobe.com/.

#### __About me page__
About me image is taken from pexels - https://www.pexels.com/sv-se/foto/svartvitt-mode-man-person-1040880/

#### __Services__
<br>
The user can choose to send an email through one of the many contact forms on the page. Either through the service request forms or the normal contact form. The email is received by me every time and a successfu
Testimonial image yellow background from pexels - https://www.pexels.com/sv-se/foto/kvinna-ogon-modell-ansikte-415829/
Testimonial image girl jeans jacket from pexels - https://www.pexels.com/sv-se/foto/mode-kvinna-ung-tittar-1130626/
Testimonial image guy blue t-shirt from pexels - https://www.pexels.com/sv-se/foto/man-person-ansikte-staende-2379004/
Testimonial image girl black t-shirt from pexels - https://www.pexels.com/sv-se/foto/mode-person-hander-kvinna-1024311/

#### __Gallery images__

I have lost the documentation where I have written down the links. Been trying to find from where I downloaded them.
Can't find it. I know it's from pexels and from adobe, but I can't find the links.

#### __Agile Tools__

A link to the agile tool I have used during the development of this project. [Trello - Milestone5](https://trello.com/invite/b/o62444I2/a933ac02a2d5a85f2a29fcf6b91cef3c/milestone5)

#### __Marketing Plan__

Marketing Plan Creatorstudio Inc 

 

The approach I am taking to make this company reach leads is to generate organic customers through posting consistently on the pages created on Instagram, as well as Facebook. 

  

Making clients neutrally see my work through the social media platforms, If they wish there are content and newsletter signups on the website where ads can be used to influence the audience in making purchases. 

The weekly newsletter would be updated, and links and calls to action should be added. The design of the newsletter should be updated accordingly. 

With this approach, the more posts that are posted on Instagram and Facebook will generate future leads to the website once a following has been established. 

If capital was not an issue google ad sense, along with the previous would be a great way to bring in more leads. But as this costs a lot of money. It's not an ideal way to start. 

As the following of the 2 social media platforms grow, a youtube channel should be created to make the content more visually engaging. By putting a face to the brand, clients would feel more at ease before making the first purchase. But as this is a graphic design studio, the true product is the work that is created by the owner. 

Making the artwork as good as possible is a sure way to bring in more clients.  

So as a recap of the marketing plan. 

Steps in order. 

Push Instagram & Facebook - Through posts and actively commenting and engaging with other similar content creators. 

Paying for Ads on the platforms to reach a wider demographic. 

Making the business a google business to use the ad sense of Google. 

Growing an organing following by putting a face to the brand. 

Starting a youtube channel where the work process is documented and shared with the followers. 

Making collaborations with similar content creators to reach a 		wider audience.                  

Using the follower base to market the work created. 

By following these steps consistently a strong following base would be acquired, Organic customers would come to the page just to be the curiosity of the followers and work posted. 
