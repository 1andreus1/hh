import requests
from time import sleep

def get_categories():
    res=requests.get('https://api.hh.ru/specializations')
    categories=[]
    for i in res.json():
        for j in i['specializations']:
            categories.append(j)
    return categories
def get_resumes(id_area):
    result=[]
    t=0
    while 1:
        try:
            sleep(t)
            pages=int(requests.get('https://api.hh.ru/resumes', headers=headers, params={'area': id_area,'driver_license_types':["A","B","C","D","E","BE","CE","DE","TM","TB"]}).json()['pages'])
            break
        except:
            print('Неудача')
            if t == 0:
                t += 1
            else:
                t *= 2
    if pages>20:
        pages=20
    for p in range(pages):
        t=0
        while 1:
            try:
                sleep(t)
                res = requests.get('https://api.hh.ru/resumes',headers=headers,params={'area': id_area,'per_page':100,'page':p,'driver_license_types':["A","B","C","D","E","BE","CE","DE","TM","TB"]})
                result=[*result,*(res.json()['items'])]
                break
            except:
                print('Неудача')
                if t == 0:
                    t += 1
                else:
                    t *= 2

    return result
def get_cities():
    result=[]
    res = requests.get('https://api.hh.ru/areas/113')
    for i in res.json()['areas']:
        result=[*result,*i['areas']]
    return result
resumes=set()
sum=0
area='4228'
try:
    with open('С правами.txt','r',encoding='utf-8') as f:
        txt=f.readlines()
        area=txt[0][:-1]
        links=map(lambda x:x.split()[1],txt[1:])
    for i in links:
        resumes.add(i)
        sum+=1
    flag=True
    print(sum,area,resumes)
except:
    print('файл не найден')
# headers = {
#     'User-Agent': 'Vakansii sanjsknc@yandex.ru',
#     'Authorization': 'Bearer NHSF98T6SVBBSSLN0RO5G1D69HADAO3DCJRT5REO1HDN9T9OK69O0ACB9EEDKRHO',
#         }
# access_token
headers = {
    'User-Agent': 'Vakansii sanjsknc@yandex.ru',
    'Authorization': 'Bearer R3SNQE1BB9FQOCRUM1UFS4DF2BKSA6EDQEFN717ALI992CB44J7P83N4JIMVE5UL',
        }

# for i in res.json()['items']:
#     print(i)
# res = get('https://hh.ru/oauth/authorize', headers=headers, params={
#                             'response_type':'code',
#                             'client_id':'OTJH66HE54I2TGLK4AQOMPAHII6V37SJG5C4M05VS99UG8OLTDQ7R6GAGOC8665D'})
#
# res = post('https://hh.ru/oauth/token',data={
# 'grant_type':'authorization_code',
# 'client_id':'OTJH66HE54I2TGLK4AQOMPAHII6V37SJG5C4M05VS99UG8OLTDQ7R6GAGOC8665D',
# 'client_secret':'O2ELTCU0S958I8JCCTM21O4S8S3VUKD30H40551OBJSI5D7D3BPCK002BEHBI7IQ',
# 'code':'SG5SP738CH4DKN0IGOMNDHIA8R4D5GSP312K68SC68ESMOOHHD9F3D45T0RKOV18'
# })
#
# print(res.text)
# print(res.json())
# access_token='R3SNQE1BB9FQOCRUM1UFS4DF2BKSA6EDQEFN717ALI992CB44J7P83N4JIMVE5UL'
# refresh_token='Q5HGGT1H672D1DGSIAU2ND7L8DQ37LS58PO1QK36QJT656R5P4QCRKOT02Q2B4CK'
# print(get_categories())
#
#
#
#
# r=get_resumes('11.71','1901')
# for i in r:
#     print(i)
# async def gather_data():
#     async with aiohttp.ClientSession(headers=headers,trust_env=True) as session:
#         tasks=[]
#         lt=0
#         for id_area in get_cities():
#             print(id_area)
#             t1=time()
#             if id_area['id'] == '2':
#                 continue
#             for s, e in ages:
#                 print(s,e)
#                 request=requests.get('https://api.hh.ru/resumes', headers=headers,params={'specialization': '11.71', 'area': id_area['id'],'age_from':s,'age_to':e}).json()
#                 print(request)
#                 pages = int(request['pages'])
#                 if pages==1:
#                     for i in request['items']:
#                         resumes.add(i['alternate_url'])
#                     pages=0
#                 if int(request['found']) == 0:
#                     print('пусто')
#                     pages = 0
#                 if pages > 20:
#                     pages = 20
#                 print(pages)
#                 for p in range(pages):
#                     tasks.append(asyncio.create_task(get_data(session,'11.71',id_area['id'],s,e,p)))
#                     lt+=1
#                     if lt==100:
#                         await asyncio.gather(*tasks)
#                         lt=0
#                         tasks=[]
#             t2=time()
#             print(t2-t1)
#         if tasks:
#             await asyncio.gather(*tasks)
# def main():
#     asyncio.get_event_loop().run_until_complete(gather_data())
#
# async def get_data(session,id_spec,id_area,s,e,p):
#     try:
#         t = 0
#         while 1:
#             await asyncio.sleep(t)
#             async with session.get('https://api.hh.ru/resumes', headers=headers,
#                                    params={'specialization': id_spec, 'area': id_area, 'per_page': 100, 'page': p,
#                                            'age_from': s, 'age_to': e},ssl=False) as res:
#                 text = await res.json()
#                 print(text)
#                 try:
#                     for i in text['items']:
#                         resumes.add(i['alternate_url'])
#                     break
#                 except:
#                     print('Новая попытка '+str(t))
#     except:
#         print('Неудача')
#
#         if t == 0:
#             t += 1
#         else:
#             t *= 2



for id_area in get_cities():
    print(id_area)
    if id_area['id']==area:
        flag=False
    else:
        if flag:
            continue
    if id_area['id']=='2':
        continue
    for element in get_resumes(id_area['id']):
        resumes.add(element['alternate_url'])
        sum+=1
    s = id_area['id'] + '\n'
    k = 0
    for i in resumes:
        s += str(k) + ' ' + i + '\n'
        k += 1
    with open('С правами.txt', 'w+', encoding='utf-8') as f:
        f.write(s)
    print(sum)

