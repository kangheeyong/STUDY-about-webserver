# simple FCM

# 간단한 사용 방법
- firebase-messaging-sw.js
- index.html
- send_message.py
### 1. firebase에서 프로젝트 설정 -> 일반
firebaseConfig 값을 `firebase-messaging-sw.js`와 `index.html`에 넣어 주세요.
![스크린샷 2021-04-18 오후 6 15 53](https://user-images.githubusercontent.com/18637774/115140499-94e9d380-a072-11eb-8855-4a1fae907c6e.png)

### 2. liveserver로 띄우면 아래와 같이 떠야함
![스크린샷 2021-04-18 오후 6 15 08](https://user-images.githubusercontent.com/18637774/115140501-96b39700-a072-11eb-9c26-3244c75c4464.png)

### 3. 프로젝트 설정 -> 클라우드 메시징
key 값을 `.serviceAccountKey.json`로 저장
![스크린샷 2021-04-18 오후 6 20 13](https://user-images.githubusercontent.com/18637774/115140555-d8dcd880-a072-11eb-949c-72f9294df924.png)

### 4. 브라우저에서 얻은 토큰값을 `send_message.py`에 넣어주고 실행
<img width="895" alt="스크린샷 2021-04-18 오후 6 29 22" src="https://user-images.githubusercontent.com/18637774/115140789-07a77e80-a074-11eb-9847-bd859396de0b.png">
