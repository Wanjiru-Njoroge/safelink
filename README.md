#### **Overview**
Safelink is a secure, user-friendly platform designed to provide help and support for individuals in distress. 
It connects users with nearby resources such as NGOs, shelters, and legal aid services, while offering features for 
secure reporting and quick exits in case of emergencies. The platform ensures privacy and accessibility for all users.

#### **Features**
1. **Location Services**
Find Nearby Resources:
Safelink integrates with mapping services to locate nearby support centers based on the user’s location.
Admin Management:
Admins can add, edit, or remove resource locations through an intuitive admin panel.

2. **Secure and Anonymous Reporting**
Users can report incidents without logging in or providing personal information.
Reports are encrypted during transmission and securely stored to maintain user privacy.
Optional fields allow users to provide contact details if they want follow-up assistance.

3. **Resource Directory**

4. **Quick Exit**
A safety feature that allows users to leave the platform instantly.
Redirects to a neutral website to prevent detection.

#### **Technology Stack**
**Frontend**: HTML, CSS, JavaScript
**Backend**: Django (Python Framework)
**Database**: Mysql
**APIs**:  and mapping services

#### **Getting Started**
1. **Installation**
Clone the repository:

````
git clone https://github.com/yourusername/safelink.git
cd safelink
````
Install dependencies:
````
pip install -r requirements.txt

````
Set up the database:
````
python manage.py migrate
````
Start the development server:

````
python manage.py runserver
````
Access the application in your browser at:
````
http://127.0.0.1:8000/

````
2. Admin Panel
Create a superuser to manage the platform:
````
python manage.py createsuperuser
````
Log in to the admin panel at:
````
http://127.0.0.1:8000/admin/
````
Add or manage resource locations, review reports, and ensure the platform remains updated.


#### **Usage**
**Users:**
Locate nearby help resources based on your location.
Submit incident reports securely and anonymously.
Quickly exit the platform in emergencies.

**Admins:**
Manage resources and ensure accurate information is available for users.
Oversee submitted reports while maintaining user privacy.

## **Contributing**
We welcome contributions to enhance Safelink! To contribute:
Fork the repository.
Create a new branch for your feature:
````
git checkout -b feature-name
````
Commit your changes:
````
git commit -m "Add your feature description here"
````
Push your branch:
````
git push origin feature-name

````
Open a pull request for review.


## **Future Plans**
**Incident hotspot mapping using heatmaps.**
**Automated resource matching based on report details.**
**Multilingual support to reach a broader audience.**

License
Safelink is open-source software licensed under the MIT License.

   



