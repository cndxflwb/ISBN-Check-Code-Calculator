original_input = input("请输入要计算的12位ISBN: ").strip()

# 提取输入中的所有数字字符
digits = [c for c in original_input if c.isdigit()]
digits_str = ''.join(digits)

# 验证是否为12位数字
if len(digits_str) != 12:
    print("输入错误：必须提供12位数字")
else:
    # 计算加权和
    total = 0
    for i in range(12):
        num = int(digits_str[i])
        # 判断奇数位（位置1、3、5...）
        if (i + 1) % 2 == 1:
            total += num * 1
        else:
            total += num * 3
    
    # 计算校验码
    remainder = total % 10
    check_digit = (10 - remainder) % 10
    
    # 处理原始输入格式
    if any(not c.isdigit() for c in original_input):
        # 找到最后一个数字的位置
        last_digit_pos = -1
        for i in range(len(original_input)-1, -1, -1):
            if original_input[i].isdigit():
                last_digit_pos = i
                break
        # 截取到最后一个数字并添加校验码
        trimmed = original_input[:last_digit_pos+1]
        full_isbn = f"{trimmed}-{check_digit}"
    else:
        full_isbn = f"{original_input}{check_digit}"
    
    print(f"完整的ISBN为：{full_isbn}")