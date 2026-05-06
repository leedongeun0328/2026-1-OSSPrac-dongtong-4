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
        "role_details": [
            {
                "icon": "bi bi-server",
                "title": "프로젝트 소개 구현",
                "description": "팀 소개 웹사이트의 목적과 개발 배경을 설명하는 프로젝트 소개 영역을 구성했습니다."
            },
            {
                "icon": "bi bi-database",
                "title": "역할·기술·협업 내용 정리",
                "description": "역할 분담, 기술 스택, 오픈소스 협업 과정을 카드 형태로 정리했습니다."
            },
            {
                "icon": "bi bi-diagram-3",
                "title": "웹 애플리케이션 구조 시각화",
                "description": "User, Browser, Flask, Templates/Static, Bootstrap 흐름을 보여주는 구조 다이어그램을 구현했습니다."
            }
        ],
        "skills": [
            {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
            {"name": "Flask", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
            {"name": "GitHub", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"}
        ],
        "contribution": "서버 라우팅, Flask 프로젝트 구조 설계, 데이터 처리 로직, 백엔드 기능 구현",
        "phone": "010-3007-1852",
        "self_intro": "안녕하세요. 저는 ENTP 개발자입니다.",
        "portfolio": "https://github.com/SoyoonJee",
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
        "role_details": [
            {
                "icon": "bi bi-server",
                "title": "메인 소개 화면 구현",
                "description": "웹사이트 첫 화면에 팀명, 프로젝트 소개 문구, 이동 버튼이 보이도록 메인 소개 영역을 구성했습니다."
            },
            {
                "icon": "bi bi-database",
                "title": "팀원 소개 카드 구현",
                "description": "각 팀원의 역할, 기술 스택, 프로젝트 기여도, 연락처, 자기소개가 카드 형태로 출력되도록 구현했습니다."
            },
            {
                "icon": "bi bi-diagram-3",
                "title": "반응형 화면 구성",
                "description": "Bootstrap을 활용하여 다양한 화면 크기에서도 팀원 소개 페이지가 보기 좋게 보이도록 구성했습니다."
            }
        ],
        "skills": [
            {"name": "HTML5", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
            {"name": "JavaScript", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
            {"name": "Bootstrap", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg"},
            {"name": "GitHub", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"}
        ],
        "contribution": "메인 화면 UI 설계, 팀원 카드 디자인, 반응형 레이아웃, Bootstrap 스타일 적용",
        "phone": "010-9315-7148",
        "self_intro": "안녕하세요. 저는 ISTP 개발자입니다.",
        "portfolio": "https://github.com/leedongeun0328",
        "email": "idongeun52@gmail.com",
        "image": "/static/images/lee.jpg",
        "department": "통계학과"
    },
    {
        "id": 3,
        "name": "조수아",
        "role": "Backend Developer/Flask·기능 구현 담당",
        "intro": "Flask를 활용하여 페이지 라우팅 구조를 설계하고, 개발과정 섹션 및 팀원별 상세 페이지 기능을 구현했습니다.",
        "detail_intro": (
            "조수아 팀원은 Flask를 기반으로 웹 애플리케이션의 페이지 구조를 설계하고, "
            "개발과정 섹션과 팀원 상세 페이지 기능을 구현했습니다. "
            "특히 role_details 데이터를 활용하여 팀원별 담당 역할이 동적으로 출력되도록 구성하였으며, "
            "사용자가 쉽게 정보를 확인할 수 있도록 페이지 흐름과 UI 연결을 개선하였습니다."
        ),
        "role_details": [
            {
                "icon": "bi bi-server",
                "title": "개발과정 navbar 추가",
                "description": "base.html의 navbar에 개발과정 메뉴를 추가하고, 클릭 시 해당 섹션으로 이동하도록 연결했습니다."
            },
            {
                "icon": "bi bi-database",
                "title": "개발과정 섹션 구현",
                "description": "index.html에 id='process' 섹션을 추가하고, 프로젝트 진행 흐름과 협업 방식을 정리했습니다."
            },
            {
                "icon": "bi bi-diagram-3",
                "title": "담당 역할 상세 분리",
                "description": "app.py에 role_details 데이터를 추가하고, member_detail.html에서 팀원별 담당 역할이 다르게 출력되도록 수정했습니다."
            }
        ],
        "skills": [
            {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
            {"name": "Flask", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
            {"name": "HTML5", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
            {"name": "Bootstrap", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg"},
            {"name": "GitHub", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"}
        ],
        "contribution": "개발과정 섹션 구현, navbar 연결, 팀원 상세 페이지 구조 설계, role_details 기반 동적 데이터 출력 기능 구현",
        "phone": "010-5160-4212",
        "self_intro": "안녕하세요. 저는 ENTJ 개발자입니다.",
        "portfolio": "https://github.com/choosooa",
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

@app.route("/input")
def input_page():
    return render_template("input.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/result")
def result():
    return render_template("result.html")