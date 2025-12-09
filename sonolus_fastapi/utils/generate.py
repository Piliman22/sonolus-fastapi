import random, string

def generate_random_string(length: int) -> str:
    """
    指定された長さのランダムな文字列を生成します。
    Args:
        length (int): 生成する文字列の長さ
    Returns:
        str: 生成されたランダムな文字列
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))