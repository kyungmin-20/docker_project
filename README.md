# FastAPI Docker EC2 배포 과제

FastAPI 기반 수강기록 API 를 Docker 컨테이너로 빌드하여 AWS Learner Lab EC2 환경에 배포한 과제 저장소입니다.

## 데모 영상

▶️ **영상 링크**: <https://youtu.be/JNeMC0PTdYs>

포함 내용: EC2 SSH 접속 / `docker ps` 결과 / `docker inspect ... RestartPolicy` 확인 / 브라우저에서 `http://<EC2 IP>/courses` JSON / `/docs` Swagger UI + Try it out 응답.

## 프로젝트 구조

```
.
├── main.py              # FastAPI 진입점
├── courses.py           # /courses GET, POST 라우터
├── model.py             # Course Pydantic 모델
├── courses.json         # 데이터 파일
├── requirements.txt     # fastapi, uvicorn[standard]
├── Dockerfile           # 컨테이너 이미지 빌드 정의
├── docker-compose.yml   # 컨테이너 실행 정의 (80:8000, restart: always)
├── .dockerignore
└── .gitignore
```

## API

| Method | Path      | 설명 |
| ------ | --------- | --- |
| GET    | `/`       | 헬스 체크 |
| GET    | `/courses`| 수강 과목 목록 조회 |
| POST   | `/courses`| 수강 과목 추가 |

Swagger UI: `/docs`

## 실행 방법 (로컬)

```bash
docker compose up -d --build
```

- 브라우저: <http://localhost/courses> 또는 <http://localhost/docs>
- 중지: `docker compose down`

## EC2 배포 절차 (AWS Learner Lab)

1. EC2 인스턴스 시작 (Amazon Linux 2023 또는 Ubuntu).
2. 보안그룹 인바운드: TCP **80** (0.0.0.0/0), TCP 22 (내 IP).
3. SSH 접속 후 Docker 설치:
   ```bash
   sudo dnf install -y docker docker-compose-plugin git
   sudo systemctl enable --now docker
   sudo usermod -aG docker ec2-user
   exit   # 재접속하여 그룹 반영
   ```
4. 코드 가져와서 빌드 & 실행:
   ```bash
   git clone https://github.com/kyungmin-20/docker_project.git
   cd docker_project
   sudo docker compose up -d --build
   sudo docker ps
   ```
5. 브라우저에서 접속: `http://<EC2 퍼블릭 IP>/courses`

## 포트 / 재시작 정책

- 외부 포트: **80** → 내부(FastAPI): **8000**
- `restart: always` 적용 — EC2 재부팅 후에도 컨테이너 자동 기동.

## 평가 기준 매핑

| 기준 | 처리 |
| --- | --- |
| Dockerfile 작성 | `Dockerfile` 포함 |
| Docker 실행 | `docker compose up -d --build` |
| 외부 80 포트 | `ports: "80:8000"` |
| restart: always | compose 설정 |
| EC2 배포 | 위 절차 |
| 데모 영상 | 상단 영상 링크 |
