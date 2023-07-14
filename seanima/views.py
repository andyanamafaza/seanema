import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.contrib.humanize.templatetags.humanize import intcomma
from random import shuffle
from .models import UserProfile, TicketTransaction

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        age = request.POST['age']
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, balance=0, age=age, name=name)
        login(request, user)
        return redirect('index')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def fetch_movie_data():
    response = requests.get('https://seleksi-sea-2023.vercel.app/api/movies')
    return response.json()

def index(request):
    movies = fetch_movie_data()
    shuffled_movies = list(movies)
    shuffle(shuffled_movies)
    context = {
        'movies': shuffled_movies,
        'mov': movies,
    }
    return render(request, 'index.html', context)

def movie_detail(request, movie_title):
    movies = fetch_movie_data()
    movie = next((movie for movie in movies if movie['title'] == movie_title), None)
    return render(request, 'movie_detail.html', {'movie': movie})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def top_up_balance(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        user_profile.deposit_balance(amount)
        return redirect('index')


@login_required
def withdraw_balance(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        if(amount > user_profile.balance or amount > 500000):
            return redirect('index')
        user_profile.withdraw_balance(amount)
        return redirect('index')

@login_required
def book_ticket(request, movie_title):
    movies = fetch_movie_data()
    movie = next((movie for movie in movies if movie['title'] == movie_title), None)

    if movie is None:
        return HttpResponseNotFound("Movie not found.")

    booked_seats = TicketTransaction.objects.filter(movie_title=movie['title']).values_list('seat_numbers', flat=True)
    available_seats = [i for i in range(1, 65) if str(i) not in ','.join(booked_seats)]
    all_seats = [i for i in range(1, 65)]

    if request.method == 'POST':
        user_profile = request.user.userprofile
        selected_seats = request.POST.getlist('seat')
        if (
            len(selected_seats) > 6
            or any(int(seat) not in available_seats for seat in selected_seats)
            or user_profile.age < movie['age_rating']
        ):
            return redirect('book_ticket', movie_title=movie_title)

        total_cost = len(selected_seats) * movie['ticket_price']
        if user_profile.balance < total_cost:
            return redirect('top_up_balance')

        user_profile.balance -= total_cost
        user_profile.save()

        TicketTransaction.objects.create(
            user=request.user,
            movie_title=movie['title'],
            seat_numbers=selected_seats,
            total_cost=total_cost
        )
        return redirect('transaction_history')
    
    context = {
        'movie': movie,
        'available_seats': available_seats,
        'all_seats': all_seats,
    }

    return render(request, 'book_ticket.html', context)


@login_required
def cancel_ticket(request, transaction_id):
    ticket = TicketTransaction.objects.get(pk=transaction_id)
    user_profile = request.user.userprofile
    user_profile.deposit_balance(ticket.total_cost)
    ticket.delete()
    return redirect('transaction_history')


@login_required
def transaction_history(request):
    transactions = TicketTransaction.objects.filter(user=request.user)
    for transaction in transactions:
        transaction.total_cost = f"Rp. {intcomma(transaction.total_cost)}"
    return render(request, 'transaction_history.html', {'transactions': transactions})
