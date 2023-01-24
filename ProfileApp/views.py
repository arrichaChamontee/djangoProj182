from django.shortcuts import render

# Create your views here.
def Profile(request):
    return render(request,'Profile.html')

def Education(request):
    return render(request,'Education.html')

def Attention(request):
    return render(request,'Attention.html')

def Career(request):
    return render(request, 'Career.html')

def RoleModel(request):
    return render(request,'RoleModel.html')

def ShowMyData(request):
   name = 'Arricha Chamontee'
   nickname ='nut'
   age = '22'
   BloodGroup = 'B'
   occupation = 'student'
   country ='Thailand'
   Rolemadel = 'Kendoll jenner'
   hobby ='listen to music'
   talent = 'artwork'
   FavoriteFlowers = 'hydrangeas'
   products = [
        ['162700','ROUGE ALLURE VELVET','1,500','/static/images/product01.webp'],
        ['131882', 'SUBLIMAGE LE CORRECTEUR YEUX', '4,150', '/static/images/product02.webp'],
        ['147130', 'SUBLIMAGE L ESSENCE DE TEINT', '5,950', '/static/images/product03.webp'],
        ['145764', 'N°1 DE CHANEL REVITALIZING FOUNDATION', '3,000', '/static/images/product04.webp'],
        ['145385', 'N°1 DE CHANEL LIP AND CHEEK BALM', '1,800', '/static/images/product05.webp'],
        ['190010', 'NOIR ALLURE', '1,700', '/static/images/product06.webp'],
        ['164140', 'LES 4 OMBRES', '2,550', '/static/images/product07.webp'],
        ['174200', 'ROUGE COCO FLASH TOP COAT', '1,500',  '/static/images/product08.webp'],
        ['165060', 'ROUGE ALLURE LAQUE', '1,500', '/static/images/product09.webp'],
        ['159723', 'LE VERNIS', '1,500', '/static/images/product10.webp'],
   ]
   context ={'name':name,'nickname':nickname,'age':age,'BloodGroup':BloodGroup,'occupation':occupation,
             'country':country,'Rolemadel':Rolemadel,'hobby':hobby,'talent': talent,
             'FavoriteFlowers': FavoriteFlowers,'products': products,}
   return render(request,'ShowMyData.html',context)
