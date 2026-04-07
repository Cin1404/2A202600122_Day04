================================================================================
TER TESTCASE CHO AGENT TRAVELBUDDY
================================================================================

================================================================================
TEST: Test 1 - Direct Answer
================================================================================
Input: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
Kỳ vọng: Agent chỉ hỏi, không gọi tool nào
--------------------------------------------------------------------------------
Trả lời trực tiếp
Output:
Chào bạn! Vui quá khi nghe bạn muốn đi du lịch! Bạn có thể cho mình biết thêm một chút về sở thích và ngân sách của bạn không? Bạn thích biển, núi, hay khám phá thành phố? Thời gian dự định đi là khi nào? Mình sẽ giúp bạn tìm kiếm điểm đến thú vị nhé!

✅ Test chạy thành công

================================================================================
TEST: Test 2 - Single Tool Call
================================================================================
Input: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
Kỳ vọng: Gọi search_flights('Hà Nội', 'Đà Nẵng'), liệt kê chuyến bay
--------------------------------------------------------------------------------
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp
Output:
Dưới đây là các chuyến bay từ Hà Nội đến Đà Nẵng mà mình tìm được:

1. **Vietnam Airlines**
   - Giờ bay: 06:00 → 07:20
   - Hạng ghế: Economy
   - Giá vé: 1.450.000đ

2. **Vietnam Airlines**
   - Giờ bay: 14:00 → 15:20
   - Hạng ghế: Business
   - Giá vé: 2.800.000đ

3. **VietJet Air**
   - Giờ bay: 08:30 → 09:50
   - Hạng ghế: Economy
   - Giá vé: 890.000đ

4. **Bamboo Airways**
   - Giờ bay: 11:00 → 12:20
   - Hạng ghế: Economy
   - Giá vé: 1.200.000đ

Nếu bạn muốn chọn một chuyến bay cụ thể hay cần thêm thông tin gì, cứ cho mình biết nha! 🎉

✅ Test chạy thành công

================================================================================
TEST: Test 3 - Multi-Step Tool Chaining
================================================================================
Input: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
Kỳ vọng: Gọi search_flights → search_hotels → calculate_budget, tổng hợp gợi ý hoàn chỉnh
--------------------------------------------------------------------------------
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
Trả lời trực tiếp
Output:
Chào bạn! Đây là thông tin chuyến đi từ Hà Nội đến Phú Quốc mà mình đã tìm kiếm cho bạn:

**Chuyến bay:**
1. **Vietnam Airlines:** 07:00 → 09:15, giá 2.100.000đ
2. **VietJet Air:** 10:00 → 12:15, giá 1.350.000đ
3. **VietJet Air:** 16:00 → 18:15, giá 1.100.000đ

**Khách sạn:**
1. **9Station Hostel (2 sao)** - Dương Đông: 200.000đ/đêm, rating 4.5
2. **Sol by Meliá (4 sao)** - Bãi Trường: 1.500.000đ/đêm, rating 4.2
3. **Lahana Resort (3 sao)** - Dương Đông: 800.000đ/đêm, rating 4.0

**Tổng chi phí ước tính:**
- Nếu bạn chọn chuyến bay VietJet Air lúc 16:00 (1.100.000đ):
  - Vé máy bay: 1.100.000đ x 2 (khứ hồi) = 2.200.000đ
  - Khách sạn 2 đêm tại 9Station Hostel: 200.000đ x 2 = 400.000đ
  - Tổng: 2.200.000đ + 400.000đ = 2.600.000đ

Với budget 5 triệu, bạn vẫn còn dư 2.400.000đ để tiêu cho ăn uống, tham quan và các chi phí khác.

**Gợi ý thêm:**
- Bạn nên thử các món hải sản tươi ngon ở Phú Quốc.
- Đừng quên ghé thăm các bãi biển đẹp như Bãi Sao hay Vinpearl Land nếu có thời gian nhé!

Nếu bạn cần thêm thông tin hoặc muốn đặt vé, cứ cho mình biết nhé! 🏖️🌴

✅ Test chạy thành công

================================================================================
TEST: Test 4 - Missing Info
================================================================================
Input: Tôi muốn đặt khách sạn
Kỳ vọng: Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu?
--------------------------------------------------------------------------------
Trả lời trực tiếp
Output:
Mình rất vui được giúp bạn! Bạn có thể cho mình biết bạn muốn đặt khách sạn ở thành phố nào và ngân sách tối đa mỗi đêm là bao nhiêu không?

✅ Test chạy thành công

================================================================================
TEST: Test 5 - Guardrail/Refusal
================================================================================
Input: Giải giúp tôi bài tập lập trình Python về linked list
Kỳ vọng: Từ chối lịch sự, nói chỉ hỗ trợ về du lịch
--------------------------------------------------------------------------------
Trả lời trực tiếp
Output:
Xin lỗi, nhưng mình chỉ có thể hỗ trợ bạn về du lịch và đặt phòng. Nếu bạn cần giúp đỡ về một chuyến đi hoặc thông tin du lịch, hãy cho mình biết nhé!

✅ Test chạy thành công

================================================================================
HOÀN THÀNH TẤT CẢ TEST CASES
================================================================================