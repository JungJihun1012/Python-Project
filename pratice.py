friends=["이상원", "이정우", "홍의준", "윤상지"]
select=0
while select!=9:
  print("1. 친구 리스트 출력", "2. 친구 추가", "3.친구 삭제", "4. 이름 변경", "9. 종료")
  select=int(input("메뉴를 선택하시오:"))
  if select==1:
    print("친구 리스트는:", friends)
    continue
  elif select==2:
    addfriend=input("추가할 친구 이름을 입력하세요:")
    friends.append(addfriend)
    print("친구 추가가 완료되었습니다")
    continue
  elif select==3:
    remfriend=input("삭제할 친구 이름을 입력하세요:")
    friends.remove(remfriend)
    print("친구 삭제가 완료되었습니다")
    continue
  elif select==4:
    chfriend=input("이름을 변경할 친구 이름을 입력하세요:")
    chdfriend=input("변경 후 이름을 입력하세요:")
    a=friends.index(chfriend)
    friends.insert(a,chdfriend)
    friends.remove(chfriend)
    continue
  else:
    print("종료되었습니다.")
    break