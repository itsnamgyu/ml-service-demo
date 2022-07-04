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

1. 먼저 학습된 ML 모델 파일 (`model.pt`)를 최상단 폴더에 복사해주세요.
2. 아래 명령어를 실행하시면 로컬 및 외부에서 접근할 수 있는 Django 웹 서버가 8000번 포트에서 서빙됩니다.

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

명령어를 실행한 개발용 머신에서 접속하는 경우 주소창에 `localhost:8000`, 다른 서버 머신에서 명령어를 실행한 경우, `<서버 ip 주소 혹은 도메인>:8000`로 접속 가능합니다.

본 명령어는 개발 및 테스트용으로, production (상용) 환경에서 배포할 때에는 웹 서버 전용 소프트웨어 프로그램 (e.g., Apache, WSGI) 혹은 클라우드 서비스를 사용합니다.
 
 ----
# Docker
위의 파일을 Docker 상에서 실행할 수 있도록 하는 과정입니다.

_Linux 환경에서 실행하였으며, docker를 실행할 때 sudo를 사용하지 않도록 설정하였음._

해당 repository의 코드를 도커 상에서 사용하기 위해서 세 가지의 단계를 걸칩니다.

### 1. Dockerfile 작성

Docker 상에서 Django 서버를 가동하기 위해 필요한 절차들을 Dockerfile 작성하게 됩니다. 

### 2. Docker Build

"demo"라는 이름으로 Docker Image를 만들어줍니다. 

```bash
docker build . -t demo
```

현재 존재하는 docker image를 확인할 합니다.

```bash
docker images
```

### 3. Docker Container 실행

빌드한 이미지를 통해 Docker container를 생성합니다. 
Dockerfile에서 Docker container가 실행됨과 동시에 Django 데모 서버가 시작되도록 설정해두었습니다. 

```bash
docker run -it --name django_demo -p 8000:8000 demo0:0
```

컨테이너의 이름은 django_demo로 하였으며 아래 커맨드로 현재 존재하는 컨테이너들을 확인할 수 있습니다. 

```bash
docker ps -a
```
