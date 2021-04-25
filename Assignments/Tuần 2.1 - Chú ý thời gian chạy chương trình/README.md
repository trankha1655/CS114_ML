## Problem 1: [Tìm số gần nhất(nhiều lần)](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Tim_So_Gan_Nhat.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Cho mảng số nguyên A đã sắp xếp tăng dần, tìm trong mảng k số có giá trị gần với giá trị x nhất.

**INPUT**

Dòng đầu tiên cho biết số phần tử của mảng

Dòng thứ 2 là toàn bộ mảng liệt kê trên một hàng, các phần tử cách nhau bởi khoảng trắng

Các dòng sau đó, mỗi dòng chứa 02 số **k  và x** , **k≤n**

Input kết thúc bằng một dòng trống không có nội dung.

**OUTPUT**
Ứng với mỗi cặp số **(k, x)** xuất ra màn hình số lớn nhất và nhỏ nhất trong dãy **k** số có giá trị gần với **x** nhất.

**nếu có nhiều dãy thõa yêu cầu, xuất ra dãy nằm gần phần đàu mảng A nhất.**

**VÍ DỤ**

| Input | Output |
|:---:|:---:|
|15 <br/> 27753 27754 27755 27756 27758 <br/> 27758 27760 27761  27763 27764 <br/>27764 27765 27766 27766  27766 <br/> 6 43416 <br/> 3 34222 <br/> 3 34222 <br/> 9 29492 <br/>15 10434  <br/> 4 37086  <br/> 10 35250 <br/> |  27764 27766 <br/> 27766 27766 <br/>27760 27766 <br/> 27753 27766 <br/>27765 27766 <br/>27758 27766  |
| 21 <br/> 26475 26477 26479 26481 26481 26483 26483 <br/> 26484 26485 26487 26489 26489 26490 26491 <br/> 26492 26492 26493 26493 26494 26495 26496 <br/> 3 32272<br/>4 27892 <br/>9 18564 <br/>10 15216 <br/>4 15714 <br/> 20 256 <br/> 11 38574| 26494 26496 <br/>26493 26496 <br/> 26475 26485  <br/> 26475 26487<br/> 26475 26481<br/>26475 26495 <br/> 26489 26496<br/> |

## Problem 2: [Đếm Node Lá](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Dem_Node_La.py)
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

## Problem 6: [Tần Suất](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Tan_Suat.py)
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
|:---:|:---:|
|3 | |
|5 4 | |
|1 2 4 8 5 | 1|
|4 15| 2|
|15 5 15 5 | 0|
|4 9 | |
|4 4 5 5 | |
|2 | |
|1 -15 | |
|15 | 0|
|5 -99 | 5|
|-99 -99 -99 -99 | |



## Problem 7: [Số Có Hậu](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/So_Co_Hau.py)
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
|:---:|:---:|
| 23 122 | 1|








