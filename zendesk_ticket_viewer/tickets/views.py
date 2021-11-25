from typing import Any
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from tickets import helper

# Create your views here.
def get_tickets(request):
    response = helper.get_tickets()
    if response.status_code==200:
        all_tickets = response.json()['tickets']
        if len(all_tickets)==0:
            return render(request,'main/error.html',{'error_msg':'You have no tickets!'})
        page = request.GET.get('page', 1)
        paginator = Paginator(all_tickets,25)
        try:
            tic = paginator.page(page)
        except PageNotAnInteger:
            tic = paginator.page(1)
        except EmptyPage:
            tic = paginator.page(paginator.num_pages)
        return render(request,'main/tickets.html',{'response':tic})   
    else:
        return render(request,'main/error.html',{'error_msg':'Uh uh! There seems to be an issue in getting your tickets. Please check back later. Sorry for the inconvenience!'})



def get_ticket_details(request,ticket_id):
    response = helper.get_tickets()
    if response.status_code==200:
        all_tickets = response.json()['tickets']
        ticket_detail:Any
        for i in range(0,len(all_tickets)):
            if all_tickets[i].get('id')==ticket_id:
                ticket_detail = all_tickets[i]
        return render(request,'main/ticket_detail.html',{'ticket_detail':ticket_detail})
    
    else:
        return render(request,'main/error.html',{'error_msg':'Uh uh! There seems to be an issue in getting your tickets. Please check back later. Sorry for the inconvenience!'})
    
    
    

