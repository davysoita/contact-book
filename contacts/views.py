from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Contact
from .forms import ContactForm


def home(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/home.html", {"contacts": contacts})

def contact_detail(request, pk):
   # contact = Contact.objects.get(pk=pk)
    contact = get_object_or_404(Contact, pk=pk)  
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def add_contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ContactForm()

    return render(request,"contacts/add_contact.html",  {"form": form} )

def edit_contact(request,pk):

    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect("contact_detail", pk=contact.id)

    else:
        form = ContactForm(instance=contact)

    return render( request,  "contacts/edit_contact.html", {"form": form, "contact": contact})

       
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        contact.delete()
        return redirect("home")

    return render( request, "contacts/delete_contact.html", {"contact": contact} )


def about(request):
    return render(request, 'contacts/about.html')