from django.shortcuts import render
import requests
from .models import Contact
from django.contrib import messages
url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "d9cbda2f6dmshc2bba4bd0e71c1ap1ab42fjsnc01c43dd2e87"
}
response = requests.request("GET", url , headers=headers).json()
#print(response)


def index(request):
    mapArray = []
    mylist = []
    clist=[]
    noofresults = int(response['results'])
    for y in range(0, noofresults):
        cdict = {}
        cdict['country'] = response['response'][y]['country']
        cdict['active'] = response['response'][y]['cases']['active']
        cdict['new'] = response['response'][y]['cases']['new']
        cdict['total'] = response['response'][y]['cases']['total']
        clist.append(cdict)
    #print(clist)

    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])

    if request.method=="POST":

        selectedcountry = request.POST['selectedcountry']



        for x in range(0,noofresults):

            if selectedcountry == response['response'][x]['country']:


                new = response['response'][x]['cases']['new']

                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)


        context = {'data': clist,'selectedcountry': selectedcountry,'mylist': mylist ,'new': new, 'active':active, 'critical': critical, 'recovered': recovered, 'deaths': deaths, 'total': total}

        return render(request, 'index.html', context)


    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):

        mylist.append(response['response'][x]['country'])
    context = {'mylist': mylist}
    return render(request,'index.html', context)


def india(request):
    return render(request, 'india.html')
def frontpage(request):
    return render(request,'frontpage.html')
def protection(request):
    return render(request,'protect.html')
def symptoms(request):
    return render(request,'symptoms.html')
def prevent(request):
    return render(request,'prevent.html')
def  handwash(request):
    return render(request,'handwash.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "contact.html")


