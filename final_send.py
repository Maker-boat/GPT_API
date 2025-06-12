import requests

def main():
    # 設定伺服器 IP 或網域（本機測試時用 localhost）
    server_url = "https://e55a-1-34-27-124.ngrok-free.app/chat"  # ✅ 改成你部署的 GPT 電腦 IP，例如 http://192.168.1.100:5000/chat

    while True:
        prompt = input("請輸入你想問 ChatGPT 的內容（輸入 q 離開）：\n> ")
        if prompt.lower() == "q":
            break

        try:
            res = requests.post(server_url, data={"prompt": prompt})
            res.raise_for_status()  # 若有錯會觸發例外
            data = res.json()

            if "reply" in data:
                print("\n💬 ChatGPT 回應：\n" + data["reply"])
            else:
                print("\n⚠️ 發生錯誤：", data.get("error", "未知錯誤"))

        except requests.exceptions.RequestException as e:
            print("\n❌ 無法連線伺服器或請求失敗：", str(e))

if __name__ == "__main__":
    main()