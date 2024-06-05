from django.shortcuts import render


def show_prices(request):
    context = {
        'single_visit': {
            'adults_price': 400,
            'children_price': 400,
        },
        'subscription_90_8': {
            'adults_price': 3000,
            'children_price': 2700,
        },
        'subscription_90_12': {
            'adults_price': 3500,
            'children_price': 3200,
        },
        'subscription_60_8': {
            'adults_price': 2500,
            'children_price': 2200,
        },
        'subscription_60_12': {
            'adults_price': 3000,
            'children_price': 3700,
        },

        'individual_single_visit': {
            'adults_price': 600,
            'children_price': 800,
        },
        'individual_subscription_90_8': {
            'adults_price': 5000,
            'children_price': 4900,
        },
        'individual_subscription_90_12': {
            'adults_price': 6000,
            'children_price': 5600,
        },
        'individual_subscription_60_8': {
            'adults_price': 3000,
            'children_price': 4000,
        },
        'individual_subscription_60_12': {
            'adults_price': 5000,
            'children_price': 5600,
        },
    }
    return render(
        request,
        'prices/prices.html',
        context
    )
