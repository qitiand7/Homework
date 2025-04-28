import hashlib
import time


def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def find_hash_with_prefix(prefix, nickname):
    t = time.time()
    while True:
        nonce = time.time() * 1000000
        data = f"{nickname}{int(nonce)}"
        hash_value = calculate_hash(data)
        if hash_value.startswith(prefix):
            return data, hash_value, time.time() - t


def main():
    nickname = "QI"
    prefix4 = "0000"

    data4, hash4, time4 = find_hash_with_prefix(prefix4, nickname)
    print(f"满足 4 个 0 开头的哈希值:")
    print(f"Data: {data4}")
    print(f"Hash: {hash4}")
    print(f"Time: {time4:.4f} 秒")

    prefix5 = "00000"
    data5, hash5, time5 = find_hash_with_prefix(prefix5, nickname)
    print(f"\n满足 5 个 0 开头的哈希值:")
    print(f"Data: {data5}")
    print(f"Hash: {hash5}")
    print(f"Time: {time5:.4f} 秒")


if __name__ == "__main__":
    main()
