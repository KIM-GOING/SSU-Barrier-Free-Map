# __<div align='center'>SSU-Barrier-Free-Map</div>__

## __들어가며__

위 프로젝트는 2022년 2학기 숭실대학교 IT대학 전공과목 오픈소스기반기초설계 강의에서 진행한 프로젝트입니다.

## __주제 선정 및 선정 배경__

저희 프로젝트의 주제는 `Soongsil Barrier-Free Map` 입니다.

거동이 불편한 사람들은 이동 중 길을 찾아보는 것에 큰 불편함을 느낍니다. 그래서 이동 전, 본인이 가고자 하는 곳의 길을 미리 봐 두고 출발하는 경우가 많습니다. 저희 팀은 이 점에서 착안하여 교내 배리어 프리 시설 상황을 종합하여 제공하고자 합니다.

저희의 서비스는 숭실대학교 교내 배리어 프리 환경과 학교 근처 시설의 배리어 프리 현황이 등록된 웹 서비스 입니다. 교내 건물에서 벗어나 학교 주변에 있는 배리어 프리 현황을 제공하여 서비스의 사용성을 넓혔습니다.

누구나 쉽게 정보를 등록하고 나눌 수 있는 장을 마련하여, 전국민이 함께 만드는 배리어 프리 지도를 구축하는 것이 저희 팀 프로젝트의 최종 목표입니다.

---

## __사용자 메뉴얼__

### 제공 기능
- 숭실대학교 내 건물별 배리어 프리 정보 제공
- 숭실대학교 근처 부대시설 배리어 프리 정보 제공
- 자주가는 장소에 대한 즐겨찾기 등록
  
### 서비스 메인화면
![서비스 메인화면](https://user-images.githubusercontent.com/87303406/207527420-5a58d333-f7cc-47f5-af11-7f3fd646112e.png)
- 화면 중앙의 `건물별 보기`와 `내 주변 보기` 버튼을 통해 각각의 세부 페이지로 이동합니다.
- 화면 상단바는 모든 페이지에 고정적으로 있으며, 왼쪽 로고는 `서비스 메인페이지`, 즐겨찾는 장소는 `즐겨찾기 페이지`로 이동합니다.

### 건물별 보기 메인화면
![건물별보기 메인화면](https://user-images.githubusercontent.com/87303406/207536324-542794db-31fc-4708-952d-c0de3457d315.png)
- 좌측 네비게이션바와 화면 중앙 약도에 있는 건물을 클릭하여 해당 건물의 `배리어 프리 정보 상세페이지`로 이동합니다.
- `mouse hover` 이벤트를 적용하여 마우스의 위치에 맞게 네비게이션바와 약도의 건물명이 강조됩니다.

### 건물별 보기 세부화면
![건물별보기 세부화면](https://user-images.githubusercontent.com/87303406/207537822-e7c5f924-b465-47f7-863e-dc8f655d14af.png)
- 화면 중앙의 메인 컨텐츠 부분에서 스크롤을 내리며 해당 건물의 배리어 프리 정보를 확인합니다.
- 화면 좌측 네비게이션바에서 특정 건물을 클릭할 시, 해당 건물의 상세페이지로 이동합니다.

![건물별보기 북마크](https://user-images.githubusercontent.com/87303406/207538534-b3abaeee-b9af-417e-8ba1-9b78c40c0904.png)
- 건물 이름 우측에 위치한 `별 이미지`를 클릭하여 해당 건물을 `즐겨찾기`에 등록, 해제합니다.

### 내 주변 보기 메인화면
![내주변보기 메인화면](https://user-images.githubusercontent.com/87303406/207539363-762aba6b-8b4c-40d2-84eb-24dd3c47e7fd.png)
- 화면 중앙의 지도에서 원하는 장소를 탐색합니다.
- 원하는 장소에 대한 정보가 없다면 클릭하여 정보를 추가합니다.
- 원하는 장소에 대한 마커가 있다면 클릭하여 해당 장소의 상세페이지로 이동합니다.

### 내 주변 보기 정보추가화면
![내주변보기 정보추가화면](https://user-images.githubusercontent.com/87303406/207542974-d99a4b51-a79f-411f-a1cd-c559a47e7d41.png)
- 관리자가 제공하는 양식에 맞게 배리어 프리 정보를 저장합니다.
- 만일 해당 배리어 프리 정보와 관련된 사진이 있다면 첨부할 수 있습니다.

### 내 주변 보기 세부화면
![내주변보기 세부화면](https://user-images.githubusercontent.com/87303406/207543337-fa5374a7-89df-49d2-903a-68c252e06e40.png)
- 화면 중앙의 메인 컨텐츠 부분에서 스크롤을 내리며 해당 장소의 배리어 프리 정보를 확인합니다.
- 좌측 네비게이션바를 클릭하여 해당 부분으로 점프할 수 있습니다.
- 건물별 보기 상세페이지와 동일하게 즐겨찾기 기능을 사용할 수 있습니다.

![내주변보기 커뮤니티](https://user-images.githubusercontent.com/87303406/207543789-d38c46bd-5eab-4ba3-806b-dbd5a50d6497.png)
- 세부 페이지 하단에 위치한 글 작성하기 버튼을 통해 커뮤니티 기능을 이용합니다.
- 작성자는 클라이언트 고유 IP주소로 나타나며 작성 내용이 누적되어 컨텐츠 화면에 나타납니다.

### 즐겨찾는 장소
![북마크](https://user-images.githubusercontent.com/87303406/207545272-37539f28-596c-48f7-8dde-03268e04e535.png)
- 세부 페이지에서 즐겨찾기한 장소들을 확인합니다.
- 별 이모티콘을 클릭하여 해당 건물을 즐겨찾기에서 해제할 수 있습니다.

---

## __사용한 기술 스택__
### Front-end
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>
### Back-end
<img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat&logo=Amazon AWS&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat&logo=Amazon S3&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=SQLite&logoColor=white"/>