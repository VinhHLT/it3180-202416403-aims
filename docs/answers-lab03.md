# Câu hỏi thảo luận Lab 03

## 1. Merge base là gì? Vai trò của nó khi hợp nhất nhánh?
- **Merge base** là commit tổ tiên chung gần nhất (Best Common Ancestor) của hai nhánh đang được hợp nhất.
- Trong thuật toán trộn 3 chiều (**3-way merge**), Git đối chiếu trạng thái của 2 đầu nhánh với `merge base`:
  - Nếu chỉ một nhánh thay đổi so với `merge base`, Git tự động nhận thay đổi đó.
  - Nếu cả hai nhánh cùng sửa một dòng theo hai nội dung khác nhau so với `merge base`, Git báo **Merge Conflict** để lập trình viên trực tiếp kết hợp ý đồ của cả hai bên.

## 2. Vì sao trên `master` và `release/*` phải dùng `git revert` mà không dùng `git reset`?
- `git reset` dời con trỏ nhánh lùi về quá khứ và xóa bỏ commit khỏi lịch sử (viết lại lịch sử), vi phạm luật bảo vệ nhánh (Branch Protection) và làm hỏng lịch sử trên máy của các thành viên khác.
- `git revert` tạo ra một commit mới đảo ngược hoàn toàn thay đổi của commit bị lỗi mà không xóa lịch sử cũ.
- Cách làm này vừa tuân thủ quy trình Pull Request trên nhánh được bảo vệ, vừa đảm bảo tính kiểm toán (Auditability) trong SCM: ghi nhận rõ lỗi xuất hiện ở đâu và được hoàn tác tại thời điểm nào.
