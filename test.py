"""
File kiểm tra Agent TravelBuddy
Chạy 5 test cases để xác minh hoạt động của agent
"""

from agent import graph

def test_case(name: str, user_input: str, expected_behavior: str):
    """
    Chạy một test case duy nhất
    """
    print("\n" + "="*80)
    print(f"TEST: {name}")
    print("="*80)
    print(f"Input: {user_input}")
    print(f"Kỳ vọng: {expected_behavior}")
    print("-"*80)
    
    try:
        result = graph.invoke({"messages": [("human", user_input)]})
        final_message = result["messages"][-1]
        
        print(f"Output:\n{final_message.content}")
        print("\n✅ Test chạy thành công")
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")


def main():
    print("\n" + "="*80)
    print("TER TESTCASE CHO AGENT TRAVELBUDDY")
    print("="*80)
    
    # Test 1 — Direct Answer (Không cần tool)
    test_case(
        name="Test 1 - Direct Answer",
        user_input="Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
        expected_behavior="Agent chỉ hỏi, không gọi tool nào"
    )
    
    # Test 2 — Single Tool Call
    test_case(
        name="Test 2 - Single Tool Call",
        user_input="Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng",
        expected_behavior="Gọi search_flights('Hà Nội', 'Đà Nẵng'), liệt kê chuyến bay"
    )
    
    # Test 3 — Multi-Step Tool Chaining
    test_case(
        name="Test 3 - Multi-Step Tool Chaining",
        user_input="Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!",
        expected_behavior="Gọi search_flights → search_hotels → calculate_budget, tổng hợp gợi ý hoàn chỉnh"
    )
    
    # Test 4 — Missing Info / Clarification
    test_case(
        name="Test 4 - Missing Info",
        user_input="Tôi muốn đặt khách sạn",
        expected_behavior="Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu?"
    )
    
    # Test 5 — Guardrail / Refusal
    test_case(
        name="Test 5 - Guardrail/Refusal",
        user_input="Giải giúp tôi bài tập lập trình Python về linked list",
        expected_behavior="Từ chối lịch sự, nói chỉ hỗ trợ về du lịch"
    )
    
    print("\n" + "="*80)
    print("HOÀN THÀNH TẤT CẢ TEST CASES")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
