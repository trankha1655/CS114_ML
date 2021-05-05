# Tuần 1.2 - Tăng tốc từ từ

## Progress
|ID   | Problem | Status 
|:---:|:---:|:---:|
|1 | [	Tìm số gần nhất](#problem-1) | 	:white_check_mark: 
|2 |[Thêm và xóa](#problem-2)| :white_check_mark: 
|3 | [		Merge sorted array](#problem-3) | :white_check_mark:
|4 | [	ROI (region of interest)](#problem-4)| :white_check_mark:
|5 | [		Reshape matrix](#problem-5)| :white_check_mark:
|6 | [	Online game](#problem-6)| :white_check_mark:
|7 | [	Online game 2](#problem-7) | :white_check_mark:



## Problem 1:
### 
# [	Tìm số gần nhất](Tim_So_Gan_Nhat.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**


Cho mảng số nguyên **A** đã sắp xếp tăng dần, tìm trong mảng **k** số có giá trị gần với giá trị **x** nhất.

**INPUT**

Dòng đầu tiên cho biết số phần tử của mảng

Dòng thứ 2 là toàn bộ mảng liệt kê trên một hàng, các phần tử cách nhau bởi khoảng trắng

Dòng cuối cùng lần lượt là 02 số **k** và **x**

**OUTPUT**

**k** số có giá trị gần với **x** nhất trong mảng. Các số này được xuất theo thứ tự tăng dần (trong trường hợp mảng có nhiều số có cùng khoảng cách tới **x**, ưu tiên chọn số có giá trị nhỏ hơn)

| Input | Output |
|:---|:---|
|16 <br/> 228 230 232 232 233 233 235 237 239 239 239 241 243 245 246 247 <br/> 5 398| 241 243 245 246 247|
|12 <br/> 26619 26620 26621 26622 26623 26625 26626 26626 26627 26628 26628 26629 <br/> 5 4146| 26619 26620 26621 26622 26623|
|5<br/> 1 2 4 7 10 <br/>3 4| 1 2 4|

## Problem 2: 
### [	Thêm và xóa](Them_Va_Xoa.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Không chỉ thuận tiện khi bổ sung phần tử, danh sách liên kết còn hiệu quả khi xóa bỏ phần tử ở đầu danh sách, cuối danh sách hoặc một vị trí đã xác định trong danh sách.

Hãy viết chương trình thực hiện các thao tác trên:

**INPUT**

Input gồm nhiều dòng, mỗi dòng sẽ có cấu trúc ở một trong 7 dạng sau:

- Dạng 0: Dòng bắt đầu bằng con số 0, theo sau là một số nguyên dương < 1000, chương trình cần phải thêm con số này vào đầu danh sách
- Dạng 1: Dòng này bắt đầu bằng con số 1, theo sau là một số nguyên dương < 1000, chương trình cần phải thêm con số này vào cuối danh sách
- Dạng 2: Dòng này bắt đầu bằng con số 2, theo sau là 2 số nguyên **a, b** < 1000, chương trình cần tìm vị trí đầu tiên mà số **a** xuất hiện trong danh sách, sau đó thêm số **b** vào sau số này. Nếu số **a** không có trong danh sách, thêm **b** vào đầu danh sách
- Dạng 3: Dòng này bắt đầu bằng con số 3, theo sau là một số nguyên dương **n** < 1000. Chương trình cần tìm số **n** đầu tiên trong danh sách và xóa số này.
- Dạng 4: Dòng này bắt đầu bằng con số 4, theo sau là một số nguyên dương **n** < 1000. Chương trình cần xóa tất cả số mang giá trị **n** ra khỏi danh sách.
- Dạng 5: Dòng này bao gồm con số 5, khi gặp dòng này, chương trình sẽ xóa số đầu tiên trong danh sách.
- Dạng 6: Dòng này bao gồm một con số 6. Đây là dòng cuối cùng trong input, báo hiệu input kết thúc

**OUTPUT**

In danh sách thu được sau khi thực hiện tất cả các thao tác theo yêu cầu trong input. Danh sách được in trên một dòng với mỗi số cách nhau bởi khoảng trắng. Nếu danh sách rỗng, xuất ra chữ “blank” (không có ngoặc kép)

VÍ DỤ:

| Input | Output |
|:---|:---:|
| 1 7<br/>3 3<br/>2 0 9<br/>3 3<br/>1 1<br/>5<br/>1 4<br/>1 4<br/>4 9<br/>0 1<br/>5<br/>0 3<br/>0 3<br/>5<br/>2 6 0<br/>5<br/>0 7<br/>4 8<br/>1 2<br/>1 0<br/>2 9 0<br/>2 1 8<br/>3 5<br/>3 0<br/>5<br/>4 1<br/>1 1<br/>1 7<br/>4 2<br/>2 7 5<br/>0 0<br/>1 3<br/>0 3<br/>3 6<br/>5<br/>2 1 9<br/>5<br/>5<br/>6 |7 5 8 4 4 0 1 9 7 3|
| 5<br/>1 6<br/>2 6 3<br/>5<br/>3 8<br/>0 0<br/>3 7<br/>0 9<br/>1 6<br/>5<br/>0 9<br/>2 6 9<br/>1 2<br/>1 1<br/>1 4<br/>5<br/>4 5<br/>1 6<br/>0 3<br/>2 9 3<br/>6 |3 0 3 6 9 3 2 1 4 6|
### ***GHI CHÚ***: 
Sinh viên chỉ được phép include thư viện nhập/xuất (iostream và cstdio) khi làm bài.


## Problem 3:
### [	Merge sorted array](Merge_Sorted_Array.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Cho 2 dãy số nguyên ***a*** có ***na*** số và ***b*** có ***nb*** số, mỗi dãy đã được sắp xếp theo thứ tự tăng dần. Hãy trộn hai dãy này lại để kết quả cuối cùng là một dãy tăng dần với  các phần tử là các phần tử của ***a*** và ***b***.
**INPUT**

Dòng đầu tiên chứa kích thước của hai mảng nhập vào ***na, nb (0 < na, nb <= 100000)***

Hai dòng tiếp theo lần lượt chứa các phần tử của mảng ***a*** và ***b***

**OUTPUT**
Như ví dụ

VÍ DỤ:

| Input | Output |
|:---|:---|
| 4 5<br/>1 2 4 9<br/>8 10 20 22 30| 1 2 4 8 9 10 20 22 30|
|5 3<br/>1 1 1 2 10<br/>3 4 100|	1 1 1 2 3 4 10 100 |

## Problem 4:
### [ROI (region of interest)](ROI.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Trong xử lý ảnh y khoa, người ta đôi lúc chỉ quan tâm đến một vùng nhỏ của bức ảnh. Với đầu vào là một bức ảnh nhị phân I với các điểm màu trắng (nhận giá trị 1) thể hiện các vùng tế bào có khả năng bị ung thư, các vùng màu đen (nhận giá trị 0) là các vùng không có dấu hiệu của ung thư. Biết chiều cao và chiều rộng của ảnh, hãy giúp các bác sĩ xác định các tế bào có khả năng bị ung thư trong vùng quan tâm của họ biết tọa độ góc trái trên và phải dưới của vùng này lần lượt là (top, left) và (bottom, right).

<img  src="ROI.png">

**INPUT**

h, w: lần lượt là chiều cao vào chiều rộng của ảnh

h dòng tiếp theo, mỗi dòng chứa w số nhận giá trị là 0 hoặc 1 chính là bức ảnh các bác sĩ đang xem xét

top, left, bottom, right: lần lượt là toạ độ trên, trái, phải, dưới của vùng được quan tâm
**OUTPUT**

Một bức ảnh nhị phân có kích thước (h,w) tương tự ảnh đầu vào 

với các tế bào ung thư nằm ngoài vùng quan tâm được chuyển thành giá trị 0 (màu đen)


VÍ DỤ:

| Input | Output |
|:---:|:---:|
| 3 4<br/>0 1 0 1<br/>1 1 1 0<br/>0 1 1 0<br/>0 0 2 2| 0 1 0 0<br/>1 1 1 0<br/>0 1 1 0|



## Problem 5:
### [Reshape matrix](Reshape_Matrix.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Cho một ma trận có kích thước mxn và hai biến r,c tương ứng với số dòng và số cột muốn reshape.

Ma trận được reshape có kích thước rxc và được điền đầy đủ các phần tử của ma trận gốc theo chiều ngang.

Nếu có thể reshape được ma trận, xuất ra ma trận mới.

Ngược lại, xuất ma trận gốc.

 

**INPUT**

Dòng đầu tiên gồm hai số nguyên dương ***n , m ( 2 ≤ n , m ≤ 3000 )*** — Theo thứ tự là số hàng,cột của ma trận gốc.

Dòng thứ hai gồm hai số nguyên dương ***r , c*** — Theo thứ tự là số hàng,cột của ma trận muốn reshape thành. 

***n*** dòng tiếp theo là giá trị từng hàng của ma trận gốc ***a1, a2, ..., am ( − 10 5 ≤ a i ≤ 10 5 )*** — Các phần tử cách nhau ***một khoảng trắng***.

**OUTPUT**

Nếu có thể reshape được ma trận, xuất ra ma trận mới.

Ngược lại, xuất ma trận gốc.

**VÍ DỤ:**

| Input | Output |
|:---|:---|
| 2 3<br/>3 2<br/>1 2 3<br/>4 5 6 |1 2<br/>3 4<br/>5 6|
|3 3<br/>1 9<br/>5 7 9<br/>9 6 4<br/>3 5 8|5 7 9 9 6 4 3 5 8|
|3 3<br/>1 8<br/>4 2 1<br/>3 8 9<br/>4 6 7 |4 2 1<br/>3 8 9<br/>4 6 7|

## Problem 6: 
### [Online game](Online_Game.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Khi làm việc với yêu cầu tìm kiếm, chúng ta có thể sử dụng thuật toán tìm kiếm nhị phân. Tuy nhiên thuật toán tìm kiếm nhị phân chỉ có thể chạy trên cấu trúc dữ liệu mảng và mảng đó phải được sắp xếp thứ tự. Việc sắp xếp thường có độ phức tạp khá cao, điển hình là trong trường hợp sau đây:

Giả định công ty NaViGame đang duy trì một hệ thống server rất lớn đáp ứng cho hàng chục triệu acccount của các game thủ. Hệ thông server này duy trì một danh sách các game thủ đang online cho phép nhà quản trị có thể kiểm tra xem một game thủ bất kỳ nào đó có đang online hay không. Hãy giúp công ty NaViGame xây dựng module kiểm tra game thủ online này.

**INPUT**

Mỗi dòng của input chứa hai con số a và b. Số a có giá trị là 1 hoặc 2 đại diện cho hai tình huống là có game thủ đăng nhập vào hệ thống và người quản trị vừa nhập một yêu cầu kiểm tra. Số b là mã số của game thủ trong tình huống đó (giá trị b không quá 1 tỷ).

Ví dụ như dòng: 1 565481 cho biết game thủ với mã số 465481 vừa mới đăng nhập vào hệ thống

dòng: 2 87126 cho biết người quản trị muốn kiểm tra xem game thủ với mã số 87126 có đang online trong hệ thống hay không.

Input sẽ kết thúc bằng dòng chỉ chứa một số 0.

**OUTPUT**

Ứng với mỗi yêu cầu kiểm tra của nhà quản trị xuất ra trên một dòng giá trị 0 nếu game thủ đó không online. Nếu game thủ đang online, xuất ra 1

**VÍ DỤ:**

| **INPUT** | **OUTPUT** |
|:---|:---:|
| 1 1<br/>1 2<br/>1 3<br/>2 4<br/>2 1<br/>1 5<br/>0| 0<br/>1|
|1 2<br/>2 3<br/>1 44<br/>1 5<br/>2 5<br/>2 1<br/>2 2<br/>1 3<br/>0|0<br/>1<br/>0<br/>1|


## Problem 7:
### [Online game 2](Online_Game_2.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Nếu bạn có thể chèn thêm giá trị vào cây nhị phân thì chắc hẳn bạn cũng có thể xóa giá trị ra khỏi cây chứ nhỉ?

Giả định công ty NaViGame đang duy trì một hệ thống server rất lớn đáp ứng cho hàng chục triệu acccount của các game thủ. Hệ thông server này duy trì một danh sách các game thủ đang online cho phép nhà quản trị có thể kiểm tra xem một game thủ bất kỳ nào đó có đang online hay không. Hãy giúp công ty NaViGame xây dựng module kiểm tra game thủ online này.

**INPUT**

Mỗi dòng của input chứa hai con số a và b. Số a có giá trị là 1 hoặc 2 hoặc 3 đại diện cho các tình huống là có game thủ đăng nhập vào hệ thống, có game thủ đăng xuất khỏi hệ thống và người quản trị vừa nhập một yêu cầu kiểm tra. Số b là mã số của game thủ trong tình huống đó (giá trị b không quá 1 tỷ).

Ví dụ như

Dòng: 1 565481 cho biết game thủ với mã số 465481 vừa mới đăng nhập vào hệ thống

Dòng: 2 87126 cho biết người quản trị muốn kiểm tra xem game thủ với mã số 87126 có đang online trong hệ thống hay không.

Dòng: 3 48769 cho biết là game thủ có mã số 48769 vừa đăng xuất khỏi hệ thống.

Input sẽ kết thúc bằng dòng chỉ chứa một số 0.

**OUTPUT**

Ứng với mỗi yêu cầu kiểm tra của nhà quản trị xuất ra trên một dòng giá trị 0 nếu game thủ đó không online. Nếu game thủ đang online, xuất ra 1


**VÍ DỤ:**

|**INPUT** | **OUTPUT** |
|:---|:---:|
| 1 1<br/>2 8<br/>1 5<br/>1 1<br/>1 0<br/>1 3<br/>3 7<br/>3 9<br/>1 3<br/>1 4<br/>2 1<br/>1 8<br/>1 7<br/>2 9<br/>1 7<br/>1 9<br/>1 8<br/>3 4<br/>3 8<br/>2 1<br/>1 8<br/>3 3<br/>1 2<br/>1 2<br/>3 4<br/>1 5<br/>1 8<br/>1 2<br/>1 3<br/>2 1<br/>1 8<br/>1 4<br/>1 7<br/>2 7<br/>3 2<br/>1 7<br/>1 7<br/>1 4<br/>3 5<br/>1 1<br/>1 8<br/>3 6<br/>0 |0<br/>1<br/>0<br/>1<br/>1<br/>1|
|1 1<br/>1 3<br/>1 2<br/>1 4<br/>2 1<br/>1 1<br/>3 1<br/>2 1<br/>0|1<br/>0|


