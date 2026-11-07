# Câu hỏi thảo luận Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ:**
  - `--global`: Lưu tại tệp `~/.gitconfig` (hoặc `~/.config/git/config`) trong thư mục người dùng của hệ điều hành.
  - `--local`: Lưu tại tệp `.git/config` nằm ngay bên trong thư mục `.git/` của repository hiện tại.
- **Sự khác biệt và độ ưu tiên:**
  - `--global` áp dụng cho mọi repository của người dùng trên máy tính đó.
  - `--local` chỉ áp dụng riêng cho repository hiện tại.
  - Độ ưu tiên: `--local` > `--global` > `--system` (cấu hình `--local` sẽ ghi đè `--global`).

## 2. Vì sao dùng `git mv` thay vì xóa rồi tạo tệp mới?
- `git mv` thực hiện đồng thời việc di chuyển tệp và cập nhật cả thao tác xóa đường dẫn cũ lẫn thêm đường dẫn mới vào vùng Staging (Index).
- Nhờ đó, Git và GitHub nhận diện chính xác tệp ở trạng thái `renamed` thay vì tính là xóa tệp cũ và thêm tệp mới rời rạc.
- Trong Quản lý cấu hình phần mềm (SCM), việc này giúp bảo toàn xuyên suốt lịch sử thay đổi của Configuration Item, cho phép truy vết đầy đủ bằng lệnh `git log --follow`.

## 3. `release/lab01` có phải là baseline không?
- **Có.** Baseline là một phiên bản cấu hình đã được thống nhất và đóng băng tại một mốc xác định để làm cơ sở cho các bước tiếp theo, chỉ sửa đổi qua quy trình kiểm soát chính thức.
- Nhánh `release/lab01` đóng băng trạng thái nộp bài của Lab 01, tách biệt hoàn toàn với sự phát triển tiếp diễn trên `master` và chỉ nhận các bản vá khẩn cấp (`hotfix/*`) qua Pull Request.

## 4. Vì sao không commit thẳng lên `master` dù làm một mình?
- **Cô lập rủi ro:** Giữ cho nhánh `master` luôn ở trạng thái ổn định, chạy đúng; mọi thử nghiệm hoặc tái cấu trúc được cô lập trên nhánh riêng.
- **Tự rà soát (Self-review):** Tạo Pull Request giúp kiểm tra lại toàn bộ thay đổi (`Files changed`), phát hiện sớm tệp rác hoặc sai sót trước khi gộp.
- **Truy vết thay đổi (Traceability):** Lưu lại ngữ cảnh (Mục đích, Thay đổi, Cách kiểm thử) như một Change Request chính thức trong quy trình SCM.
