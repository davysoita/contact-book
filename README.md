# My Contacts (Django Contact Book)

Simple Django contact book project for managing contacts (add, edit, view, delete).

## Prerequisites

- Python 3.10+ (project uses Python 3.14 in environment snapshot)
- Git (optional)
- Windows PowerShell (examples below)

## Setup (Windows PowerShell)

1. Clone or open the project folder and create a virtual environment (if not present):

```powershell
python -m venv venv
```

2. Activate the virtual environment:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

3. Install dependencies (this project uses Django). If you have a `requirements.txt`, run:

```powershell
pip install -r requirements.txt
```

If you do not have `requirements.txt`, install Django directly:

```powershell
pip install django
```

## Database setup

Run migrations:

```powershell
python manage.py migrate
```

(Optional) Create a superuser for the admin site:

```powershell
python manage.py createsuperuser
```

## Run the development server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## How the app works

- Add a contact: click "Add New Contact" on the home page.
- View details: click "View" in the Actions column.
- Edit a contact: click "Edit" or the Edit link on the detail page.
- Delete a contact: click "Delete" to open a confirmation page, then confirm.

Notes: Templates with actions are located in the `contacts/templates/contacts/` folder. Important files:

- [contacts/views.py](contacts/views.py#L1)
- [contacts/forms.py](contacts/forms.py#L1)
- [contacts/models.py](contacts/models.py#L1)
- [contacts/urls.py](contacts/urls.py#L1)
- [contacts/templates/contacts/home.html](contacts/templates/contacts/home.html#L1)
- [contacts/templates/contacts/contact_detail.html](contacts/templates/contacts/contact_detail.html#L1)
- [contacts/templates/contacts/add_contact.html](contacts/templates/contacts/add_contact.html#L1)
- [contacts/templates/contacts/edit_contact.html](contacts/templates/contacts/edit_contact.html#L1)
- [contacts/templates/contacts/delete_contact.html](contacts/templates/contacts/delete_contact.html#L1)

## Troubleshooting

- If you see a FieldError about unknown fields, confirm the names in `Contact` model and `ContactForm.Meta.fields` match.
- Ensure the virtual environment is activated before running management commands.

## Next steps

- Add a `requirements.txt` using `pip freeze > requirements.txt`.
- Run `python manage.py check` and `python manage.py runserver` to verify functionality.

---

README created by the project maintainer assistant.
