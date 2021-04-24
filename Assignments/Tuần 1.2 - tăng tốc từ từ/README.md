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




