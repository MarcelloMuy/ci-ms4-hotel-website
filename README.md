# Hotel Booking System with Django

## Introduction

Welcome to my fourth milestone project. In this project, I create a hotel booking system where users can register an account, book a room, and manage their bookings.  
It will use the Django framework, Python, HTML, and JavaScript languages.

This project aims to show the use of CRUD functionality (Create, Read, Update, Delete). After registering an account, the user can create, read, update and delete their hotel booking.

A live website can be found [here](https://my-hotel-project.herokuapp.com/).

![website preview](readme_assets/images/website_preview.png)

## Table of Contents

- [1 UX](#1-ux)
  - [Strategy](#strategy)
    - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [User Expectations](#user-expectations)
    - [User Stories](#user-stories)
    - [Scope](#scope)
      - [Phase 1](#phase-1)
      - [Phase 2](#phase-2)
  - [Structure](#structure)
    - [Data Model](#data-model)
  - [Wireframes](#wireframes)
    - [Mobile](#mobile)
    - [Desktop](#desktop)
  - [Surface](#surface)
    - [Colours](#colours)
    - [Typography](#typography)
- [2 Features](#2-features)
  - [All Pages](#all-pages)
  - [Home Page](#home-page)
  - [Our Rooms Page](#our-rooms-page)
  - [Book Now Page](#book-now-page)
  - [My Bookings Page](#my-bookings-page)
  - [Register page](#register-page)
  - [Sign in/out](#sign-in/out)
- [3 Technologies Used](#3-technologies-used)
- [4 Testing](#4-testing)
- [5 Development Cycle](#5-development-cycle)
- [6 Deployment](#6-deployment)
- [7 End Product](#7-end-product)
- [8 Known Bugs](#8-known-bugs)
- [9 Credits](#9-credits)

## 1 UX

[Go to the top](#table-of-contents)

Traveling is by far the thing that I like to do most, and a big part of the trip is about where you are staying.
When you visit a new city, you need a place to stay. The easiest way to book a hotel room is online.

This project will demonstrate how simple and easy a hotel booking system can be.

## Strategy

[Go to the top](#table-of-contents)

### Project Goals

[Go to the top](#table-of-contents)

This project aims to allow users to register a new account, perform a sign-in and sign-out action, book a hotel room, and manage their bookings (see past and future bookings, make an update on an upcoming booking, or cancel the booking).

### User Goals

[Go to the top](#table-of-contents)

First Time Visitor Goals

- As a first-time visitor, I want to book a room for a chosen date.
- As a first-time visitor, I want to view pictures of the hotel room and prices per night.
- As a first-time visitor, I want to view information about the hotel so I can decide to book a room.
- As a first-time visitor, I want to get the hotel's contact information.

Returning Visitor Goals

- As a Returning Visitor, I want to view my bookings details.
- As a Returning Visitor, I want to update an upcoming booking.
- As a Returning Visitor, I want to cancel an upcoming booking.

Frequent User Goals

- As a Frequent User, I want to see my past bookings or book a new stay.

### User Expectations

[Go to the top](#table-of-contents)

 The following user expections were considered while designing the site:

- The menu is clear to read and navigate.
- The site structure is designed to be simple and easy to use.
- The user interface is easy to navigate.
- The website is responsive on all devices.
- All images on the website are of high quality.
- Easy to find contact information and hotel location.

### User Stories

[Go to the top](#table-of-contents)

I use GitHub kanban board to log all user stories for my project. It was an excellent tool to visualize what to focus on first.
The user stories would go directly to the "To Do" lane when created. I would move them to the "In progress" lane when working on the story, and once completed, I would move them to the "Done" lane.

![user_story_board](readme_assets/images/user_story_board.png)

### Scope

[Go to the top](#table-of-contents)

I decided to divide this project into two phases. I include the features that I have identified as a minimum viable product in the first phase.
In the second, I included the features that I found would make a good improvement for the web application.

### Phase 1

[Go to the top](#table-of-contents)

- Display rooms pictures
- Display hotel information, including location and contact
- Allow users to register a new account
- Responsive design
- Ability to create a booking
- Ability to update a booking
- Ability to cancel a booking
- Display past bookings
- Display alerts for each step of CRUD operations

### Phase 2

[Go to the top](#table-of-contents)

- Register account email confirmation
- Email confirmation for new bookings
- Create a new Django view to confirm booking deletion instead of using a JavaScript function
- Calculate the total of the booking and display it to the user
- A button on the "Update booking" page to go back to "My Bookings" page if the user changes their mind.

## Structure

[Go to the top](#table-of-contents)

- All pages of this project are responsive using different screen sizes. In addition, fonts and color scheme are consistent throughout all pages, guaranteeing the best user experience.
- Navbar is positioned at the top, and Footer at the bottom of all pages.
- Buttons have self-describing text for easy navigation.

### Data Model

[Go to the top](#table-of-contents)

- Planned database structure:

![database_model](readme_assets/images/data_model.png)

- Final database structure:

```python
class Booking(models.Model):
    ''' Model for user bookings '''
    today = date.today()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    created_on = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(15), MinValueValidator(1)])
    check_in_date = models.DateField(default=date.today)
    number_of_nights = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(30), MinValueValidator(1)])
    TYPE_OF_ROOM_CHOICES = [
        ('Twin', 'Twin Room'),
        ('Double', 'Double Room'),
        ('Family', 'Family Room'),
    ]
    type_of_room = models.CharField(
        max_length=15,
        choices=TYPE_OF_ROOM_CHOICES,
        blank=False,
        default='Double'
        )

    ''' Display objects using the check-in date'''
    def __str__(self):
        return str(self.check_in_date)

    class Meta:
        """ Meta class used for organizing bookings by check-in date """
        ordering = ['check_in_date']
```

## Wireframes

[Go to the top](#table-of-contents)

### Mobile

Home Page mobile:

![home_page_mobile](readme_assets/wireframes/mobile_home_page.png)

Our Rooms Page mobile:

![ours_rooms_page_mobile](readme_assets/wireframes/mobile_our_rooms_page.png)

My bookings Page mobile:

![my_bookings_page_mobile](readme_assets/wireframes/mobile_my_bookings.png)

Book Now Page mobile:

![book_now_page_mobile](readme_assets/wireframes/mobile_book_now.png)

Sign in/out and Register Page mobile:

![sign_in/out_and_register_page_mobile](readme_assets/wireframes/mobile_sign_in_out.png)

### Desktop

[Go to the top](#table-of-contents)

Only the index page and my bookings page have a difference in design compared to the mobile version.

Index Page desktop top:

The index page has a bigger hero image covering most of the page, a margin on both sides of the page, and the hotel info is displayed on top of the hero image.

![index_page_desktop_top](readme_assets/wireframes/desktop_index_top.png)

Index Page desktop bottom:

![index_page_desktop_bottom](readme_assets/wireframes/desktop_index_bottom.png)

My Bookings Page desktop:

My bookings page displays booking cards in rows of up to four cards.

![my_bookings_page_desktop](readme_assets/wireframes/desktop_my_bookings.png)

## Surface

[Go to the top](#table-of-contents)

### Colours

I used ColorSpace to generate this colour scheme.

![colour_scheme](readme_assets/wireframes/colour_scheme.png)

The following colors were used to design this website:

- #E9DBC9
- #005B4B
- #e9dbc9c9
- #BCBEA9
- #f8f9fa

### Typography

[Go to the top](#table-of-contents)

I decided to use Google fonts "Karla" for all pages with "Sans Serif" as the backup font.

Google fonts link [here](https://fonts.google.com/specimen/Karla?query=karla)

## 2 Features

[Go to the top](#table-of-contents)

### All Pages

Navigation bar:

- Is placed at the top of the screen at all times
- If the user is logged in, the "Sign-in" link will change to "Sign out" and the "Register" link will disappear.
- The link in the navbar will have a class attribute to show as active when the user is the specific page. The "Home" and "Contact US" links will be activated together as both links belong to the same page but in different sections.
- The restaurant logo works as a link for the home page.
- In the mobile version, the logo is positioned at the center of the navbar, and a hamburger icon is placed on the left.
- All links are displayed when the hamburger icon is clicked, as shown below.

Navbar Logged:

![navbar_logged](readme_assets/features/navbar_logged.png)

Navbar not Logged:

![navbar_not_logged](readme_assets/features/navbar_not_logged.png)

Navbar showing "Our Rooms" link active:

![navbar_active_link](readme_assets/features/navbar_active_link.png)

Navbar mobile:

![navbar_mobile](readme_assets/features/mobile_navbar.png)

Navbar hamburger icons mobile:

![navbar_hamburger_icons_mobile](readme_assets/features/mobile_navbar_hamburger_icon.png)

Footer:

- The footer is placed at the bottom of the screen at all times.
- It has three social links placed at the center of the page that opens in a new page.

![footer](readme_assets/wireframes/footer.png)

### Home Page

[Go to the top](#table-of-contents)

- The Home page has a short description of the hotel and two action buttons.
- A button for booking a room and a button that will send the user to the "Our Rooms" page, where they can see information and pictures of the rooms.
- For larger screens the hotel information is displayed inside a container on top of the hero image to increase readability.

![features_index_hero](readme_assets/features/features_index_hero.png)

- Below the hero image, you can find an iframe containing the google maps location of the hotel.

![features_index_map](readme_assets/features/features_index_map.png)

- At the bottom of the page, you can find the hotel's contact information: address, email and phone number.

![features_index_contact](readme_assets/features/features_index_contact.png)

### Our Rooms Page

[Go to the top](#table-of-contents)

- On the "Our Rooms" page, you will find pictures of the three types of rooms the hotel has: Double Room, Twin Room and Family Room.
- Under each picture, there is the price per night for the room and a short description of the room.

![features_double_room](readme_assets/features/features_double_room.png)
![features_twin_room](readme_assets/features/features_twin_room.png)
![features_family_room](readme_assets/features/features_family_room.png)

### Book Now Page

[Go to the top](#table-of-contents)

- If the user is not logged in, a call for sign-in is displayed on the page.

![features_not_auth_book_form](readme_assets/features/features_not_auth_book_now.png)

On the "Book Now" page, the user will be asked to fill up a form with:

![features_book_now](readme_assets/features/features_book_now.png)

- Check-in date (date must be for the next day onwards)
- Number of nights (up to 30 nights)
- Number of guests (up to 15 guests)
- Type of room (Choose between double, twin or family rooms)
- When clicking the "Book Now" button thank you page will be displayed.
- On the "thank you" page, the user can find a button to manage bookings.

![features_thank_you](readme_assets/features/features_thank_you.png)

- An alert error message will show if the user inserts any invalid information.

![features_date_error_alert](readme_assets/features/features_date_error_alert.png)
![features_nights_error_alert](readme_assets/features/features_nights_error_alert.png)
![features_guests_error_alert](readme_assets/features/features_guests_error_alert.png)

### My bookings Page

[Go to the top](#table-of-contents)

- If the user is not logged in, a call for sign-in is displayed on the page.

![features_my_bookings_not_auth](readme_assets/features/features_my_bookings_not_auth.png)

On the "My bookings" page, the bookings are separated into two categories: Upcoming and Past.

- If the user has no bookings, a message is displayed instead of the cards.

![features_my_bookings_no_bookings](readme_assets/features/features_my_bookings_no_bookings.png)

- For upcoming bookings, the card will have two buttons at the bottom for updating and deleting the booking.
- The cards are ordered by the nearest check-in date.

Bookings will be displayed in rows of up to four cards, depending on the screen size.
Each booking is displayed on a card containing:

- Check-in date
- Number of Nights
- Room Type
- Number of Guests

![features_my_bookings_upcoming](readme_assets/features/features_my_bookings_upcoming.png)
![features_my_bookings_past](readme_assets/features/features_my_bookings_past.png)

- If the user clicks on the "Update" button, the "Update Booking" page will show containing a form to update the booking.

![features_update_booking](readme_assets/features/features_update_booking.png)

- An alert will show when the update is done.

![features_update_booking_alert](readme_assets/features/features_update_booking_alert.png)

- If the user clicks on the "Cancel" button, a JavaScript onclick function will be called, and a popup to confirm the cancellation will show.

![features_delete_booking_confirmation](readme_assets/features/features_delete_booking_confirmation.png)

- An alert will show when the cancelation is done.

![features_delete_booking_alert](readme_assets/features/features_delete_booking_alert.png)

### Register Page

[Go to the top](#table-of-contents)

On the registration page, the user will need to fill up a form containing:

- Username
- Email(optional)
- password
- password(again)

![features_sign_up](readme_assets/features/features_sign_up.png)

When clicking the sign-up button, two alerts will show.

![features_registration_alerts](readme_assets/features/features_registration_alerts.png)

Because this project doesn't have an e-mail confirmation management system yet.
This line of code was added to settings.py.

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

The e-mail confirmation is handled in the console, as seen below.

![features_console_email_confirmation](readme_assets/features/features_console_email_confirmation.png)

### Sign in/out

[Go to the top](#table-of-contents)

On "Sign in" page, the user will need to fill up a form containing:

- Username
- Password

![features_sign_in](readme_assets/features/features_sign_in.png)

An alert will show once the sign-in is completed.

![features_sign_alert](readme_assets/features/features_sign_in_alert.png)

If the user clicks on the sign-out link in the navigation bar, the "Sign out" page will be displayed.

![features_sign_out](readme_assets/features/features_sign_out.png)

If the user confirms the sign-out, an alert will show.

![features_sign_out_alert](readme_assets/features/features_sign_out_alert.png)

## 3 Technologies Used

[Go to the top](#table-of-contents)

- [HTML5](https://en.wikipedia.org/wiki/HTML)
  - The project uses HyperText Markup Language.
- [CSS3](https://en.wikipedia.org/wiki/CSS)
  - The project uses Cascading Style Sheets.
- [Django 3.2](https://en.wikipedia.org/wiki/Django_(web_framework))
  - Django was used as the web framework to develop this project.
  - Below you can find the Django libraries and packages used in this project.
    - [Gunicorn](https://gunicorn.org/)
      - Used to run server on heroku
    - [Dj_database_url](https://pypi.org/project/dj-database-url/)
      - Utility to utilize the DATABASE_URL environment variable to configure Django application.
    - [Psycopg2](https://pypi.org/project/psycopg2/)
      - Library to connect to PostgreSQL
    - [Cloudinary](https://en.wikipedia.org/wiki/Cloudinary)
      - Library to host pictures on Heroku
    - [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
      - Library used for authentication and registration
    - [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
      - Library used to format forms in Django.
    - [WhiteNoise](http://whitenoise.evans.io/en/stable/)
      - Allows web app to serve its own static files.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - The project uses JavaScript.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - The project uses Python.
- [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - The project uses Bootstrap 4.6.
- [Cloudinary](https://en.wikipedia.org/wiki/Cloudinary)
  - Cloudinary was used as cloud-based service to store the images used in this project.
- [PostgreSQL](https://www.postgresql.org/)
  - The project uses PostgreSQL as a database.
- [Gitpod](https://www.gitpod.io/)
  - The project uses Gitpod.
- [Chrome](https://www.google.com/intl/en_uk/chrome/)
  - The project uses Chrome to debug and test the source code using HTML5.
- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to create the wireframes during the design process.
- [Canva](https://en.wikipedia.org/wiki/Canva)
  - Canva was used as the image provider for this project.
- [Google Fonts](https://fonts.google.com/)
  - Google fonts were used to import the "Karla" font into the style.css file which is used on all pages throughout the project.
  [Heroku](https://en.wikipedia.org/wiki/Heroku)
  - Heroku was useed as a cloud platform service for this project.
- [GitHub](https://github.com/)
  - GitHub was used to store the project's code after being pushed from Git.

## 4 Testing

[Go to the top](#table-of-contents)

### Chrome DevTools

I used the developer tools to debug my code and try different styles. When something in my code didn’t behave as I expected, I would inspect it and try out other solutions. Finally, when I was happy with the results, I would copy and paste the code into the project file.

### Responsive Tools

I used [Am I Responsive](http://ami.responsivedesign.is) in conjunction with Chrome DevTools to check how the website behaved in different screen sizes.

### W3C Validator Tools

#### HTML

I used [W3C Markup](https://validator.w3.org/) to check my code for any errors in the HTML pages.

- All pages were tested using the heroku live link
- I found an error within my index.html iframe.

![w3c_index_iframe_error](readme_assets/error_images/w3c_index_iframe_error.png)

- This error was fixed by moving all the iframe src path to one single line.

![w3c_index_iframe_error_fix](readme_assets/error_images/w3c_index_iframe_error_fix.png)

- All other template pages came back with no errors.

#### CSS

I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) to check my code for any errors in my style.css page.

I had no errors in my CSS file:
![w3c_css_validation](readme_assets/error_images/w3c_css_validation.png)

### JavaScript

I used [JS Hint](https://jshint.com/) to check for any errors in the base.html file JavaScript script tag. JS Hint showed warnings below:

![js_hint_error](readme_assets/error_images/js_error.png)

As these warnings were related to the esversion, they were ignored.

### Python

I used [PEP8 online](http://pep8online.com/) to check for errors within my Python files.

- views.py:

  Three errors were found in this file

![Pep8 Views](readme_assets/error_images/pep8_views_errors.png)

All errors were fixed by removing trailing space and whitespace from the specific lines.

![Pep8 Views Fix](readme_assets/error_images/pep8_views_errors_fix.png)

- settings.py:

  Multiple  "line too long" errors were found in this file

![Pep8 Settings](readme_assets/error_images/pep8_settings_errors.png)

I decided to make no changes to the settings.py as the errors were in a critical part of the code.

- models.py:

  No errors were found

![Pep8 Models](readme_assets/error_images/pep8_models_no_error.png)

- forms.py:

  No errors were found

![Pep8 Forms](readme_assets/error_images/pep8_forms_no_error.png)

- urls.py

  No errors were found

![Pep8 URLs](readme_assets/error_images/pep8_urls_no_error.png)

## Manual Testing

[Go to the top](#table-of-contents)

I