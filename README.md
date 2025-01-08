# Magical Realm eBay

Magical Realm eBay is a Django-powered marketplace for magical items, designed as a learning project to explore the capabilities of Django while creating an engaging platform for virtual trading. Users can register, list magical items for sale, browse categories, manage shopping carts, and purchase items.

## Features

- **User Authentication**: Register, log in, log out, and manage profiles.
- **Magical Items**: Create, view, and manage listings for magical items.
- **Categories**: Browse items by categories like Potions, Weapons, etc.
- **Shopping Cart**: Add items to the cart, view the cart, and purchase items.
- **Dynamic UI**: Styled with Bootstrap and custom CSS for a responsive, clean interface.
- **Validation**: Custom validators for user age and phone number.
- **Messages**: Feedback to users during operations like profile updates, purchases, etc.

## Project Structure

magical_realm_ebay/
├── accounts/                # User authentication and profiles
├── items/                   # Magical item management
├── marketplace/             # Homepage, search, and category views
├── shopping_carts/          # Shopping cart functionality
├── static/                  # CSS, images, and other static files
├── templates/               # Base and shared templates
└── manage.py                # Django management script


## Requirements

This project uses the following Python dependencies:

- `asgiref==3.8.1`
- `crispy-bootstrap5==2024.10`
- `Django==5.1.3`
- `django-crispy-forms==2.3`
- `django-profanity-filter==0.2.1`
- `inflection==0.5.1`
- `pillow==11.0.0`
- `python-dotenv==1.0.1`
- `sqlparse==0.5.2`
- `typing_extensions==4.12.2`

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/magical_realm_ebay.git
   cd magical_realm_ebay
2. **Set Up the Virtual Environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
3. **Install Requirements**
    ```bash
    pip install -r requirements.txt
4. **Set Up the Database**
    ```bash
    python manage.py migrate
5. **Load Sample Data (Optional)** Load initial data for categories and items.
    ```bash
    python manage.py loaddata accounts/fixtures/users.json
    python manage.py loaddata items/fixtures/categories.json
    python manage.py loaddata items/fixtures/items.json
6. **Run the Development Server**
    ```bash
    python manage.py runserver
7. **Access the App** Open your browser and navigate to http://127.0.0.1:8000.

## Tests
Run tests for all apps to ensure the functionality is working as expected:

    python manage.py test

## Environment Variables
The project uses a .env file for sensitive settings. Create a .env file in the root directory and add the following variables:

    SECRET_KEY=your-secret-key
    DEBUG=True

## URM Diagram
![URL Diagram](https://github.com/dci-fbw-p-24-e03/FriederikeDjangoProject/blob/main/magical_realm_ebay/exomarket_friederike.png)

## Future Enhancements
- Add Testing
- Add Middleware and Logging
- Add Custom Commands
- Add transactional email notifications.
- Integrate payment gateway simulation.
- Add search filtering by item attributes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Developed as a learning project for Django.
- Inspired by fantasy trading concepts from gaming.