# Câu hỏi thảo luận Lab 03
1. Merge base là tổ tiên chung gần nhất của hai nhánh, dùng trong thuật toán 3-way merge để phát hiện conflict khi hai nhánh cùng sửa một vùng code.
2. Trên master và release/* phải dùng git revert thay vì reset vì reset xóa lịch sử (viết lại lịch sử), vi phạm bảo vệ nhánh, trong khi revert tạo commit đảo ngược giữ nguyên lịch sử kiểm toán.
