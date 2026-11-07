# Câu hỏi thảo luận Lab 01
1. Cấu hình `--global` lưu tại `~/.gitconfig` áp dụng toàn hệ thống user; `--local` lưu tại `.git/config` của repo hiện tại và có độ ưu tiên cao hơn.
2. Dùng `git mv` giúp Git ghi nhận thao tác đổi tên (`renamed`) thay vì xóa và thêm mới, bảo toàn lịch sử tệp qua `git log --follow`.
3. `release/lab01` là baseline vì là phiên bản đóng băng tại mốc nộp bài, chỉ sửa qua quy trình chính thức.
4. Không commit thẳng lên master để cô lập rủi ro, tự rà soát code qua PR và lưu vết thay đổi (Change Request).
