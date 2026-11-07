# Câu hỏi thảo luận Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **`--global`**: Lưu tại `~/.gitconfig` trong thư mục người dùng, áp dụng cho mọi repository của user trên máy.
- **`--local`**: Lưu tại `.git/config` của riêng repository hiện tại, chỉ áp dụng cho repo đó và ghi đè lên cấu hình `--global`.

## 2. Vì sao dùng `git mv`?
- Giúp Git ghi nhận thao tác di chuyển/đổi tên tệp (`renamed`) ngay trong vùng Staging, giữ nguyên lịch sử thay đổi của tệp khi truy vết bằng `git log --follow`.

## 3. `release/lab01` có phải baseline không?
- Có. `release/lab01` là một Baseline đánh dấu mốc hoàn thành của Lab 01 để nộp bài, không nhận các commit phát triển tính năng thông thường.

## 4. Vì sao không commit thẳng lên `master` dù làm một mình?
- Đảm bảo nhánh `master` luôn ổn định, cô lập các thử nghiệm/tái cấu trúc trên nhánh riêng, giúp tự rà soát lại thay đổi qua Pull Request và tuân thủ nhất quán quy trình SCM.
