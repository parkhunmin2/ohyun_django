from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

grade_db = [
  {
    "_id": "42afda16-cdce-4a8f-B763-ac98bd7cdf2a",
    "index": "1",
    "teather": "조성찬",
    "address": "잠실로 39-3",
    "phone": "010-2965-7135",
    "grade": "3",
    "num": "3",
    "contents": "정하여 후가 이하의 이름과 풀이 별들을 민주적이어야 구하기. 자를 창달에"
  },
  {
    "_id": "ac4caaea-1b93-4e65-A508-527a0c117d2c",
    "index": "2",
    "teather": "라채훈",
    "address": "망우로 20-6",
    "phone": "010-6071-6897",
    "grade": "2",
    "num": "8",
    "contents": "고동을 직무를 남은 수립에 대통령은 침해한 과할 관하여는. 군영과 가는"
  },
  {
    "_id": "c6d36b8a-3581-4c02-C46b-897c5c61e01b",
    "index": "3",
    "teather": "현민혁",
    "address": "용산로 40-1",
    "phone": "010-4519-7852",
    "grade": "2",
    "num": "3",
    "contents": "선출하는 쓸쓸함과 복지와 효력을 여부가 행하고 청춘이 언덕. 유지에 방황하여도"
  },
  {
    "_id": "4dc93a55-a59f-4971-B880-5d7fb5b79b29",
    "index": "4",
    "teather": "자가율",
    "address": "영등포로 24-8",
    "phone": "010-2228-6121",
    "grade": "2",
    "num": "9",
    "contents": "가지에 강요당하지 관리 연임할 정당의 외국에의 임대차와 때에는. 스며들어 생생하며"
  },
  {
    "_id": "1afc1cf8-d1f7-4123-B49c-8df244b245b4",
    "index": "5",
    "teather": "당이랑",
    "address": "동일로 11-9",
    "phone": "010-6420-9383",
    "grade": "2",
    "num": "10",
    "contents": "원대하고 물공급·포로·군용물에 있다 소금이라 신성한 뿐이다 최고득표자가 못할. 설산에서 미묘한"
  }
]

def index(request):
    return render(request,'main/index.html')

def jejuohyun(request):
     return render(request,'main/jejuohyun.html')

def high_1st(request):
    return render(request,'main/high_1st.html')

def high_2nd(request):
    return render(request,'main/high_2nd.html')

def high_3rd(request):
    return render(request,'main/high_3rd.html')

def my_page(request):
    return render(request,'main/my_page.html')

def grade(request):
    return render(request,'main/grade.html')