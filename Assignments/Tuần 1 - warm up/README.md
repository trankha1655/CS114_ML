# Week 1

## Progress
|ID   | Problem | Status 
|:---:|:---:|:---:|
|1 | [Tổng số ước](#problem-1) | 	:white_check_mark: 
|2 |[Fibo](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/fibo.py)| :white_check_mark: 
|3 | [Tam Giác](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Tam_Giac) | :white_check_mark:
|4 | [Áp suất](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Ap_Suat.py)| :white_check_mark:
|5 | [Đường sắt](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Duong_Sat.py)| :white_check_mark:
|6 | [KFC](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/KFC.py)| :white_check_mark:
|7 | [Gà Chó](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Ga_Cho.py) | :white_check_mark:
|8 | [Task](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Task.py) | :white_check_mark:
## Problem 1: 
### [Tổng số ước](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Tong_Uoc_So.py)
**Time limit per test: 1 second**

**Memory limit per test: 50 megabytes**

<br/>Viết chương trình tính tổng các ước số thực sự của một số nguyên dương.
**INPUT**:  Số nguyên dương **n** giá trị không quá **10^9**.

**OUTPUT**:Tổng các ước số của **n** (không kể **n**)

| Input | Output |
|:---:|:---:|
| 4 | 3 |
| 5 | 1 |
| 6 | 6 |
| 8 | 7 |
| 27 | 13 |

## Problem 2: [Fibo](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/fibo.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**
Nhập vào số nguyên **x** sao cho **1 ≤ x ≤ 30**. Nếu **x** không thỏa điều kiện, chương trình xuất ra màn hình thông báo **“So <x> khong nam trong khoang [1,30].”**. Nếu **x** nằm trong đoạn **[1,30]**, chương trình xuất ra màn hình số Fibonacci thứ **x**.



| Input | Output |
|:---:|:---:|
| -6 | 	So -6 khong nam trong khoang [1,30].|
| 6 | 8 |

## Problem 3: [Tam Giac](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Tam_giac.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**
Viết chương trình nhập vào 3 số thực. Hãy cho biết đó có phải là độ dài 3 cạnh 1 tam giác hay không? Nếu phải thì đó là loại nào trong 4 loại sau: tam giác thường, cân, đều, vuông.

Nếu là tam giác tính diện tích tam giác.

**INPUT**:  
Dòng đầu tiên là độ dài cạnh 1.

Dòng thứ hai là độ dài cạnh 2.

Dòng thứ ba là độ dài cạnh 3.

**OUTPUT**: 
Định dạng như ví dụ minh họa. Diện tích làm tròn 02 chữ số sau dấu thập phân.

| Input | Output |
|:---: |:---:|
| 2 <br/> 3 <br/> 4| Tam giac thuong, dien tich = 2.9 |
| 3 <br/> 4 <br/> 5 | Tam giac vuong, dien tich = 6 |
| 1 <br/> 2 <br/> 3| Khong phai tam giac |

## Problem 4: [Áp suất](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Ap_suat.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Tìm ra áp suất chất lỏng/khí và cách đo đạt chúng là một vấn đề nghiên cứu vật lý thực nghiệm từng làm đau đầu nhiều nhà khoa học thời trung cổ. Đã có nhiều nhà khoa học khác nhau đề xuất các thang đo khác nhau. Tuy nhiên ngày nay một đơn vị đo áp suất phổ thông mà dễ hiểu là tính lực tác động (theo khối lượng) chia cho diện tích. Khổ nổi trong hệ đo lường quốc tế (SI) và hệ đo Imperial phổ biến ở Mỹ người ta đo khối lượng và áp suất bằng cách đơn vị khác nhau. Bạn Bình vừa mua một con mô-tô phân khối lớn hàng nhập nguyên chiếc từ Mỹ về, tài liệu hướng dẫn của xe ghi áp suất phù hợp khi bơm xe bằng đơn vị PSI (Pound / square inches - 1 pound lực trên một inch vuông). Còn ống bơm của Bình tích hợp đồng hồ đo áp suất bằng đơn vị kg/cm2 (1 kilogram lực trên một centimét vuông).

Biết: 1 pound = 0.453592 kg

và 1 inch = 2,54 cm

Viết công thức giúp Bình đổi PSI sang kg/cm2

**INPUT**:  
Một con số duy nhất theo đơn vị PSI

**OUTPUT**: 
Một con số ương ứng theo đơn vị kg/cm2


| Input | Output |
|:---:|:---:|
| 15 | 	1.0546|
| 2018 | 	141.879|

## Problem 5: [Đường sắt](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Duong_sat.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Thành phố đang xây dựng tuyến đường sắt trên cao phục vụ giao thông nội đô. Tuyến đường sẽ có **k**+1 ga đánh số từ 0 đến **k**. Tàu chạy suốt ngày đêm, từ ga 0 đến ga **k** và quay lại. Thời gian đi từ một ga tới ga kế tiếp là 1 phút, thời gian dừng ở mỗi ga là không đáng kể. Hệ thống giao thông này không những nhanh, chuẩn xác về thời gian mà còn là một phương tiện tuyệt vời để ngắm thành phố.

BHL của UIT quyết định sẽ tặng cho tất cả tham gia lớp Python online mỗi bạn một vé đi tàu miễn phí trong năm học.

Minh rất háo hức với thông báo này và quyết tâm phải giành được một vé. Phần lớn thời gian rảnh rỗi trong ngày Minh đều dùng để rèn luyện lập trình Python, còn ban đêm là thời gian của những giấc mơ đẹp. Minh thấy mình bước lên tàu ở ga số 0, ngồi cạnh cửa sổ say sưa ngắm nhìn quang cảnh thành phố từ trên cao. Thời gian trôi đi khá nhanh. Đồng hồ cho biết Minh đã ngồi trên tàu t phút và Minh quyết định xuống tàu . . .

Chuông đồng hồ vang lên, Minh tỉnh giấc, vội vàng đi đánh răng, rửa mặt, chuẩn bị đi học. Trên đường tới trường Minh vẫn nghĩ về giấc mơ đêm qua và không thể nhớ được mình đã xuống ở ga số mấy.

Hãy xác định ga mà Minh đã xuống trong giấc mơ sắp thành hiện thực của mình.

**INPUT**:  
Vào từ thiết bị nhập chuẩn gồm một dòng chứa 2 số nguyên **k** và **t** (0 < **k**, **t** ≤ 109)

**OUTPUT**: 
Đưa ra thiết bị xuất chuẩn một số nguyên – ga xác định được.


| Input | Output |
|:---:|:---:|
| 5  8 | 	2|

## Problem 6: [KFC](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/KFC.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Bình vừa mua xách tay một cái nhiệt kế hồng ngoại cực xịn cực chính xác chỉ mỗi tội nó hiển thị nhiệt độ theo thang đo độ **F - Farenheit**. Hãy giúp Bình đổi qua độ **C - Celsius** và độ **K - Kelvin**

**INPUT**:  
Một con số - nhiệt độ theo thang **F**

**OUTPUT**: 
Hai con số - nhiệt độ theo thang **C** và thang **K**


| Input | Output |
|658.4  |	 348 621.15|
| 472.6 | 244.778 517.928|



## Problem 7: [Gà Chó](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201%20-%20warm%20up/Ga_Cho.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Vừa gà vừa chó

Bó lại cho tròn

**xxx** con

**yy** chân chẵn

Hãy xác định số con gà và số con chó thỏa mãn yêu cầu.

**INPUT**:  
Vào từ thiết bị nhập chuẩn gồm 1 dòng ghi 2 số nguyên **xxx** và **yy** (2≤ **xxx**, **yy** ≤ 109)

**OUTPUT**: 
Đưa ra thiết bị xuất chuẩn một dòng 2 số nguyên số gà và số chó tìm được.

Dữ liệu luôn bảo đảm có kết quả.


| Input | Output |
|36 100|	 24 14|







