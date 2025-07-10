Câu 1: Python là một ngôn ngữ thông dịch vì mã chương trình được chạy trực tiếp thông qua trình thông dịch. Nếu có lỗi ở dòng nào, chương trình sẽ dừng tại dòng đó, giúp lập trình viên dễ phát hiện lỗi

Câu 2:
* Các kiểu dữ liệu của Python:
  1. Kiểu số học:
      -int: số nguyên (4,-2)
      -float: số thực(3.14, 5,6)
      -complex: số phức (5 + i)
  2. Kiểu chuỗi:
      -str: Chuỗi ký tự("Hello","XinChao")
  3. Kiểu logic:
      -bool: Giá trị đúng / sai (true/ false)
  4. Kiểu tập hợp:
      -list: Danh sách có thể thay đổi(vd:[1,2,3])
      -tuple: Bộ giá trị không thay đổi(vd:(1,2,3))
      -set: Tập hợp không trùng lặp (vd:{1,2,3})
      -dict: Từ điển (dạng khóa-giá trị)(vd: {"name" : "giang","age" : 18} )
  5. Kiểu đặc biệt:
      -NoneType: Biểu thị giá trị rỗng(None)


* Các kiểu toán tử trong Python:
Trong python có  7 loại toán tử chính:

1. Toán tử số học:
    + (cộng): Thực hiện phép cộng 2 số
    - (Trừ): Thực hiện phép trừ 2 số
    * (Nhân): Thực hiện phép nhân 2 số
    / (Chia): Thực hiện phép chia lấy kết quả là số thực
    // (Chia lấy phần nguyên): Thực hiện phép chia lấy phần nguyên
    % (Chia lấy phần dư): Thực hiện phép chia lấy phần dư
    ** (Lũy thừa):  Thực hiện phép tính lũy thừa.

2. Toán tử so sách:
    == (Bằng): So sánh 2 giá trị xem có bằng nhau không
    != (Không bằng): So sánh 2 giá trị xem có khắc nhau hay không
    < (Nhỏ hơn): So sánh giá trị bên trái có nhỏ hơn giá trị bên phải không
    > (Lớn hơn): So sánh giá trị bên trái có lớn hơn giá trị bên phải không
    <= (Nhỏ hơn or bằng): So sánh giá trị bên trái có nhỏ hơn hoặc bằng giá trị phải không
    >= (Lơn hơn or bằng): So sánh giá trị bên trái có lớn hơn hoặc bằng giá trị phải không

3. Toán tử gán:

    = (Gán): Gán giá trị của 1 biểu thức cho 1 biến
    += (Cộng và gán): Cộng giá trị của một biểu thức với biến và gán kết quả cho biến
    -= (Trừ và gán): Trừ giá trị của một biểu thức từ biến và gán kết quả cho biến
    *= (Nhân và gán): Chia giá trị của một biến với một biểu thức và gán kết quả cho biến
    /= (Chia và gán): Chia giá trị của một biến cho một biểu thức và gán kết quả cho biến
    %= (Chia lấy phần dư và gán): Chia giá trị cảu 1 biến cho 1 biểu thức , lấy phần dư và gán kết quả cho biến
    //= (Chia lấy phần nguyên và gán): Chia giá trị của 1 biến cho 1 biểu thức,lấy phần nguyên và gán kết quả cho biến
    **= (Lũy thừa và gán): Tính lũy thừa của 1 biến và 1 biểu thức, sau đó gán kết quả cho biến

4. Toán tử logic:
  . AND: Trả về True nếu cả hai toán hạng đều True.
  . OR:  Trả về True nếu ít nhất một toán hạng là True.
  . NOT:  Trả về True nếu toán hạng là False, và ngược lại.

5. Toán tử bitwise
 . & (AND bit): Thực hiện phép AND bitwise giữa 2 số
 . | (OR bit): Thực hiện phép OR bitwise giữa 2 số
 . ^ (XOR bit): Thực hiện phép XOR bitwise giữa 2 số
 . ~ (NOT bit): Thực hiện phép NOT bitwise(đảo bit)
 . << (Dịch bit sang trái): Dịch bit của 1 số sang trái
 . >> (Dịch bit sang phải): Dịch bit của 1 số sang phải

6. Toán tử thành viên
  . in: Trả về True nếu một giá trị có mặt trong một chuỗi, danh sách, tuple, hoặc set.
  . not in: Trả về False nếu một giá trị có mặt trong một chuỗi, danh sách, tuple, hoặc set.

7. Toán tử nhận dạng
  . is: Trả về True nếu hai biến tham chiếu đến cùng một đối tượng.
  . is not: Trả về True nếu hai biến không tham chiếu đến cùng một đối tượng.

* Mệnh đề điều kiện và vòng lặp
    1. Mệnh đề điều kiệu:
        . if: Thực hiện một khối lệnh nếu điều kiện là True
        . elif: (else if) Kiểm tra thêm điều kiện nếu điều kiện if trước đó là False.
        . else: Thực hiện một khối lệnh nếu không có điều kiện if hoặc elif nào đúng.
    VD: 
    x = 10
    if x > 5:
      print("x lớn hơn 5")
    elif x == 5:
      print("x bằng 5")
    else:
      print("x nhỏ hơn 5")
    
    2. Vòng lặp:
      . for: Lặp qua một dãy các phần tử (ví dụ: danh sách, chuỗi, tuple).
      VD: 
      for i in range(5):
          print(i)

      .while: Lặp lại một khối lệnh khi điều kiện còn đúng. 
      VD:
      i = 0
      while i < 5:
        print(i)
        i += 1
      
    3. Các lệnh điều khiển vòng lặp:
      . break: Thoát khỏi vòng lặp
      . continue: Bỏ qua vòng lặp hiện tại
      . pass: Không làm gì cả


* Kiểu dữ liệu True, False
    Có đúng hai giá trị duy nhất:
      . True (đúng)
      . False (sai)

    Dùng chủ yếu trong:
      . So sánh (a > b)
      . Điều kiện (if, while)
      . Biểu thức logic (and, or, not)

