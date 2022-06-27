# ml-service-demo
ML 연동 웹 서비스 데모 (KR)

# Installation

### 1-1. Linux에서 Anaconda 설치

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
chmod 774 Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh  # 모두 yes
```

### 1-2. 기타 환경에서 Anaconda 설치

[Anaconda 공식 다운로드 페이지](https://www.anaconda.com/products/distribution#Downloads) 참고.

### 2. Anaconda 설치 확인

- 설치 후에는 터미널 혹은 ssh 연결을 껐다켜야 할수도 있습니다. 터미널 프롬프트 앞에 `(base)`가 뜨거나 `conda` 명령어가 동작하면 Anaconda가 정상적으로 설치된 것입니다.
- 여러 프로젝트를 개발하면서 패키지 버전 충돌을 예방하고자 하면 conda env 가상 환경 참고.

### 3. PyTorch 설치

```bash
 conda install pytorch torchvision -c pytorch
```

### 4. 기타 Python 패키지 설치

```bash
pip install -r requirements.txt  # 사용되는 패키지는 해당 txt 파일 참고! 
```

# Getting Started

아래 명령어를 실행하시면 로컬 및 외부에서 접근할 수 있는 Django 웹 서버가 8000번 포트에서 서빙됩니다.

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

명령어를 실행한 개발용 머신에서 접속하는 경우 주소창에 `localhost:8000`, 다른 서버 머신에서 명령어를 실행한 경우, `<서버 ip 주소 혹은 도메인>:8000`로 접속 가능합니다.

본 명령어는 개발 및 테스트용으로, production (상용) 환경에서 배포할 때에는 웹 서버 전용 소프트웨어 프로그램 (e.g., Apache, WSGI) 혹은 클라우드 서비스를 사용합니다.
