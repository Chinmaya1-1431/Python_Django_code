from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    cont={
        "name":"chinmaya",
        "Age": 26,
        "Address":
    {
            "Street":"Kovil",
            "City":"Thiruvallur"
    }
    }
    return render(request,"home.html",cont)
    # if age >= 18:
    #     return HttpResponse("You are eligible")
    # else:
    #     return HttpResponse("You are Not eligible")
# return HttpResponse("Welcome to My App")



