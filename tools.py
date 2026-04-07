from langchain_core.tools import tool

# ============================================================
# MOCK DATA — Dữ liệu giả lập hệ thống du lịch
# Lưu ý: Giá cả có logic (VD: cuối tuần đắt hơn, hạng cao hơn đắt hơn)
# Sinh viên cần đọc hiểu data để debug test cases.
# ============================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy tuyến bay, trả về thông báo không có chuyến.
    """
    def fmt_price(value: int) -> str:
        return f"{value:,}".replace(",", ".") + "đ"

    flights = FLIGHTS_DB.get((origin, destination))
    if flights:
        lines = [f"Chuyến bay từ {origin} đến {destination}: "]
        for item in flights:
            lines.append(
                f"- {item['airline']}, {item['departure']} → {item['arrival']}, {item['class']}, {fmt_price(item['price'])}"
            )
        return "\n".join(lines)

    reverse_flights = FLIGHTS_DB.get((destination, origin))
    if reverse_flights:
        lines = [
            f"Không tìm thấy chuyến bay từ {origin} đến {destination}.",
            f"Tuy nhiên có chuyến bay từ {destination} đến {origin}:"
        ]
        for item in reverse_flights:
            lines.append(
                f"- {item['airline']}, {item['departure']} → {item['arrival']}, {item['class']}, {fmt_price(item['price'])}"
            )
        return "\n".join(lines)

    return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.

    Tham số:
    - city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: giá tối đa mỗi đêm (VND), mặc định không giới hạn

    Trả về danh sách khách sạn phù hợp với tên, số sao, giá, khu vực, rating.
    """
    def fmt_price(value: int) -> str:
        return f"{value:,}".replace(",", ".") + "đ"

    hotels = HOTELS_DB.get(city)
    if not hotels:
        return f"Không tìm thấy khách sạn tại {city}."

    filtered = [hotel for hotel in hotels if hotel["price_per_night"] <= max_price_per_night]
    if not filtered:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {fmt_price(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."

    filtered.sort(key=lambda item: (-item["rating"], item["price_per_night"]))
    lines = [f"Khách sạn tại {city}, tối đa {fmt_price(max_price_per_night)}/đêm:"]
    for hotel in filtered:
        lines.append(
            f"- {hotel['name']} ({hotel['stars']} sao, {hotel['area']}), {fmt_price(hotel['price_per_night'])}/đêm, rating {hotel['rating']}"
        )
    return "\n".join(lines)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.

    Tham số:
    - total_budget: tổng ngân sách ban đầu (VND)
    - expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy,
      định dạng 'tên_khoản:số_tiền' (VD: 'vé_máy_bay:890000,khách_sạn:650000')

    Trả về bảng chi tiết các khoản chi và số tiền còn lại.
    Nếu vượt ngân sách, cảnh báo rõ ràng số tiền thiếu.
    """
    def fmt_price(value: int) -> str:
        return f"{value:,}".replace(",", ".") + "đ"

    if not expenses or not isinstance(expenses, str):
        return "Lỗi: tham số expenses không hợp lệ. Vui lòng nhập chuỗi định dạng 'tên_khoản:số_tiền'."

    items = [part.strip() for part in expenses.split(",") if part.strip()]
    if not items:
        return "Lỗi: không có khoản chi nào được cung cấp. Vui lòng nhập dạng 'tên_khoản:số_tiền'."

    parsed = {}
    total_cost = 0
    for part in items:
        if ":" not in part:
            return f"Lỗi định dạng: '{part}'. Mỗi khoản phải có dạng 'tên:số_tiền'."
        name, value = part.split(":", 1)
        name = name.strip()
        value = value.strip().replace(".", "").replace(",", "")
        if not name or not value.isdigit():
            return f"Lỗi định dạng: '{part}'. Vui lòng dùng tên và số tiền nguyên dương."
        cost = int(value)
        parsed[name] = cost
        total_cost += cost

    remaining = total_budget - total_cost
    lines = ["Bảng chi phí:"]
    for name, cost in parsed.items():
        lines.append(f"- {name}: {fmt_price(cost)}")
    lines.append("---")
    lines.append(f"Tổng chi: {fmt_price(total_cost)}")
    lines.append(f"Ngân sách: {fmt_price(total_budget)}")
    lines.append(f"Còn lại: {fmt_price(remaining if remaining >= 0 else abs(remaining))}")

    if remaining < 0:
        lines.append(f"Vượt ngân sách {fmt_price(abs(remaining))}! Cần điều chỉnh.")
    return "\n".join(lines)

# --- KẾT THÚC CODE tools.py ---

# Chú ý:
# - search_flights: phải xử lý tuple key, thử tra ngược chiều
# - search_hotels: phải lọc + sắp xếp, không chỉ lookup
# - calculate_budget: phải parse chuỗi, xử lý format lỗi, tính toán thực sự
# - 3 tools có MỐI LIÊN HỆ: kết quả flights -> input cho budget -> quyết định hotels
