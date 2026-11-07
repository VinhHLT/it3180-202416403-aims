# Thảo luận Lab 05
1. Release-first tạo bản vá trực tiếp trên bản đang chạy nên khắc phục nhanh cho khách hàng; Upstream-first sửa trên master trước nên tránh quên cập nhật ở nhánh chính.
2. Nếu quên lan truyền sang release/lab05, lệnh `git tag --contains <FIX_SHA>` hoặc vòng lặp kiểm tra thực thi trên các phiên bản sẽ phát hiện ngay.
