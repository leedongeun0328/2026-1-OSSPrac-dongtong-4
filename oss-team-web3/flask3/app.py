from flask import Flask, render_template, abort

app = Flask(__name__)

team_members = [
    {
        "id": 1,

        "name": "지소윤",
        "role": "Backend Developer / Flask 담당",
        "intro": "Flask 기반 서버 구조와 API 설계를 담당하는 백엔드 개발자입니다.",
        "detail_intro": (
            "지소윤 팀원은 Python과 Flask를 기반으로 웹 애플리케이션의 서버 구조를 설계하고, "
            "사용자 요청을 처리하는 라우팅과 데이터 처리 로직을 담당합니다. 유지보수가 쉬운 코드 구조와 "
            "명확한 API 설계를 중요하게 생각합니다."
        ),
        "skills": [
            {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
            {"name": "Flask", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
            {"name": "GitHub", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"}
        ],
        "contribution": "서버 라우팅, Flask 프로젝트 구조 설계, 데이터 처리 로직, 백엔드 기능 구현",
        "phone": "010-3007-1852",
        "self_intro": "안녕하세요. 저는 ENTP 개발자입니다.",
        "portfolio": "https://github.com/minsu",
        "email": "ddaeng0321@gmail.com",
        "image": "/static/images/yoon.jpg",
        "department": "통계학과"
        
    },
    {
        "id": 2,
        "name": "이동은",
        "role": "Frontend Developer / HTML·CSS 담당",
        "intro": "사용자 친화적인 인터페이스와 반응형 웹 디자인을 담당합니다.",
        "detail_intro": (
            "이동은 팀원은 HTML, CSS, Bootstrap을 활용하여 사용자가 보기 쉽고 친근하게 느낄 수 있는 "
            "화면을 구성합니다. 카드형 레이아웃, 반응형 디자인, 색상 조합, 사용자 경험 개선을 담당합니다."
        ),
        "skills": [
            {"name": "HTML5", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
            {"name": "JavaScript", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
            {"name": "Bootstrap", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg"}
        ],
        "contribution": "메인 화면 UI 설계, 팀원 카드 디자인, 반응형 레이아웃, Bootstrap 스타일 적용",
        "phone": "010-9315-7148",
        "self_intro": "안녕하세요. 저는 ISTP 개발자입니다.",
        "portfolio": "https://github.com/jihyun",
        "email": "idongeun52@gmail.com",
        "image": "/static/images/lee.jpg",
        "department": "통계학과"
    },
    {
        "id": 3,
        "name": "조수아",
        "role": "DevOps / Nginx·배포 담당",
        "intro": "Nginx와 Linux 서버 환경을 구성하고 안정적인 배포를 담당합니다.",
        "detail_intro": (
            "조수아 팀원은 Nginx, Gunicorn, Linux 기반 운영 환경을 구성합니다. Flask 애플리케이션이 "
            "운영 서버에서 안정적으로 동작할 수 있도록 리버스 프록시, 정적 파일 처리, 배포 환경을 관리합니다."
        ),
        "skills": [
            {"name": "Linux", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"},
            {"name": "Nginx", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg"},
            {"name": "Docker", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"},
        ],
        "contribution": "Nginx 설정, Gunicorn 연동, Linux 배포 환경 구성, 운영 안정성 관리",
        "phone": "010-5160-4212",
        "self_intro": "안녕하세요. 저는 ENTJ 개발자입니다.",
        "portfolio": "https://github.com/doyoon",
        "email": "josuah0813@gmail.com",
        "image": "/static/images/cho.jpg",
        "department": "통계학과"
    }
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        team_members=team_members,
        active_page="home"
    )


@app.route("/members/<int:member_id>")
def member_detail(member_id):
    member = next((m for m in team_members if m["id"] == member_id), None)

    if member is None:
        abort(404)

    return render_template(
        "member_detail.html",
        member=member,
        active_page="members"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
