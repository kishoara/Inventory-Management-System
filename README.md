# Inventory-Management-System

A web-based Inventory Management System that allows a company to manage products, suppliers, sales, and stock levels efficiently.

# Inventory Management System

A web-based Inventory Management System built with Flask that allows companies to manage products, suppliers, sales, and stock levels efficiently.

## Features

- ✅ Add, update, and delete products
- ✅ Track stock quantities and prices
- ✅ View inventory reports
- ✅ Low stock alerts
- ✅ Order management
- ✅ Clean and responsive UI

## Technologies Used

- **Backend:** Flask, SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Python Version:** 3.x

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/Inventory-Management-System.git
cd Inventory-Management-System
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python app.py
```

4. Open your browser and navigate to

```
http://127.0.0.1:5000/
```

## Project Structure

```
Inventory-Management-System/
│
├── app.py                 # Main application file
├── models.py              # Database models
├── routes.py              # Application routes
├── requirements.txt       # Project dependencies
│
├── static/
│   └── style.css         # CSS styles
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add_product.html
│   ├── update_product.html
│   ├── report.html
│   └── orders.html
│
└── database.db           # SQLite database (created on first run)
```

## Usage

### Adding Products

1. Click on "Add Product" in the navigation
2. Fill in product name, price, and quantity
3. Click "Add Product" to save

### Managing Inventory

- View all products on the home page
- Update product details by clicking "Edit"
- Delete products by clicking "Delete"

### Reports

- View low stock items
- See total inventory value
- Track total number of products

## Demo

[Add your demo video here]

## Screenshots



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## Acknowledgments

- Flask documentation
- SQLAlchemy documentation
