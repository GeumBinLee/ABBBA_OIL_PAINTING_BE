</br>
<p align="center"><img width="671" alt="Screen Shot 2022-11-28 at 10 15 30 AM" src="https://user-images.githubusercontent.com/18550082/204172506-4d73abb6-f2cc-4a5c-9655-856d9465899a.png"></p>
</br>

## Marvel Pics
</br>

- Style-Transfer-pytorch([A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)) 모델을 이용하여 이미지를 변환하고, 그 이미지를 확인할 수 있는 웹 서비스
- 제작 기간: 2022.11.22 ~ 2022.11.28
- Team 개발 노션: [https://www.notion.so/b7bf50eceff243a2b348f766d76098cb](https://www.notion.so/b7bf50eceff243a2b348f766d76098cb)
- FE Repository Info: [https://github.com/GeumBinLee/ABBBA_OIL_PAINTING_FE](https://github.com/GeumBinLee/ABBBA_OIL_PAINTING_FE)

</br></br>

#### **프로젝트 개요**

1. 프로젝트와 팀 소개
    
    Mockup & API & DB Modeling
    
2. 프로젝트 주요 기능
</br></br></br></br>

>### 프로젝트와 팀 소개

마블의 내 최애가 그려주는 나만의 사진!</br>
좋아하는 캐릭터를 선택하고 사용자가 변환하고 싶은 사진을 업로드하면 캐릭터의 스타일대로 사진을 변화시켜줍니다. 
</br></br>
****저희는 스파르타코딩클럽 내일배움캠프 3기 5인으로 구성된 팀입니다.****
|**김민규**|오민규|윤민성|윤장미|이금빈|
|:---:|:---:|:---:|:---:|:---:|
|Contact: [:electric_plug:](https://kmg0485.tistory.com/)|Contact: [:bulb:](https://dhalsrbbbbbbb.tistory.com/)|Contact: [:computer:](https://tweakycoding.tistory.com/)|Contact: [:sunglasses:](https://velog.io/@r5zyoon)|Contact: [:sparkling_heart:](https://lgb9811.tistory.com/)|
</br>
</br></br>

>### Figma mock-up
![Untitled](https://user-images.githubusercontent.com/18550082/204173260-8fda2295-a6d9-4099-9192-5eec3df8bb6e.png)
</br></br></br>

>### API
#### 수정 완료된 명세 이미지만 첨부하시면 됩니다.
</br></br></br>


>### DB Modeling
<img width="1346" alt="Screen Shot 2022-11-28 at 12 53 41 PM" src="https://user-images.githubusercontent.com/18550082/204190643-ce19efb7-2afd-43aa-baf3-6f41d89d8045.png"></br></br></br>
</br></br></br>


>### 프로젝트 주요 기능

#### Sign-up/Sign-in

- 회원가입한 사용자만 서비스를 이용할 수 있습니다. 이메일, 닉네임, 비밀번호 정보를 입력하여 회원가입을 할 수 있으며 이미 사용중인 이메일은 가입할 수 없고 비밀번호 조건을 맞추어야만 회원가입이 가능합니다.
- 이메일과 비밀번호로 로그인할 수 있습니다. 입력한 비밀번호가 정확한지 체크합니다.</br>
<img width="320" alt="Screen Shot 2022-11-28 at 9 54 46 AM" src="https://user-images.githubusercontent.com/18550082/204173364-55f5e57f-2493-4d06-a517-ea289149ed67.png"> <img width="320" alt="Screen Shot 2022-11-28 at 9 55 06 AM" src="https://user-images.githubusercontent.com/18550082/204173371-5e4fa89e-2a2a-414b-b4d9-3e2076eec645.png">

</br>

#### 이미지 변환 페이지

- 왼쪽 이미지 창에서 좋아하는 캐릭터를 선택하고 변환하고 싶은 이미지를 업로드합니다.
- Convert 버튼을 클릭하면 style_transfer 모델 실행, 좋아하는 캐릭터에 지정되어 있는 스타일에 맞춰 이미지가 변환됩니다.</br>
<img width="320" alt="Screen Shot 2022-11-28 at 12 39 48 PM" src="https://user-images.githubusercontent.com/18550082/204189261-0b5026c9-f63f-4a65-95cb-4e557040b994.png"> <img width="320" alt="Screen Shot 2022-11-28 at 12 40 13 PM" src="https://user-images.githubusercontent.com/18550082/204189274-e474be42-7202-4ee2-b48d-03fcbd5e492f.png">
</br>

#### 문의사항

- 게시글 CRUD를 문의사항으로 구현했습니다.
- 가입한 사용자는 문의사항과 문의사항 내 댓글을 작성하고 수정할 수 있습니다.</br>
<img width="320" alt="Screen Shot 2022-11-28 at 10 36 07 AM" src="https://user-images.githubusercontent.com/18550082/204173559-dcd5cb2d-b485-4de6-b52f-3c13f884ef5f.png"> <img width="320" alt="Screen Shot 2022-11-28 at 10 36 20 AM" src="https://user-images.githubusercontent.com/18550082/204173562-cf023c3f-0b77-4fe6-8699-16b7829cef1f.png">
</br>

#### 마이 프로필

- 로그인한 사용자는 프로필 페이지에서 사용자가 작성한 글과 변환했던 이미지를 모아볼 수 있습니다.
</br>

#### 메인 페이지

<img width="320" alt="Screen Shot 2022-11-28 at 10 00 37 AM" src="https://user-images.githubusercontent.com/18550082/204173747-32490d64-dbd1-43fc-9dbc-d9c8b1feb49d.png"> <img width="320" alt="Screen Shot 2022-11-28 at 10 00 54 AM" src="https://user-images.githubusercontent.com/18550082/204173750-56d434eb-ee57-4be0-9743-96bfab6240d7.png"> <img width="320" alt="Screen Shot 2022-11-28 at 10 01 14 AM" src="https://user-images.githubusercontent.com/18550082/204173754-60a6da93-de64-4d00-9278-3c9b731449e3.png">
</br>


