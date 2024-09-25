# DH Bakes - Local Bakery eCommerce Website

Welcome to DH Bakes, a fully-functional B2C eCommerce platform for a local bakery, offering customers the convenience of browsing, ordering, and requesting custom delicious baked goods online. Whether you're looking for a custom cake for a special occasion or simply want to indulge in fresh pastries, DH Bakes provides a user-friendly experience for everyone.

The site was built using HTML, CSS, JavaScript/JQuery and Python (Using the Django Framework)

Users can experience the site in full, viewing all products with the various filter options, subscribe to newsletters and offers, check out FAQ's and Testimonials, along with adding their own reviews and sending messages to the store owners. Users can view recipes uploaded by the store owners so they can also bake their own cakes at home.

The site has a fully functional payment/checkout system, allowing users to create a profile which saves their data to and their previous order history. All users will receive order confirmation emails as long as a real email is added for checkout.

DH Bakes is built with responsive design in mind and can be used on a variety of screen sizes.

![Responsive view of DH Bakes](readmedocs/screenshots/amiresponsive.png)

The Live Site can be found [Here](https://dh-bakes-e0dca18717d0.herokuapp.com/)



## User Experience (UX)

DH Bakes has been designed for a real life business that my partner does on the side of normal work. It's a family run bakery of three sisters sharing a love for delicious creations. Users can visit the store and purchase popular bakes, request custom bakes via the contact us form, view previous user experience via testimonials, check out FAQ's to help answer anything a site visitor may need to know. 

All users can browse, sort and filter the products on store using a variety of tools such as the search bar, nav item and built in ordering filters.

Staff/Admin users can fully operate their product lists directly from the product management page, allowing for the store products to be easily updated when needed.

The site design links in with the pink theme already established by the owners who only operated from Facebook and Instagram previously.

### Site User Goals

- View products that are available on the site
- Search for specific products using the search bar / filters available
- Add items to my bag to view before checking out
- Purchase Items that i've selected
- Create an account for better site engagement
- Receive order confirmations of orders i've placed
- See previous orders from my profile page
- Save my details to my profile for quicker checkouts
- View FAQ's to help me find out information about possible questions I have
- Check out testimonials from previous users who have shopped on site before
- Add a testimonial if I want to
- Get in touch with the store owners via a contact us form for anything I may need to request
- Sign up to a newsletter to get updates and discounts
- Easily find the stores social media accounts

### Returning User UX

- View my previous orders via the order history section of my profile
- When checking out have my profile details auto populate in my delivery info on checkout. 
- Be able to reset my password if I forget it. 


## Business Model

DH Bakes operates on the business model: Business-to-Consumer (B2C)
The site offers freshly baked cakes, cookies, cheesecakes, and other baked goods. DH Bakes target market will be individuals (families, event organizers, food enthusiasts, and gifting consumers) who enjoy premium baked goods and are looking for convenient, fresh, and customisable treats delivered to their doorsteps.

The website has been created so the business owners have a primary platform where customers will browse, order, and customize baked goods. The website has user-friendly features such as product filters (e.g., by occasion, flavour), easy customisation tools, and secure payment options for checkout.


## Marketing

DH Bakes positions itself as a premium yet approachable online bakery offering high-quality, customisable products. The focus will be on freshness, quality and personal touches for special occasions.

Investing in SEO optimisation will help drive organic traffic to the site, focusing on key terms related to what the site offers.

In addition, Facebook and Instagram pages have been used in the past as the main source of custom for DH Bakes, these are still operational and can be accessed directly from the website. The website will be added to both social media platforms for users viewing the social pages access to the website URL.

### Socials

Due to DH Bakes being an existing business before this website creation. Their Facebook and Instagram pages already existed. Please feel free to take a look below at each site.

[Facebook](https://www.facebook.com/dhbakesx)

![Facebook page](readmedocs/socials/facebook.png)


[Instagram](https://www.instagram.com/dhbakes_/)

![Instagram page](readmedocs/socials/instagram.png)

### Mailchimp

Mailchimp was added to the sites home page to allow site visitors to add their email address to subscribe to the store for updates and offers on the site. Site owners can access their Mailchimp dashboard showing all email addresses of users that have added their email to this feature.

![Mailchimp](readmedocs/screenshots/mailchimp.png)

### SEO

I used an online tool [WordStream](https://tools.wordstream.com/fkt?website=https%3A%2F%2Fdh-bakes-e0dca18717d0.herokuapp.com%2F&cid=&camplink=&campname=&geoflow=0) to help locate keywords to use for my site. There was a mixture of a high and low competition so I used a selection of all that appeared in the results.

Key words were then added into the meta tags of the base.html file:

<meta name="keywords" content="cookies, cakes, cupcakes, baking, bakers, birthdays, chocolate, vanilla, bakery, custom cakes, recipes, sweet things, sweet tooth, freshly baked, custom cookies, desert">


## Agile Working

Before I began coding my project, I set up an Issues template in GitHub and linked it with a board for user stories. In addition, labels and milestones were created ensure my project work was planned accordingly based on the time I had to finish and submit the work.

User stories were added to sprints to allow me to focus on sections of work at a particular time. Allowing me to work out a good pace to complete work.

As things occurred during the project, other items would be introduced and re-prioritised, enforcing the agile methodology of working.

![User Story Board](readmedocs/screenshots/github-board.png)


## Site Design

The base design was inspired by the Code Insitute Boutique Ado walkthrough, however there were other styling changes added to make this different and consist of a better UX and UI. The nav bar and footer show on all pages along with the search bar. The colour scheme / buttons / text / shadow boxes are all consistent throughout.

### Wireframes

Wireframes were created to give me an idea on how i'd like various pages to look at along with URL setup before the project code was started.

*ADD WIRE FRAMES HERE*

### Colour Scheme

As DH Bakes already existed I went with a pink and white colour scheme with hints of grey to accent the colour. I started off with a brighter pink but this flagged up with contrast issues so went darker to avoid these issues.

Image was created using [Coolors](https://coolors.co/ab0368-cb047c-ffffff-f0f0f0)

![Colour Scheme](readmedocs/screenshots/coolors.png)


### Database Schema

An entity relationship diagram was created using [DBeaver](https://dbeaver.io/) and shows the schemas for each of the models and how they are related.

*ADD ENTITY DIAGRAM HERE*


## Site Security

Decorators were added such as @login_required and HttpResponseForbidden to views to ensure certain pages and actions are restricted from users who may have worked out a URL path or bi-passed other security barriers.

These additions would mean messages or pages (403.html) would display to the user if they tried to get to a page that they shouldn't.

Example - Editing a Testimonial that is not owned by the user - this is when a user has entered the correct URL path to edit a testimonial they do not own.

![Unauthorised Access](readmedocs/screenshots/403-error.png)


Trying to add a product when you are not an admin user - this directs the user to sign in if they're not logged in, or displays a message if they are logged in:

![Error message](readmedocs/screenshots/security-error.png)

## Testing

Site testing can be found in [TESTING.md](https://github.com/philtipping31/DH-Bakes/blob/main/TESTING.md)


## Features

*ADD FEATURES HERE*

### Features not yet implemented


## Deployment and Setup

### Heroku

1. Create a Heroku App:

Log in or create an account on Heroku.
Click 'New' and then 'Create New App'.
Enter a unique name and select a region, then click 'Create App'.

2. Connect to GitHub:

In the Heroku dashboard, go to the 'Deploy' tab.
Choose 'GitHub' as the deployment method, find your repository, and click 'Connect'.

3. Set Config Vars:

Go to the 'Settings' tab and click 'Reveal Config Vars'.
Add the environment variables from env.py and other items added in settings.py that required.
Add DISABLE_COLLECTSTATIC and set it to 1 to disable, or 0 if the app is ready for static file collection.
Add all other relevant config vars to the site to ensure it operates correctly:

Deploy:

In the 'Deploy' tab, select the branch you want to deploy (usually main) and click 'Deploy Branch'.
Once deployed, click 'View' to see your live site.


### Local Deployment

#### Version Control

DH Bakes was created using the cloud IDE GitPod code editor and pushed to github.

The following git commands were used throughout development to push code to the remote repo:

git add . - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue, ready for the final step.

git push - This command was used to push all committed code to the repository on github.


### Forking

Fork a Repository:

Log in to GitHub (or create an account).
Navigate to the repository you want to fork.
Click the 'Fork' button in the top right corner.


### Cloning 

Clone a Repository:

Log in to GitHub (or create an account).
Navigate to the repository you want to clone.
Click the 'Code' button and choose to clone using HTTPS, SSH, or GitHub CLI. Copy the link provided.
Open your terminal and navigate to the directory where you want to clone the repository.
Run git clone and press enter.


### Creation of project

The base of this project was taken using the [CI Template](https://github.com/Code-Institute-Org/ci-full-template)

Clicking 'Use this template' > 'Create a new repository'


### Database

This project uses a PostgreSQL relational database from Code Institute.

To connect to the database:

Go to the Code Institute Database Maker
Create a database using the email address used to sign up for the Code Institute LMS.
The Database URL is sent to the email address.
Add the database URL as a variable to the project and make sure to keep it secret. This was added directly to Heroku config vars.


### AWS


This project uses AWS S3 to host images. Follow the steps below to set it up:

Step 1: Set Up AWS S3 Bucket

1. Create an AWS Account: Log in to your AWS account.
2. Search for S3: In the search bar, type 'S3' and click on the S3 service.
3. Create a New Bucket:
    - Click "Create Bucket."
    - Enter a bucket name.
    - Enable 'ACLs enabled' and select 'Bucket owner preferred.'
    - Uncheck 'Block all public access.'
    - Acknowledge the risks of public access by checking the box.
    - Leave other settings as default, then click "Create bucket."

Step 2: Enable Static Website Hosting

1. After creating the bucket, click on the bucket name to view details.
2. In the Properties tab, scroll to Static Website Hosting and click "Edit."
3. Enable static hosting, enter index.html for the Index document, and error.html for the Error document.
4. Save the changes.

Step 3: Configure CORS (Cross-Origin Resource Sharing)
1. Navigate to the Permissions tab.
2. Scroll down to CORS Configuration and click "Edit."
3. Add the following code and save changes:

[
  {
    "AllowedHeaders": ["Authorization"],
    "AllowedMethods": ["GET"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]


Step 4: Set a Bucket Policy

1. In the Permissions tab, scroll to Bucket Policy and click "Edit."
2. Open the Policy Generator in a new tab:
    - Select 'S3 Bucket Policy' as the policy type.
    - Enter * (wildcard) for the Principal.
    - Choose 'GetObject' for the action.
    - Copy the ARN (Amazon Resource Name) of your bucket from the previous tab and paste it into the ARN field.
    - Click "Add Statement" and then "Generate Policy."

3. Copy the generated policy and paste it into the Bucket Policy editor. Add /* at the end of the Resource value to allow access to all objects within the bucket. For example:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "YOUR_BUCKET_ARN/*"
        }
    ]
}

4. Save the policy.

Step 5: Edit Access Control List (ACL)

1. In the Permissions tab, go to Access Control List (ACL) and click "Edit."
2. Check the 'List' permission under "Everyone (public access)." Acknowledge the risks and save changes.


IAM (Identity and Access Management)

Step 1: Create a User Group
1. Search for 'IAM' in the AWS search bar and click on IAM.
2. In the left menu, click "User Groups" and select "Create Group."
3. Enter a group name and click "Create user group."

Step 2: Create a Policy

1. Go to Policies in the left menu and click "Create Policy."
2. In the JSON tab, choose Import Managed Policy and search for AmazonS3FullAccess.
3. After importing, add your bucket’s ARN twice to the Resource section: once with just the ARN and once with /* at the end. Example:

"arn:aws:s3:::yourbucket",
"arn:aws:s3:::yourbucket/*"

4. Name the policy and click "Create Policy."

Step 3: Attach Policy to User Group

1. In User Groups, click on your group and go to the Permissions tab.
2. Click "Add Permissions" → "Attach Policies."
3. Search for your newly created policy, check the box next to it, and click "Attach."

Step 4: Create a User

1. Go to Users and click "Create User."
2. Enter a username, select the previously created group, and complete the steps to create the user.

Step 5: Generate Access Keys

1. In the Users section, click on your new user and navigate to the Security Credentials tab.
2. Under Access Keys, click "Create Access Key."
3. Choose "Application running outside AWS," click "Create Access Key," and download the .csv file containing the key.
4. Use the values from the file for your Heroku environment variables:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY

The project is now configured to host images using AWS S3 with appropriate permissions and access controls.



### Stripe

This project uses Stripe in test mode to manage secure payments.

Steps to Connect to the Stripe API:

1. Sign In or Sign Up for a Stripe Account:

- Go to Stripe's website and either log into your existing account or create a new one.

2. Access API Keys:

- Navigate to the "Developers" section from the main menu.
- Under "API keys", locate and retrieve your test API keys.

3. Obtain the Required API Keys:

- You will need two keys to integrate Stripe with your project:

    STRIPE_PUBLIC_KEY: The publishable key (starts with pk).
    STRIPE_SECRET_KEY: The secret key (starts with sk).

- These keys should be added to your Gitpod environment variables before deployment and later to the Heroku config vars.

Handling Interrupted Payments with Stripe Webhooks:

To ensure payment consistency in case users exit the payment page prematurely or experience network issues, you should configure Stripe Webhooks:

1. Set Up Webhooks:

- Go to the "Developers" section in Stripe.
- Under "Webhooks", select "Add Endpoint".
- Provide the webhook URL for your project.
- Choose "Receive All Events" and click "Add Endpoint" to finalize.

2. Obtain the Webhook Signing Secret:

- Under the webhook details, you'll find a signing secret key (starts with wh).
- Add this key to your Gitpod variables and later to the Heroku config vars:

STRIPE_WH_SECRET: The webhook signing secret.


Stripe Integration in Your Django Project:

1. Install the Stripe Package:

- Add the Stripe package to your Django project.

2. Configure settings.py:

- Configure Stripe by adding the necessary API keys and settings in your settings.py file.

3. Include Stripe's JavaScript in Templates:

- Add Stripe's JavaScript library in your base HTML template to ensure that security features are available across the website.

4. Payment Form Integration:

- Follow Stripe's documentation to add the required JavaScript for accepting payments.
- Customize Stripe Elements (the payment UI) to match your website's design.


This ensures that the payment process is secure, integrated seamlessly into your website, and capable of handling interruptions efficiently.


### Google Mail (Gmail)

This project utilizes Gmail to manage email communications with users, specifically for account verification and order confirmation purposes.

To integrate the Gmail API:

1. Create a Gmail Account and Obtain API Key:

- Sign in or create a Google Gmail account.
- Access "Account Settings" by clicking the cog icon in the top-right corner.
- Go to the "Accounts and Import" section.
- Under "Change account settings," click on "Other Google Account settings."
- In the new settings page, click "Security" from the left menu.
- Enable 2-Step Verification by following the on-screen instructions to verify your account and password.
- After verifying, turn on 2-factor authentication (2FA).

2. Generate App Password:

- Return to the "Security" page and search fpr "App passwords."
- You may be prompted again to verify your password.
- Set "Mail" as the "App Type."
- Choose "Other (Custom name)" as the "Device Type" and enter a custom name, such as your project’s name.
- A 16-character password (API key) will be generated for you.

3. Configure Heroku:

- Add the following to your Heroku Config Vars:
EMAIL_HOST_PASS = your generated 16-character API key.
EMAIL_HOST_USER = your Gmail email address.



## Technologies and Programmes used

### Main Technologies

- HTML
- CSS
- Javascript (JQuery)
- Python (Django Framework)
- CI Database Maker for PostgreSQL Database

### Modules

- boto3==1.35.17 - The official AWS SDK for Python, enabling the integration of AWS services like S3 in Python applications.
- botocore==1.35.17 - A core library for AWS services, used internally by Boto3 to provide base operations and HTTP connections to AWS services.
- dj-database-url==0.5.0 - A Django utility for configuring database URLs in settings
- Django==4.2.7 - A Python web framework that allows quick development and clean design.
- django-allauth==0.54.0 - A Django app providing user registration, authentication, and third-party account integration.
- django-countries==7.2.1 - A Django app that provides a country field for models and forms
- django-crispy-forms==1.14.0 - A Django app for creating and managing forms with a more elegant and flexible layout.
- django-storages==1.14.4 - A Django package providing support for storing media and static files in cloud services like AWS S3
- gunicorn==23.0.0 - A Python WSGI HTTP server for UNIX that is widely used to serve Django applications in production environments due to its performance and ease of use.
- pillow==10.4.0 - A Python Imaging Library (PIL) fork that provides image processing capabilities such as opening, manipulating, and saving image files in various formats (JPEG, PNG, GIF, etc.).
- psycopg2==2.9.9 - A PostgreSQL adapter for Python, allowing Django and other Python applications to interact with PostgreSQL databases efficiently and securely.
- s3transfer==0.10.2 - A Python library that is part of Boto3 and provides optimized file transfers to and from Amazon S3, improving the efficiency of large uploads/downloads.
- sqlparse==0.5.1 - A non-validating SQL parser for Python, useful for formatting and parsing SQL queries. It’s often used in ORM systems like Django.

- stripe==10.9.0 - The official Python library for Stripe, enabling seamless integration with Stripe's payment and subscription services, allowing secure payment handling in web applications.


### External Programmes Used


## Credits and Acknowledgments

