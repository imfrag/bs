from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponseRedirect
from main.models import HouseHolder, Billboard, Staff, Repair, House, Bill
from main.models import RelHouseHolder, RelHouseholderRepair
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
import json, sys
from datetime import datetime


def verify_login(request):
    if request.session.get('user', ''):
        return True
    return False


def user_index(request, username):
    if not verify_login(request):
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'user/profile.html', {'username': username})


def update_profile(request, username):
    if not verify_login(request):
        return HttpResponseRedirect(reverse('index'))

    if request.is_ajax():
        print('hello')
        tel = request.GET['tel']
        user = HouseHolder.objects.filter(tel=tel)
        if user:
            return JsonResponse({"STATUS": ""})
        else:
            return JsonResponse({"STATUS": "1"})
    elif request.method == "POST":
        user = HouseHolder.objects.get(username=username)
        try:
            user.realname = request.POST['realname']
            user.tel = request.POST['tel']
            user.save()
        except Exception as e:
            print(e)

        user_queryset = HouseHolder.objects.filter(username=username)
        data = serializers.serialize('json', user_queryset)
        data_json = json.loads(data[1:-1])
        request.session['user'] = data_json['fields']
        return HttpResponseRedirect(reverse('profile', args=(username,)))


def user_privacy(request, username):
    if not verify_login(request):
        return HttpResponseRedirect(reverse('index'))

    if request.is_ajax():
        user = HouseHolder.objects.get(username=username)
        if (request.GET['opwd'] != user.password):
            return JsonResponse({'STATUS': "password"})

        if request.GET.get('email', ''):
            try:
                HouseHolder.objects.get(email=request.GET['email'])
            except ObjectDoesNotExist:
                return JsonResponse({'STATUS': "sucess"})

            return JsonResponse({'STATUS': "email"})
        elif request.GET.get('phone', ''):
            try:
                HouseHolder.objects.get(tel=request.GET['phone'])
            except ObjectDoesNotExist:
                return JsonResponse({'STATUS': "sucess"})

            return JsonResponse({'STATUS': "phone"})

        return JsonResponse({'STATUS': "sucess"})

    if request.method == "GET":
        return render(request, "user/privacy.html")
    elif request.method == "POST":
        hidetype = request.POST['hidetype']
        user = HouseHolder.objects.get(username=username)
        if hidetype == 'cpwd':
            user.password = request.POST['newpassword']
            user.save()
            return HttpResponseRedirect(reverse('logout'))
        elif hidetype == "cemail":
            user.email = request.POST['email']
            user.save()

            user_queryset = HouseHolder.objects.filter(username=username)
            data = serializers.serialize('json', user_queryset)
            data_json = json.loads(data[1:-1])
            request.session['user'] = data_json['fields']
            return HttpResponseRedirect(reverse('profile', args=(username,)))
        elif hidetype == "cphone":
            user.tel = request.POST['phone']
            user.save()

            user_queryset = HouseHolder.objects.filter(username=username)
            data = serializers.serialize('json', user_queryset)
            data_json = json.loads(data[1:-1])
            request.session['user'] = data_json['fields']
            return HttpResponseRedirect(reverse('profile', args=(username,)))


def get_contact(request, username):
    if not verify_login(request):
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'user/contact.html')


def get_billboard(request, username):
    if not verify_login(request):
        return HttpResponseRedirect(reverse('index'))

    billboards = []
    flag = False
    if request.GET.get('s', ''):
        if request.GET.get('title', ''):
            billboards = Billboard.objects.filter(
                title__contains=request.GET['title'])
        elif request.GET.get('content', ''):
            billboards = Billboard.objects.filter(
                content__contains=request.GET['content'])
        elif request.GET.get('publisher', ''):
            billboards = Billboard.objects.filter(
                staff_id=Staff.objects.get(username=request.GET[
                    'publisher']).staff_id)
        elif request.GET.get('time', ''):
            d = datetime(*list(map(int, request.GET['time'].split('-'))))
            billboards = Billboard.objects.filter(publish_time__lte=d)

        flag = True

    if not billboards and not flag:
        billboards = Billboard.objects.all()

    staff_ids = [bb.staff_id for bb in billboards]
    staff_names = []
    id_name = {}
    for i in staff_ids:
        if i in id_name.keys():
            staff_names.append(id_name[i])
            continue
        name = Staff.objects.get(staff_id=i).username
        id_name[i] = name
        staff_names.append(name)
    return render(request,
                  'user/billboard.html',
                  {'bbs': zip(billboards, staff_names)})


def get_repair(request, username):
    if not verify_login(request):
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        print('hello')
        description = request.POST['description']
        house_id = request.POST['house_id']
        new_repair = Repair(house_id=house_id,
                            repair_description=description)
        new_repair.save()
        new_repair_rel = RelHouseholderRepair(householder_id=request.session[
            'userid'], repair_id=new_repair.repair_id)
        new_repair_rel.save()

        return HttpResponseRedirect(reverse('repair', args=(username,)))
    elif request.method == "GET":
        i = request.session['userid']
        repairs = RelHouseholderRepair.objects.filter(
            householder_id=i).order_by('-rel_id')
        repairs_id = [i.repair_id for i in repairs]
        repairs = [Repair.objects.get(repair_id=i) for i in repairs_id]
        repairs = sorted(repairs,
                         key=lambda repair: repair.repair_time.timestamp() if
                         repair.repair_time else sys.maxsize,
                         reverse=True)
        houses_rel = RelHouseHolder.objects.filter(householder_id=i)
        houses_id = [hr.house_id for hr in houses_rel]
        houses = [House.objects.get(house_id=i) for i in houses_id]
        house_staff_ids = [(r.staff_id, r.house_id) for r in repairs]
        locations = []
        staff_names = []
        id_name = {}
        for si, hi in house_staff_ids:
            locations.append(House.objects.get(house_id=hi).location)
            if not si:
                staff_names.append("")
                continue
            if si in id_name.keys():
                staff_names.append(id_name[si])
                continue
            name = Staff.objects.get(staff_id=si).username
            id_name[si] = name
            staff_names.append(name)
        return render(request,
                      'user/repair.html',
                      {'rs': zip(repairs, staff_names, locations),
                       'houses': houses})


def get_bill(request, username):
    pass