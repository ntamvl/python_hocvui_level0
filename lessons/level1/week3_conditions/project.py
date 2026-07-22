# Dự án Tuần 3: Gương thần dự báo thời tiết
# Thử đổi thoi_tiet thành "mưa", "tuyết", hoặc "nắng" rồi chạy nhé!

thoi_tiet = "nắng"

print("🔮 Gương thần đang xem thời tiết...")

if thoi_tiet == "nắng":
    print("Trời nắng chang chang! Nhớ bôi kem chống nắng và đội mũ khi ra ngoài nhé! ☀️")
elif thoi_tiet == "mưa":
    print("Trời đang mưa lâm thâm! Nhớ mang theo ô (dù) và áo mưa kẻo cảm lạnh nha! 🌧️")
elif thoi_tiet == "tuyết":
    print("Ôi! Tuyết rơi rơi! Hãy mặc áo khoác thật dày và đi ủng ấm áp để nghịch tuyết nào! ❄️")
else:
    print("Thời tiết lạ lùng quá! Gương thần khuyên bạn cứ ở nhà chơi game cho lành! 🎮")
