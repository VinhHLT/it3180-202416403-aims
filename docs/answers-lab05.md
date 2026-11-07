# Câu hỏi thảo luận Lab 05

## 1. Ưu, nhược điểm của "Upstream-first" so với "Release-first" khi xử lý Hotfix?
- **Release-first (Sửa trên `release/*` trước -> cherry-pick về `master`):**
  - *Ưu điểm:* Vá lỗi nhanh và an toàn nhất cho bản đang chạy thực tế (`v1.0.0` -> `v1.0.1`) vì môi trường code cô lập, không bị ảnh hưởng bởi các tính năng mới chưa ổn định trên `master`.
  - *Nhược điểm:* Có nguy cơ quên lan truyền bản sửa về `master` hoặc các nhánh `release` mới hơn, gây lỗi lặp lại (regression) ở phiên bản sau.
- **Upstream-first (Sửa trên `master` trước -> cherry-pick lùi về `release/*`):**
  - *Ưu điểm:* Đảm bảo nhánh chính `master` luôn có bản sửa lỗi đầu tiên, không bao giờ bị sót lỗi ở các bản phát hành tương lai.
  - *Nhược điểm:* Tốn thời gian hơn khi cần phát hành gấp bản vá cho khách hàng, và đôi khi code trên `master` đã thay đổi cấu trúc khiến việc backport về nhánh `release` cũ phức tạp hơn.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- **Lệnh tra cứu log cherry-pick:** `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` sẽ chỉ hiện 1 commit (trên `master`) thay vì 2 commit.
- **Lệnh kiểm toán commit tương đương:** `git cherry -v origin/release/lab05 origin/release/lab04` sẽ hiển thị dấu `+` trước commit `fix: make search_by_title case-insensitive`, báo hiệu commit này chưa được đưa sang `release/lab05`.
- **Vòng lặp kiểm thử thực thi:** Khi chạy script kiểm tra `search_by_title` với từ khóa chữ thường `'lion'` qua 3 mốc `v1.0.1`, `v1.1.0`, `master`, kết quả ở `v1.1.0` sẽ trả về `0` thay vì `1`.
