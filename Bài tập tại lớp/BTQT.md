#  CÁC VÍ DỤ VỀ LINEAR REGRESSION TRONG THỰC TẾ
## Ví dụ 1: Dự đoán khả năng qua môn của một sinh viên
 - **Input**: Thời gian có mặt tại lớp(int), số giờ học trong một ngày(int), số deadline 
 về nhà hoàn thành được(int)
- **Output**: Sinh viên đó có khả năng qua môn được hay không.
- **Thu thập và xử lý dữ liệu**: Thu thập thông tin về thời gian có mặt tại lớp, số giờ tự học, số dealine hoàn thành
dựa trên bảng khảo sát hàng năm của trường.


## Ví dụ 2: Dự đoán số tiền công ty bảo hiểm phải trả cho một người.
- **Input**: Tuổi(int), cân nặng(int), chỉ số khối cơ thể(flaot), tình trạng hôn nhân(bool).
- **Output**: Số tiền công ty phải trả cho người đó trong năm.
- **Thu thập và xử lý dữ liệu**: file CSV thông tin hóa đơn mà công ty bảo hiểm chi trả trong 20 năm gần nhất với các thuộc tính nêu trên.


## Ví dụ 3: Dự đoán lượng mưa trong năm tại BRVT
 - **Input**: Nhiệt độ trung bình(float), độ ẩm trung bình(float) của 5 tháng đầu năm.
 - **Output**: Lượng mưa trung bình trong năm(float).
 - **Thu thập và xử lý dữ liệu**: file CSV bao gồm các thông số như trên trong năm của 20 năm gần nhất từ Trung tâm dự báo Khí tượng Thủy văn Quốc Gia
## Ví dụ 4: Dự đoán khả năng trúng tuyển vào trường ĐHCNTT
- **Input**: Điểm Toán(float), Điểm Lý(float), Điểm Hóa(float)
- **Output**: Khả năng trúng tuyển vào trường hay không.
-  **Thu thập và xử lý dữ liệu**: Nhà Trường sẽ công bố kết quả trúng tuyển của từng thí sinh hàng năm sau đó chúng ta thống kê lại và gom chúng lại thành một khối định dữ liệu chung có thể ở định dạng CSV.
