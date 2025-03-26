from django.shortcuts import render
def region(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        print(request.POST)
        print(form)
        print(form.cleaned_date)
        if form.is_valid():
            form.save()
            return redirect('region')
    else:
        form = RegionForm()
    crx = {
        'form': form
    }

    return render(request, 'region.html')
        # Create your views here.
