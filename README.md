# Book My Room (OYO Clone)

A **hotel booking and listing platform** inspired by OYO, built using **Python-Django**. This project showcases hotel listings, user & hotel vendor management, hotel booking, and more.

---

## 📋 Table of Contents
- [✨ Features](#features)
- [🛠️ Tech Stack](#tech-stack)
- [⚡️ Getting Started](#getting-started)
  - [Installation](#installation)
- [🌐 Features in Detail](#features-in-detail)
- [📁 Project Structure](#project-structure)
- [💻 Demo](#demo)
- [⚡️ Contributing](#contributing)
- [🌱 Future Scope](#future-scope)
- [👥 Author](#author)

---

## ✨ Features
- ✅ User Registration & Email Verification  
- ✅ Login with OTP for enhanced security  
- ✅ Hotel Owner/Vendor Registration  
- ✅ Add, Edit, and Finalize Hotels  
- ✅ Upload and Serve Media (hotel images)  
- ✅ Static File Handling and Templates  
- ✅ Integrate Rich Text Editor (Flora Editor) for hotel descriptions  
- ✅ Hotel Listing and Booking Logic  

---

## 🛠️ Tech Stack
| Component          | Details                          |
|--------------------|----------------------------------|
| **Backend**        | Python-Django                    |
| **Database**       | SQL (SQLite)                     |
| **Frontned**       | HTML, CSS, JS, BootStrap         |
| **Email Service**  | Django's Email Framework(SMTP)   |
| **Template Engine**| Django Templates                 |
| **Editor**         | Flora Editor (Rich Text Editing) |


---

### ⚙️ Installation
1. **Clone the Repository**  
    ```bash
    git clone https://github.com/your-username/django-oyo-clone.git
    cd django-oyo-clone
    ```

2. **Create a Virtual Environment**  
    ```bash
    python -m venv venv
    source venv/bin/activate    # Linux/Mac
    venv\Scripts\activate       # Windows
    ```

3. **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup `.env` File**  
    Create a `.env` file in the root directory and add:

    ```
    DJANGO_SECRET_KEY=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    ```

5. **Run Migrations**  
    ```bash
    python manage.py migrate
    ```

6. **Create Superuser**  
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**  
    ```bash
    python manage.py runserver
    ```

---

## 🌐 Features in Detail
- 🏨 **Readme Section:** Displays guides and steps about setting up the project.
- 🔐 **Authentication:** Registration, Email Verification, and Login with OTP.
- 🗄️ **Vendor Dashboard:** Logic for adding/editing hotels and updating details.
- 📃 **Finalizing Hotels:** Final review and publishing listing.
- 🖋️ **Flora Editor Integration:** Rich text editor for hotel descriptions.


---

## 💻 Demo
*(Add a link or screenshots of your running site if available.)*

---

## ⚡️ Contributing
Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-name`)  
3. Push changes (`git push origin feature-name`)  
4. Open a Pull Request  

---

## 🌱 Future Scope
- 🌍 **Deployment:** Deploy the web-application.
- 💳 **Payment Integration:** Integrate online payments (Razorpay, Stripe).
- 🛠️ **Advanced Features:** 
  - Reviews and ratings for hotels.
  - Dashboard analytics for vendors & admin.
  - Push notifications and alerts.


---

## 👥 Author
👨‍💻 Created by [Aakash Jha]
