from flask import Flask

app = Flask(__name__)

# 기본 경로('/')에 간단한 응답을 추가합니다.
@app.route('/')
def hello():
    return 'TEST PIPELINE'

# Health Check를 위한 엔드포인트('/health')를 추가합니다.
@app.route('/health')
def health():
    return 'OK', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

