from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from django.contrib import messages


@login_required(login_url='login_page')
def home(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required(login_url='login_page')
def add_product(request):

    if not request.user.role=='admin':
        messages.error(request, "Access Denied ❌")
        return redirect('home')

    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            price=price,
            vechicle_image=image,
            category=category
        )

        messages.success(request, "Product Added Successfully ✅")
        return redirect('home')

    return render(request, 'add_product.html', {'categories': categories})

@login_required(login_url='login_page')
def edit_product(request, id):

    if not request.user.role == 'admin':
        return redirect('home')

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect('home')

    categories = Category.objects.all()

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.vechicle_image = request.POST.get('image')

        category_id = request.POST.get('category')
        product.category = Category.objects.get(id=category_id)

        product.save()
        return redirect('home')

    return render(request, 'add_product.html', {
        'product': product,
        'categories': categories
    })

@login_required(login_url='login_page')
def delete_product(request, id):
    if request.method == "POST":
        try:
            product = Product.objects.get(id=id)
            product.delete()
        except Product.DoesNotExist:
            pass

    return redirect('home')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def add_to_cart(request, id):

    if not request.user.is_authenticated:
        messages.error(request, "⚠️ Please login first to add items to cart!")
        return redirect('login_page')

    if request.method == "POST":
        cart = request.session.get('cart', {})

        if str(id) in cart:
            cart[str(id)] += 1
        else:
            cart[str(id)] = 1

        request.session['cart'] = cart

        messages.success(request, "✅ Product added to cart successfully!")

    return redirect(request.META.get('HTTP_REFERER', 'home'))

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for id, qty in cart.items():
        product = Product.objects.get(id=id)

        # ✅ REMOVE COMMA BEFORE CONVERT
        price = int(str(product.price).replace(',', ''))

        product.qty = qty
        product.total_price = price * qty

        total += product.total_price
        products.append(product)

    return render(request, 'cart.html', {
        'products': products,
        'total': total
    })

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]   # ✅ அந்த product மட்டும் remove

    request.session['cart'] = cart
    return redirect('cart')

def indian_format(amount):
    return "{:,}".format(amount)

