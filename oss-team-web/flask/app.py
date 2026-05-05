from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    team_members = [
        {
            "name": "김민수",
            "role": "Backend Developer / Flask 담당",
            "intro": "Flask 기반 서버 구조와 API 설계를 담당하는 백엔드 개발자입니다.",
            "skills": ["Python", "Flask", "REST API", "SQLite", "GitHub"],
            "contribution": "서버 라우팅, 데이터 처리 로직, Flask 프로젝트 구조 설계",
            "portfolio": "https://github.com/minsu",
            "email": "minsu@example.com",
            "image": "images/member1.jpg"
        },
        {
            "name": "이지현",
            "role": "Frontend Developer / HTML·CSS 담당",
            "intro": "사용자 친화적인 화면 구성과 반응형 웹 디자인을 담당합니다.",
            "skills": ["HTML", "CSS", "JavaScript", "Bootstrap", "Figma"],
            "contribution": "팀 소개 페이지 UI 설계, 카드 레이아웃, 반응형 디자인 구현",
            "portfolio": "https://github.com/jihyun",
            "email": "jihyun@example.com",
            "image": "images/member2.jpg"
        },
        {
            "name": "박도윤",
            "role": "DevOps / Nginx·배포 담당",
            "intro": "Nginx와 Linux 서버 환경을 구성하고 안정적인 배포를 담당합니다.",
            "skills": ["Linux", "Nginx", "Gunicorn", "Docker", "AWS"],
            "contribution": "Nginx 리버스 프록시 설정, 서버 배포, 운영 환경 구성",
            "portfolio": "https://github.com/doyoon",
            "email": "doyoon@example.com",
            "image": "images/member3.jpg"
        }
    ]

    return render_template("index.html", team_members=team_members)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
