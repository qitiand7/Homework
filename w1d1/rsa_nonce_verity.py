from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


# 生成密钥对
def generate_rsa_keys(key_size=2048):
    """
    生成RSA公私钥对
    :return: 私钥和公钥对象
    """
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key


# 私钥签名
def sign_message(private_key, message):
    """
    使用私钥对消息进行签名
    :param private_key: 私钥对象
    :param message: 要签名的消息(字节类型)
    :return: 签名数据
    """
    # 计算消息的哈希值
    digest = SHA256.new(message)
    # 使用PKCS#1 v1.5签名方案
    signature = pkcs1_15.new(private_key).sign(digest)
    return signature


# 公钥验签
def verify_signature(public_key, message, signature):
    """
    使用公钥验证签名
    :param public_key: 公钥对象
    :param message: 原始消息(字节类型)
    :param signature: 签名数据
    :return: True/False
    """
    digest = SHA256.new(message)
    try:
        pkcs1_15.new(public_key).verify(digest, signature)
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    # 1. 生成密钥对
    private_key, public_key = generate_rsa_keys()
    print(private_key, public_key)

    # Data: QI1745832226456458
    # Hash: 00007deb0fec153fc931b905fc31f6407ab007af40ee6131d99126910818bd22
    message = "00007deb0fec153fc931b905fc31f6407ab007af40ee6131d99126910818bd22".encode()

    # 2. 生成签名
    signature = sign_message(private_key, message)
    print(f"Signature: {signature.hex()}")

    # 3. 验证签名(正常情况)
    print("Verification:", verify_signature(public_key, message, signature))  # 应该返回True

    # 4. 验证签名(篡改消息)
    tampered_message = b"Tampered message to sign"
    print("Verification (tampered):", verify_signature(public_key, tampered_message, signature))  # 应该返回False
