from flask import render_template, request, redirect, url_for, flash
from models import db, Product, Order
import app as app_module

# Get the app instance from the module
app = app_module.app

@app.route('/')
def index():
    print("Index route called")  # Debug print
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        new_product = Product(name=name, price=price, stock_quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_product.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.stock_quantity = int(request.form['quantity'])
        
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('update_product.html', product=product)

@app.route('/delete/<int:id>')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/report')
def report():
    low_stock = Product.query.filter(Product.stock_quantity < 5).all()
    total_products = Product.query.count()
    total_value = db.session.query(db.func.sum(Product.price * Product.stock_quantity)).scalar() or 0
    
    return render_template('report.html', 
                         low_stock=low_stock,
                         total_products=total_products,
                         total_value=total_value)

@app.route('/orders')
def orders():
    all_orders = Order.query.all()
    return render_template('orders.html', orders=all_orders)

print("Routes loaded successfully!")  # Debug print