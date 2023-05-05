from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    # Declare initial value for name and email field
    form = StudentRegistration(auto_id=True, label_suffix=' ', 
            initial = {'name': 'Mushfiq', 'email': 'mushfiq@gmail.com'})
    return render(request, 'enroll/userregistration.html',
            {'form': form})
'''
def showformdata(request):
    # Add the label suffix character '-' using label suffix parameter
    # label_suffix='-'
    form = StudentRegistration(auto_id=True, label_suffix='-')
    return render(request, 'enroll/userregistration.html',
                   {'form': form})'''

'''
def showformdata(request):
    # Omit the label suffix character using label suffix parameter
    # label_suffix=' '
    form = StudentRegistration(auto_id=True, label_suffix=' ')
    return render(request, 'enroll/userregistration.html',
                   {'form': form})

def showformdata(request):
    # If auto_id is set to any other true value such as string, then the
    # library will act as if auto_id is True.
    form = StudentRegistration(auto_id='kmr')
    return render(request, 'enroll/userregistration.html',
                   {'form': form})

def showformdata(request):
    # auto_id=True  The form output will include <label> tags and will
    # use the field name as its id for each form field (required_id=fieldName)
    form = StudentRegistration(auto_id=True)
    return render(request, 'enroll/userregistration.html',
                   {'form': form})

def showformdata(request):
    # auto_id=False  The form output will not include <label> tags 
    # nor id attributes.
    form = StudentRegistration(auto_id=False)
    return render(request, 'enroll/userregistration.html',
                   {'form': form})

def showformdata(request):
    # provide default value
    form = StudentRegistration()
    return render(request, 'enroll/userregistration.html',
                   {'form': form})
'''
