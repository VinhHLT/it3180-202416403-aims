# Câu hỏi thảo luận Lab 02

## 1. Vì sao phải đồng bộ nhánh với `master` trước khi gửi/gộp Pull Request?
- Khi làm việc song song, `origin/master` có thể đã tiến thêm các commit mới từ đồng đội.
- Việc kéo `origin/master` về nhánh tính năng trước giúp:
  1. Phát hiện và giải quyết xung đột (merge conflict) ngay trên máy cá nhân của người hiểu rõ tính năng đó nhất.
  2. Kiểm thử tích hợp sớm để tránh xung đột ngữ nghĩa (code không báo lỗi dòng nhưng ghép lại chạy sai).
  3. Đảm bảo nguyên tắc SCM: phiên bản được reviewer duyệt trên PR chính xác là phiên bản sẽ chạy sau khi gộp vào `master`.

## 2. Khi nào KHÔNG được dùng `git rebase`?
- Tuyệt đối không dùng `git rebase` trên các nhánh công khai đã chia sẻ cho nhiều người cùng làm việc (như `master`, `release/*`).
- Lý do: `rebase` viết lại lịch sử bằng cách tạo ra các commit mới với mã SHA mới. Nếu rebase nhánh dùng chung, lịch sử giữa máy các thành viên và remote sẽ bị lệch nhau, gây rối loạn lịch sử và mất mát dữ liệu khi đồng bộ. Chỉ dùng `rebase` trên các commit/nhánh cá nhân chưa chia sẻ.

## 3. `feature/*` khác `topic/*` ra sao? So sánh 3 kiểu Merge.
- **Phân biệt `feature/*` và `topic/*`:**
  - `feature/*`: Dùng để phát triển các chức năng nghiệp vụ của phần mềm (ví dụ: `feature/cart-print`, `feature/search-by-title`).
  - `topic/*`: Dùng cho các thay đổi về tài liệu, cấu hình quy trình, công cụ hoặc CI (ví dụ: `topic/pr-template`, `topic/use-case-diagram`).
- **So sánh 3 kiểu Merge:**
  - **Merge commit:** Giữ toàn bộ commit chi tiết và tạo thêm 1 commit hợp nhất (2 cha); dễ revert cả tính năng bằng 1 lệnh (`-m 1`) nhưng đồ thị lịch sử phi tuyến tính.
  - **Squash and merge:** Gộp mọi commit trên nhánh phụ thành 1 commit duy nhất trên `master`; giúp lịch sử `master` tuyến tính và sạch gọn nhưng mất chi tiết các commit nhỏ.
  - **Rebase and merge:** Đưa từng commit sang `master` với SHA mới tạo thành đường thẳng tuyến tính; giữ được chi tiết từng commit nhưng khi muốn revert cả tính năng phải revert nhiều commit.
