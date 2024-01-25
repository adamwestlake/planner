from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, F
from django.forms import modelform_factory
from django.http import HttpResponse
from teams.models import User, Location, Role
from datetime import datetime
from .forms import UserSelectionForm

def main(request):
    current_time = datetime.now()
    locations = Location.objects.all()
    user_data_by_location = {}

    for location in locations:
        users_at_location_sorted = User.objects.filter(location=location).order_by('role', 'name')
        user_data_by_location[location] = users_at_location_sorted

    return render(request, 'home.html', {'name': 'Adam','num_employees': getNumberOfEmployees(), 'num_teams': getTeams(), 'form': new(request), 'user_data_by_location': user_data_by_location,  'current_time': current_time})

def getNumberOfEmployees():
    num_employees = User.objects.count()
    return(num_employees)
def getTeams():
    num_teams = Location.objects.count()
    return(num_teams)

UserForm = modelform_factory(User, exclude=[])
def new(request):
    response = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            response = "Successfully registered User"
        else:
            response = "Failed to register User"
            
    else:
        form = UserForm()
    return render(request, "new.html", {'form': form, 'response': response})


def delete_user(request):
    
    if request.method == 'POST':
        delform = UserSelectionForm(request.POST)
        if delform.is_valid():
            user_id = delform.cleaned_data['user'].id
            user = User.objects.get(id=user_id)
            user.delete()
            return redirect('new')
    else:
        delform = UserSelectionForm()

    return render(request, 'new.html', {'form': delform})









    
















# DeleteForm = modelform_factory(User, exclude=[])
# def delete(request):
#     delresponse = None
#     if request.method == "POST":
#         delform = DeleteForm(request.POST)
#         if delform.is_valid():
#             user_id_to_delete = delform.cleaned_data.get('id')
#             try:
#                 user_delete = User.objects.get(pk=user_id_to_delete)
#                 user_delete.delete()
#                 delresponse = "User removed successfully."
#             except User.DoesNotExist:
#                 delresponse = "User not found."
    
#     else:
#         delform = DeleteForm()
#     return render(request, "new.html", {'delform': delform, 'response': delresponse})






















# TestForm = modelform_factory(User, exclude=[])
# def test(request):
#     response = None
#     user_instance = get_object_or_404(User)
#     if form.is_valid():
            
#             user_instance.delete()
#             return redirect('success_page')  # Redirect to a success page or any other desired URL
#     else:
#         form = TestForm(instance=user_instance)

#     return render(request, 'test.html', {'form': form })

# TestForm = modelform_factory(User, exclude=[])
# def test(request):


