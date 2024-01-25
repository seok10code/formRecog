conda install conda-forge::azure-storage-blob
---
conda install microsoft::azure-ai-formrecognizer
---
conda install conda-forge::azure-core
---


azure AI service를 사용해 index를 생성한 후 그 index를 기반으로 chatGPT의 답변을 리턴하기 위해 PDF 파일을 텍스트화 시키는 작업

그때 Form Recognizer를 사용해 텍스트를 추출


FORM_RECOGNIZER_KEY - 키
FORM_RECOGNIZER_ENDPOINT - 폼레커 엔드포인트
STORAGE_CONSTR - 커넥스트링
SOURCE_NAME - 컨테이너 이름
FILE_NAME - 파일 이름



*******************************
블롭스토리지 권한을 설정-구성-
스토리지 계정 키 액세스 허용 해주고
스토리지를 퍼블릭으로 바꿔주기
******************************
ID-시스템 할당 항목 켜
