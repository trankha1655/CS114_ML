# Tuần 1.2 - Tăng tốc từ từ

## Progress
|ID   | Problem | Status 
|:---:|:---:|:---:|
|1 | [	Tìm số gần nhất (nhiều lần)](#problem-1) | 	:white_check_mark: 
|2 |[Duyệt theo chiều rộng](#problem-2)| :white_check_mark: 
|3 | [		Chiều cao cây](#problem-3) | :white_check_mark:
|4 | [	Đếm node lá)](#problem-4)| :white_check_mark:
|5 | [		Print mảng 2d](#problem-5)| :white_check_mark:
|6 | [	Tần suất](#problem-6)| :white_check_mark:
|7 | [Số có hậu](#problem-7) | :white_check_mark:



## Problem 1:
### [Tìm số gần nhất (nhiều lần)](Tim_So_Gan_Nhat.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Cho mảng số nguyên A đã sắp xếp tăng dần, tìm trong mảng k số có giá trị gần với giá trị x nhất.

**INPUT**

Dòng đầu tiên cho biết số phần tử của mảng

Dòng thứ 2 là toàn bộ mảng liệt kê trên một hàng, các phần tử cách nhau bởi khoảng trắng

Các dòng sau đó, mỗi dòng chứa 02 số ***k***  và ***x*** , ***k ≤ n*** 

Input kết thúc bằng một dòng trống không có nội dung.


**OUTPUT**
Ứng với mỗi cặp số **(k, x)** xuất ra màn hình số lớn nhất và nhỏ nhất trong dãy **k** số có giá trị gần với **x** nhất.

**nếu có nhiều dãy thõa yêu cầu, xuất ra dãy nằm gần phần đàu mảng A nhất.**

**VÍ DỤ**

| Input | Output |
|:---|:---:|
|15 <br/> 27753 27754 27755 27756 27758 <br/> 27758 27760 27761  27763 27764 <br/>27764 27765 27766 27766  27766 <br/> 6 43416 <br/> 3 34222 <br/> 9 29492 <br/>15 10434  <br/> 4 37086  <br/> 10 35250 <br/> |  27764 27766 <br/> 27766 27766 <br/>27760 27766 <br/> 27753 27766 <br/>27765 27766 <br/>27758 27766  |
| 21 <br/> 26475 26477 26479 26481 26481 26483 26483 <br/> 26484 26485 26487 26489 26489 26490 26491 <br/> 26492 26492 26493 26493 26494 26495 26496 <br/> 3 32272<br/>4 27892 <br/>9 18564 <br/>10 15216 <br/>4 15714 <br/> 20 256 <br/> 11 38574| 26494 26496 <br/>26493 26496 <br/> 26475 26485  <br/> 26475 26487<br/> 26475 26481<br/>26475 26495 <br/> 26489 26496<br/> |



## Problem 2: 	
### [Duyệt theo chiều rộng](Duyet_Theo_Chieu_Rong.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Cho một dãy số. Lần lượt thêm các số trong dãy vào một cây nhị phân tìm kiếm, sau đó duyệt và xuất cây ra màn hình theo thứ tự duyệt theo chiều rộng (các node có mức thấp được xuất trước, đối với các node có cùng mức xuất node có giá trị nhỏ trước)

**INPUT**

Input gồm nhiều dòng, mỗi dòng sẽ có cấu trúc ở 1 trong 4 dạng sau:

- Dạng 0: Dòng bắt đầu bằng con số 0, theo sau là một số nguyên dương < 1000, chương trình cần phải thêm con số này vào đầu danh sách

- Dạng 1: Dòng này bắt đầu bằng con số 1, theo sau là một số nguyên dương < 1000, chương trình cần phải thêm con số này vào cuối danh sách

- Dạng 2: Dòng này bắt đầu bằng con số 2, theo sau là 2 số nguyên a, b < 1000, chương trình cần tìm vị trí đầu tiên mà số a xuất hiện trong danh sách, sau đó thêm số b vào sau số này. Nếu số a không có trong danh sách, thêm b vào đầu danh sách

- Dạng 3: Dòng này bao gồm duy nhất một con số 3. Đây là dòng cuối cùng trong input, báo hiệu input kết thúc



**OUTPUT**

Chiều cao của cây nhị phân tìm kiếm thu được khi lần lượt thêm các số trong danh sách vào cây.

**VÍ DỤ**

| Input | Output |
|:---|:---:|
| 0 6<br/>1 6<br/>0 5<br/>1 0<br/>0 3<br/>0 0<br/>0 5<br/>0 1<br/>1 1<br/>1 7<br/>2 0 3<br/>2 4 2<br/>0 0<br/>2 0 9<br/>3|6|
| 1 1<br/>0 8<br/>1 4<br/>1 0<br/>1 5<br/>1 9<br/>0 6<br/>3|4|

## Problem 3:
### [Chiều cao cây](Chieu_Cao_Cay.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Bạn Bình đã làm xong bài danh sách liên kết giờ chuyển qua bài cây nhị phân tìm kiếm. 

Hỏi nếu Bình đem danh sách đó nhập vào cây nhị phân tìm kiếm thì cây cao bao nhiêu?

**INPUT**

Một dãy số nguyên khác 0, mỗi số trên một hàng. Dãy số tận cùng bằng số 0

**OUTPUT**

Số node lá trong cây

**VÍ DỤ**

| Input | Output |
|:---:|:---:|
| 393 
 981 <br/>841 <br/> 133 <br/> 891 <br/> 739 <br/> 663 <br/> 119 <br/> 497 <br/> 865 <br/>54 <br/>631 <br/> 561 <br/>51<br/>227<br/>841 <br/>352 <br/>996 <br/>505 <br/>0 |5|


## Problem 4:
### [Đếm Node Lá](Dem_Node_La.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Cho một dãy số, hãy cho biết số node lá của cây nhị phân tìm kiếm thu được khi thêm lần lượt các số 
trong dãy vào cây.

**INPUT**

Một dãy số nguyên khác 0, mỗi số trên một hàng. Dãy số tận cùng bằng số 0

**OUTPUT**

Số node lá trong cây

**VÍ DỤ**

| Input | Output |
|:---:|:---:|
| 393 
 981 <br/>841 <br/> 133 <br/> 891 <br/> 739 <br/> 663 <br/> 119 <br/> 497 <br/> 865 <br/>54 <br/>631 <br/> 561 <br/>51<br/>227<br/>841 <br/>352 <br/>996 <br/>505 <br/>0 |5|

## Problem 5:
### [Print mảng 2d](Print_Mang_2D.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Bình đang làm bài tập mảng 2 chiều nâng rất rất cao. Bình cần xuất mảng ra màn hình để quan sát. 

Tuy nhiên do các số nguyên trong mảng độ dài khác nhau nên khi xuất ra nhìn rất lộn xộn, không biết được số nào ở cột nào. 

Bạn hãy viết giúp Bình hàm xuất mảng một cách ngay ngắn.

**INPUT**

Dòng đầu tiên chứa hai số **r** và **c** là số dòng và số cột của mảng, mỗi số không quá 1000.

**r** dòng tiếp theo, mỗi dòng chứa **c** số nguyên. Đây là các phần tử trong mảng 2 chiều

**OUTPUT**

Mảng 2 chiều được canh lề phải ở các cột. Tức là chữ số cuối cùng của các cột được viết thẳng hàng với nhau. Các chỗ trống được lấp đầy bằng ký tự khoảng trắng

Lưu ý là đê đảm bảo chính xác ở cuối mỗi dòng của ma trận chỉ được xuất ký tự xuống dòng, không được xuất khoảng trắng thừa.

**VÍ DỤ**

| Input | Output |
|:---|---|
|3 3 <br/> 593795850 925527 97481109<br/>8190 9258 2323<br/>-8328541 62240 70544569| 593795850 925527 97481109<br/> &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; 8190 &nbsp; &nbsp; 9258 &nbsp; &nbsp; &nbsp; &nbsp; 2323 <br/> &nbsp; -8328541 &nbsp; 62240 70544569 |
|5 5 <br/>28913 26846 85 19649 8524<br/>7970 31692 11666 2213 6747<br/>22640 18740 30793 9860 15977<br/>24997 18366 18071 8766 20104<br/>18223 27172 2671 101 2170|28913 26846 &nbsp; &nbsp; &nbsp; 85 19649 &nbsp; 8524<br> &nbsp; 7970 31692 11666 &nbsp; 2213 &nbsp; 6747<br> 22640 18740 30793 &nbsp; 9860 15977<br> 24997 18366 18071 &nbsp; 8766 20104<br> 18223 27172 &nbsp; 2671 &nbsp; &nbsp; 101 &nbsp; 2170|


## Problem 6:
### [Tần Suất](Tan_Suat.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Viết chương trình nhập vào một dãy gồm **n** số và biến **k**. Đếm số lần xuất hiện của **k** trong dãy đó. 

**INPUT**

Dòng đầu tiên gồm một số nguyên dương **q** — số lượng testcase. Theo sau mỗi testcase gồm:

Dòng thứ nhất là hai số nguyên dương **n,k (1≤n≤1000),(−105≤k≤105)**— Số phần tử của 
dãy và giá trị cần tìm vị trí.

Dòng thứ hai là giá trị các phần tử trong dãy **a1,a2,...,an(−105≤ai≤105)**

**OUTPUT**

Ứng với mỗi testcase, xuất ra trên một dòng số lần xuất hiện của **k**.

**VÍ DỤ**

| Input | Output |
|:---|:---:|
 |3 <br/>5 4 <br/>1 2 4 8 5 <br/>4 15<br/> 15 5 15 5 <br/>4 9 <br/>4 4 5 5 | 1 <br/>2<br/>0|
 |2 <br/>1 -15 <br/>15 <br/>5 -99<br/> -99 -99 -99 -99 |0<br/>5 |



## Problem 7: 
### [Số Có Hậu](So_Co_Hau.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Jim thích các phim và truyện kết thúc có hậu. Một lần gặp may với số n và từ đó Jim rất có cảm tình với tất cả 
các số nguyên kết thúc bằng **n**, coi chúng là những số có hậu. Ví dụ với **n** = 25 thì các số 625, 
553325,1025 là những số có hậu, còn 3255 – không có hậu!

Jim không thích các ràng buộc và hạn chế. Nhưng trong thế giới thực của chúng ta ràng buộc và 
hạn chế là điều tất yếu. Một người bạn của Jim khuyên chỉ nên quan tâm đến các số nguyên không vượt quá **m** 
và dĩ nhiên, Jim muốn biết có bao nhiêu số có hậu không vượt quá **m**.

**INPUT**

Vào từ thiết bị nhập chuẩn gồm một dòng chứa 2 số nguyên **n** và **m (1 ≤ n ≤ m ≤ 2×109)**.

**OUTPUT**

Đưa ra thiết bị xuất chuẩn một số nguyên – số lượng số có hậu tìm được.

**VÍ DỤ**

| Input | Output |
|:---|:---:|
| 23 122 | 1|








