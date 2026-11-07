# Câu hỏi thảo luận Lab 02
1. Phải đồng bộ master trước khi PR để giải quyết conflict tại máy cá nhân, kiểm thử tích hợp sớm và đảm bảo code duyệt trên PR đúng là code chạy thực tế.
2. Không bao giờ rebase các nhánh công khai đã chia sẻ (`master`, `release/*`) vì rebase viết lại lịch sử commit (thay đổi mã SHA), gây lệch pha dữ liệu của nhóm.
3. `feature/*` dùng cho tính năng phần mềm; `topic/*` dùng cho tài liệu, cấu hình, template hoặc CI.
