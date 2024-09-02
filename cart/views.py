from django.shortcuts import render

# view for cart 
def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    return render(request, "cart_add.html", {})

def cart_delete(request):
    return render(request, "cart_delete.html", {})

def cart_update(request):
    return render(request, "cart_update.html", {})