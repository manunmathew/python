forms refers to Django's from handling framework, which provides tool to easly create , validate


forms.py
in apps folder
{{form.as_p}}

    def post(self, request):
        form_instance=film_form(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data



initial you want to display default or pre-existing in a form , mostly while updating a model instance 
