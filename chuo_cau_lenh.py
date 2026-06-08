import pandas as pd

# 1. Tạo thử dữ liệu khách hàng ngay trong code để chạy mà không cần file Excel thật
data = {
    'Ten': ['Tanaka', 'Sato', 'Suzuki', 'Nguyen'],
    'Dia_chi': ['Tokyo', 'Osaka', 'Tokyo', 'Saitama'],
    'Doanh_thu': [600000, 300000, 450000, 700000]
}
df = pd.DataFrame(data)

# 2. Lọc khách hàng ở Tokyo VÀ doanh thu trên 50 vạn
# (Dấu & nghĩa là VÀ, hai điều kiện phải xảy ra cùng lúc)
ket_qua = df[(df['Dia_chi'] == 'Tokyo') & (df['Doanh_thu'] > 500000)]

# 3. In kết quả ra màn hình để xem
print(ket_qua)
