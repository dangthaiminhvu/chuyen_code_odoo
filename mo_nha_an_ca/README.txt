# Quản lý nhà ăn ca

## Mô tả
Module này hỗ trợ quản lý quá trình ăn ca tại nhà ăn, bao gồm:
1. Quẹt thẻ để vào nhà ăn.
2. Quản lý thông tin ăn ca.
3. Bấm nút mở cửa để ra khỏi nhà ăn.

## Các bước thực hiện
1. **Nhận diện - Quẹt thẻ (Vào nhà ăn)**:
   - CBCNV quẹt thẻ, hệ thống kiểm tra thông tin ăn ca.
   - Nếu hợp lệ, cửa sẽ tự động mở.
   - Nếu không hợp lệ, cửa sẽ không mở.

2. **Ăn ca**:
   - CBCNV thực hiện ăn ca tại vị trí đã đăng ký.

3. **Bấm nút mở cửa (Ra nhà ăn)**:
   - Sau khi ăn ca xong, CBCNV bấm nút để mở cửa ra khỏi nhà ăn.

## Phân quyền
- Người dùng thuộc nhóm `base.group_user` có quyền truy cập đầy đủ vào các chức năng của module.