try:
  print("-"*5, "Chào Mừng Đến Với Cửa Hàng Bán Đồ Giải Trí Online", "-"*5)
  vohang=[]
  tongcong=0
  while (True):
    print("Vui lòng nhập lựa chọn của bạn:\n1:Mua đồ chơi.\n2:Mua bản quyền trò chơi điện tử.\n3:Kết thúc và đến phần thanh toán\n4:Xóa giỏ hàng.")
    luachon=int(input("Nhập lựa chọn của bạn: "))
    if luachon==1:
      print("Vui lòng nhập lựa chọn của bạn:\n1:Ráp hình tàu vũ trụ.\n2:Robot biến hình.\n3:Ô tô điều khiển từ xa.")
      luachon=int(input("Nhập lựa chọn của bạn: "))
      if luachon==1:
        giatien = (1000000)
        print("Giá tiền bạn phải trả là", giatien, "vnd")
        tiendangco=int(input("Số tiền bạn đang có là bao nhiêu vnđ: "))
        if tiendangco>=giatien:
          ok=int(input("Bạn đã có đủ tiền, ấn phím 1 để thêm vào vỏ hàng."))
          if ok==1:
            vohang.append("Ráp hình tàu vũ trụ")
            tongcong+=1000000
          else:
            print("Bạn đã nhập sai. Vui lòng nhập lại!")
        elif tiendangco<giatien:
          tiencan=(giatien-tiendangco)
          print("bạn còn cần thêm", tiencan," vnđ", "để mua được món đồ này.")
          ngay = int(input("trung bình một ngày bạn kiếm được bao nhiêu vnđ: "))
          tb=(tiencan/ngay)
          print("bạn còn cần thêm", round(tb), "ngày để đủ tiền mua được món đồ này.")        
      elif luachon==2:
        giatien = (400000)
        print("giá tiền bạn phải trả là", giatien, "vnd")
        tiendangco=int(input("số tiền bạn đang có là bao nhiêu vnđ: "))
        if tiendangco>=giatien:
          ok=int(input("bạn đã có đủ tiền, ấn phím 1 để thêm vào vỏ hàng."))
          if ok==1:
            vohang.append("robot biến hình")
            tongcong+=400000
          else:
            print("Bạn đã nhập sai. Vui lòng nhập lại!")
        elif tiendangco<giatien:
          tiencan=(giatien-tiendangco)
          print("bạn còn cần thêm", tiencan," vnđ", "để mua được món đồ này.")
          ngay = int(input("trung bình một ngày bạn kiếm được bao nhiêu vnđ: "))
          tb=(tiencan/ngay)
          print("bạn còn cần thêm", round(tb), "ngày để đủ tiền mua được món đồ này.")
      elif luachon==3:
        giatien = (600000)
        print("giá tiền bạn phải trả là", giatien, "vnd")
        tiendangco=int(input("số tiền bạn đang có là bao nhiêu vnđ: "))
        if tiendangco>=giatien:
          ok=int(input("bạn đã có đủ tiền, ấn phím 1 để thêm vào vỏ hàng."))
          if ok==1:
            vohang.append("ô tô điều khiển từ xa.")
            tongcong+=600000
          else:
             print("Bạn đã nhập sai. Vui lòng nhập lại!")
        elif tiendangco<giatien:
          tiencan=(giatien-tiendangco)
          print("bạn còn cần thêm", tiencan," vnđ", "để mua được món đồ này.")
          ngay = int(input("trung bình một ngày bạn kiếm được bao nhiêu vnđ: "))
          tb=(tiencan/ngay)
          print("bạn còn cần thêm", round(tb), "ngày để đủ tiền mua được món đồ này.")      
    elif luachon==2:
      print("1:minecraft\n2:Among Us")
      luachon=int(input("nhập lựa chọn của bạn: "))
      if luachon==1:
        print("1:phiên bản dành cho máy tính\n2:phiên bản dành cho điện thoại.")
        luachon==int(input("nhập lựa chọn của bạn: "))
        if luachon==1:
          giatien = (450000)
          print("giá tiền bạn phải trả là", giatien, "vnd")
          tiendangco=int(input("số tiền bạn đang có là bao nhiêu vnđ: "))
          if tiendangco>=giatien:
            ok=int(input("bạn đã có đủ tiền, ấn phím 1 để thêm vào vỏ hàng."))
            if ok==1:
              vohang.append("minecraft máy tính")
              tongcong+=450000
            else:
              print("Bạn đã nhập sai. Vui lòng nhập lại!")
          elif tiendangco<giatien:
            tiencan=(giatien-tiendangco)
            print("bạn còn cần thêm", tiencan," vnđ", "để mua được món đồ này.")
            ngay = int(input("trung bình một ngày bạn kiếm được bao nhiêu vnđ: "))
            tb=(tiencan/ngay)
            print("bạn còn cần thêm", round(tb), "ngày để đủ tiền mua được món đồ này.")
        elif luachon==2:
          giatien = (179000)
          print("giá tiền bạn phải trả là", giatien, "vnd")
          tiendangco=int(input("số tiền bạn đang có là bao nhiêu vnđ: "))
          if tiendangco>=giatien:
            ok=int(input("bạn đã có đủ tiền, ấn phím 1 để thêm vào vỏ hàng."))
            if ok==1:
              vohang.append("minecraft điện thoại")
              tongcong+=179000 
            else:
              print("Bạn đã nhập sai. Vui lòng ấn phím lại!")   
          elif tiendangco<giatien:
            tiencan=(giatien-tiendangco)
            print("bạn còn cần thêm", tiencan," vnđ", "để mua được món đồ này.")
            ngay = int(input("trung bình một ngày bạn kiếm được bao nhiêu vnđ: "))
            tb=(tiencan/ngay)
            print("bạn còn cần thêm", round(tb), "ngày để đủ tiền mua được món đồ này.")
      elif luachon==2:
        giatien = (111000)
        print("giá tiền bạn phải trả là", giatien, "vnd")
        tiendangco=int(input("số tiền bạn đang có là bao nhiêu vnđ: "))
        if tiendangco>=giatien:
          ok=int(input("bạn đã có đủ tiền, ấn phím 1 để thêm vào vỏ hàng."))
          if ok==1:
            vohang.append("amongus")
            tongcong+=111000
          else:
            print("Bạn đã nhập sai. Vui lòng ấn phím lại!")
        elif tiendangco<giatien:
          tiencan=(giatien-tiendangco)
          print("bạn còn cần thêm", tiencan,"vnđ", "để mua được món đồ này.")
          ngay = int(input("trung bình một ngày bạn kiếm được bao nhiêu vnđ: "))
          tb=(tiencan/ngay)
          print("bạn còn cần thêm", round(tb), "ngày để đủ tiền mua được món đồ này.")
    elif luachon==3:
      print(vohang)
      print("bạn phải trả", tongcong, "vnd")
      print("Chúc bạn chơi vui vẻ!")
      break
    elif luachon==4:
      vohang.clear()
      tongcong=0
      print("đã xóa giỏ hàng thành công!")
except:
  print("Đã có lỗi xảy ra!")
