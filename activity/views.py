from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from activity.models import Activity
@csrf_exempt
def  hello(request):
	count=1
	k=1
	if request.GET:
		a=Activity.objects.all()
		for i in a:
			count=count+1
        	json_data=request.GET['Body']
        	lst=json.loads(json_data)
		for obj in lst:
        		for  j in range(1,count):
				b=Activity.objects.get(id=j)
                		#print obj['id']
				if(b.ids==obj['id']):
					k=1
					if(obj['state']=="True"):
						if(b.state!=True):
							b.update=True
						else:
							b.update=False
						b.state=True
						b.save()
					else:
						if(b.state!=False):
							b.update=True
						else:
							b.update=False
						b.state=False
						b.save()
					break
				else:
					k=2
			if(k==2):
				if(obj['state']=="True"):
					a=Activity(ids=obj['id'],name=obj['name'],state=True,quantity=obj['quantity'])
				else:
					a=Activity(ids=obj['id'],name=obj['name'],state=False,quantity=obj['quantity'])
				a.save()
			

        	return HttpResponse(json_data)
	else:
		a=Activity.objects.filter(update=False)
		#for i in a:
			#count=count+1
			#print(i.name)
		#print (count)
		lst=[]
		#lst=[{'state':Activity.objects.get(id=1).state,'id':Activity.objects.get(id=1).ids,'quantity':3,'name':'Baby Oil'},{'state':'True','id':115,'quantity':4,'name':'Baby Shampoo'}]
		for y in a:
			lst.append({'state':y.state,'id':y.ids,'quantity':y.quantity,'name':y.name})	
		#for obj in lst:
			#for j in range(1,count):
				#print obj["id"]
				#b=Activity.objects.get(id=j)
				#if(b.ids==obj['id']):
					#k=1
					#if(obj['state']=="True"):
						#b.state=True
						#b.save()
					#else:
						#b.state=False
						#b.save()
					#break
		
		
		#html="<html><body></body></html>"
		return HttpResponse(json.dumps(lst),content_type="application/json")

