## Problem 1: [Số amstrong](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/So_Armstrong.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**


Kiểm tra Số Armstrong (Số Armstrong là số có **K** chữ số và tổng lũy thừa bậc **K** của các chữ số bằng chính nó)

**INPUT**

Một số nguyên không âm

**OUTPUT**

Xuất **True** nếu số nhập vào là số Armstrong, ngược lại **False**

| Input | Output |
|:---:|:---:|
| 153 | True|

## Problem 2: [Bán Hàng](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Ban_Hang.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Nam đang là quản lí một cửa hàng nhỏ trong thị trấn. Cửa hàng của Nam có **n** hàng hóa, mỗi hàng hóa thứ **i** có giá **ai**
đồng,

Mỗi ngày, có rất nhiều khách hàng ghé cửa hàng của Nam và liên tục hỏi giá của từng sản phẩm. Do có quá nhiều hàng hóa nên Nam không thể nào nhớ hết giá của chúng. Vì thế, Nam đã quyết định bán đồng giá tất cả các hàng hóa trong cửa hàng của mình.

Tuy nhiên, để không lỗ vốn, Nam muốn sau khi tất cả **n** hàng hóa trong cửa hàng được bán hết thì thu được tổng số tiền **bằng (hoặc lớn hơn)** so với tổng giá hàng hóa bán với giá gốc.

Mặt khác, Nam không muốn mất khách nếu giá bán quá lớn. Vì vậy, Nam phải bán **n** hàng hóa với giá **tối thiểu** sao cho tổng số tiền thu được sau khi bán hết hàng hóa có trong cửa hàng phải **bằng (hoặc lớn hơn tối thiểu)** so với tổng giá hàng hóa bán với giá gốc.

Với mỗi testcase các bạn hãy giúp Nam tìm ra giá bán phù hợp.

**INPUT**

Dòng đầu tiên là một số nguyên **q(1≤q≤100)**— số lượng testcase. Theo sau mỗi **q** dòng là:

Dòng đầu tiên của testcase là một số nguyên **(1≤q≤100)** — số lượng hàng hóa. Dòng thứ hai 
gồm **n**  số nguyên **a1,a2,...,an(1≤ai≤107)** —  **ai** giá gốc của hàng hóa thứ **i**.

**OUTPUT**

Với mỗi testcase in ra giá bán đồng giá tối thiểu của n hàng hóa sao cho tổng số tiền thu được sau 
khi bán hết hàng hóa có trong cửa hàng phải **bằng (hoặc lớn hơn tối thiểu)** so với tổng giá hàng hóa bán 
với giá gốc.

VÍ DỤ:

| Input | Output |
|:---:|:---:|
| 3 | |
| 5 | |
| 1 2 3 4 5 | 3|
| 3 | |
| 1 2 2| 2|
| 4 | |
| 1 1 1 1 | 1|
| 1 | |
| 2 | 778|
| 777 778 | |

## Problem 3: [Xử lý chuỗi](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Xu_Ly_Chuoi.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Bob đang tham dự một lớp học lập trình. Bài tập đầu tiên của Bob là viết một chương trình đơn giản. 
Chương trình sẽ yêu cầu nhập một chuỗi, sau đó nếu có chữ viết hoa trong chuỗi thì thay thế chúng 
bằng những chữ viết thường. Xóa hết tất cả các nguyên âm và chèn dấu "." trước mỗi phụ âm có trong
chuỗi đó.

Biết nguyên âm là những kí tự "A","O","Y","E","U","I", và những kí tự còn lại là phụ âm. Chương trình 
sẽ nhận đầu vào là mỗi chuỗi và đầu ra là một chuỗi sau khi xử lí những yêu cầu trên.

Bob đang loay hoay không biết làm bài này như thế nào. Bạn hãy giúp Bob nhé.

**INPUT**

Dòng đầu tiên là một chuỗi gồm những cữ cái Latin viết hoa và viết thường, có độ dài từ 1 đến 100.

**OUTPUT**

Chuỗi kết quả.

VÍ DỤ:

| Input | Output |
|:---:|:---:|
| tour | .t.r|
|aBAcAba |	.b.c.b |
| pyThon |.p.t.h.n|

## Problem 4: [Ngôn ngữ của Lan](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Ngon_Ngu_Cua_Lan.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Lan đang học ở một trường ngoại ngữ ở Tp.HCM. Lan rất yêu thích ngôn ngữ, đặc biệt là ngữ pháp. 
Khi  bước vào năm thứ 3, Lan quyết định tạo ra một ngôn ngữ mới dễ sử dụng nhất có thể đủ để 
nói chuyện với bạn bè. Ngôn ngữ mới của Lan có tên là Lan's Language và thỏa theo những ngữ pháp sau:

  Có 3 loại từ trong Lan's Language: danh từ, động từ và tính từ. Mỗi từ trong Lan's Language thuộc một trong 3 loại từ đó.
  
  Có 2 giới tính: Nam và Nữ. Mỗi từ trong Lan's Language thuộc một trong 2 giới tính đó.
  
  Tính từ nam là những từ kết thúc với -lios và Tính từ nữ là những từ kết thúc với -liala.
  
  Danh từ nam là những từ kết thúc với -etr và  Danh từ nữ là những từ kết thúc với -etra.
  
  Động từ nam là những từ kết thúc với -initis và  Động từ nữ là những từ kết thúc với -inites.
  
  Các từ trong Lan's Language luôn kết thúc bằng 1 trong các đuôi trên.
  
  Các từ mà chỉ có mỗi đuôi như "lios", "liala", "etr"... cũng thuộc Lan's Language.
  
  Không có dấu câu, ngữ pháp chia thì và các dạng biến đổi từ trong Lan's Language.
  
  Một câu trong Lan's Language là một từ hợp lệ (thỏa những tính chất trong Lan's Language) hoặc là một mệnh đề hợp lệ.
  
Một mệnh đề hợp lệ trong Lan's language phải thỏa 2 điều kiện sau:

  Những từ trong mệnh đề phải hợp lệ và được sắp xếp theo thứ tự: Tính từ + Danh từ + Động từ. 
  Trong đó: Tính từ có thể có 1 hoặc nhiều hoặc không có nhưng phải đứng trước Danh từ. Chỉ có
  duy nhất một Danh từ trong câu. Động từ có thể có 1 hoặc nhiều hoặc không có nhưng phải
  đứng sau Danh từ.
  
  Tất cả các từ trong mệnh đề phải cùng giới tính.
Cho một câu gồm một chuỗi các từ, nhiệm vụ của bạn là viết một chương trình kiểm tra xem câu được nhập vào có thỏa mãn 
những tính chất của Lan's language hay không? 

**OUTPUT**

Nếu câu nhập vào thỏa mãn những tính chất của Lan's language, xuất YES
Ngược lại xuất NO


VÍ DỤ:

| Input | Output |
|:---:|:---:|
| petr| YES|
| etis atis animatis etis atis amatis | NO|
| nataliala kataliala vetra feinites | YES|

## Problem 4: [Rút Gọn Phân Số](https://github.com/trankha1655/CS114_ML/blob/main/Assignments/Tu%E1%BA%A7n%201.2%20-%20t%C4%83ng%20t%E1%BB%91c%20t%E1%BB%AB%20t%E1%BB%AB/Rut_Gon_Phan_So.py)
**Time limit per test: ... second**

**Memory limit per test: ... megabytes**

Viết chương trình rút gọn phân số.

**INPUT**

Dòng đầu tiên là một số nguyên **n(1≤n≤100)** — Số lượng phân số cần rút gọn

n dòng tiếp theo là hai số nguyên **a,b(a,b≥1) — a,b** lần lượt là tử số và mẫu số.

**OUTPUT**

Ứng với **n** dòng, in ra theo thứ tự **tử số** và **mẫu số** (cách nhau một khoảng trắng) sau khi rút gọn; mẫu số
chỉ được in khi lớn hơn 1.

**VÍ DỤ:**

| Input | Output |
|:---:|:---:|
| 5| |
| 6 8 | 3 4|
| 3 7 | 3 7|
| 5 10 | 1 2|
| 10 5 | 2|
| 25 100 | 1 4|
| 2| |
| 77 105 | 11 15|
| 121 11 | 11|









