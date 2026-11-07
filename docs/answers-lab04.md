# Câu hỏi thảo luận Lab 04

## 1. Vì sao `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.
- **Lý do không merge ngược `release/*` vào `master`:**
  - Mọi bước chuẩn bị phát hành (nâng version, viết CHANGELOG) đã được thực hiện trên `master` trước khi tách nhánh `release/*`.
  - Sau khi tách `release/lab04` (dòng `1.0.x`), `master` tiếp tục tiến lên `1.1.0`. Nếu merge nhánh `release/lab04` (chứa commit bump `1.0.1`) vào `master` sẽ gây xung đột số phiên bản và CHANGELOG. Do đó, chỉ mã sửa lỗi thuần túy mới được đưa về `master` qua `git cherry-pick -x`.
- **So sánh với GitFlow:**
  - **GitFlow:** Có 2 nhánh chính (`main` và `develop`), nhánh `release/*` chỉ sống ngắn hạn để chuẩn bị phát hành rồi merge vào cả `main` lẫn `develop` và xóa đi.
  - **Release Flow (học phần):** Chỉ có 1 nhánh tích hợp là `master`, còn các nhánh `release/labXX` là nhánh bảo trì dài hạn tồn tại song song để phục vụ bảo trì đa phiên bản độc lập.

## 2. Vì sao đánh số phiên bản lên `1.0.0` mà không phải `0.4.0`?
- Theo chuẩn **Semantic Versioning (SemVer)**:
  - Dải `0.y.z` (`v0.1.0`..`v0.3.0` ở Lab 01–03) dùng cho giai đoạn phát triển ban đầu khi cấu trúc mã nguồn và giao diện hàm chưa ổn định.
  - Phiên bản `1.0.0` đánh dấu cột mốc bản phát hành chính thức đầu tiên (First Stable Public Release) có đầy đủ chức năng cơ bản, cấu trúc package hoàn chỉnh, có unit test và CHANGELOG rõ ràng.
