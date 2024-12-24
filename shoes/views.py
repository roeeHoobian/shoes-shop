# shoes/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Shoe
from .forms import ReviewForm


def show_homepage(request):
    return render(request,'home.html')

def shoes_list(request):
    # Retrieve all shoes from the database
    shoes = Shoe.objects.all()

    # Pass the shoes to the template
    return render(request, 'shoes/shoes_list.html', {'shoes': shoes})

def shoe_details(request, id):
    shoe = get_object_or_404(Shoe, id=id)
    reviews = shoe.reviews.all()  # Retrieve all reviews for the shoe
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.shoe = shoe
            review.save()
            return redirect('shoe_details', id=id)  # Redirect to refresh the page

    return render(request, 'shoes/shoe_details.html', {
        'shoe': shoe,
        'reviews': reviews,
        'form': form,
    })

def about(request):
    return render(request, 'about.html')
