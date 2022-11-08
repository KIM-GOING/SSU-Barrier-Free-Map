template 경로
    templates/campus/

url 맵핑

    기본(인덱스)
        url : xxx/campus
        campus정보 campus_list에 담아 넘겨줌

    상세페이지
        url : xxx/campus/id
        campus 통해 해당 정보만 넘겨줌


campus
    building_name
    bottom_floor
    top_floor
    building_detail
    location --> 지금은 구현x
    barrier_free_info -----------> BarierFreeInfo
                                        elevator_count
                                        elevator_detail
                                        elevator_img

                                        entrance_form
                                        entrance_ramp
                                        entrance_braille
                                        entrance_detail
                                        entrance_img

                                        restroom_floor
                                        restroom_detail
                                        restroom_image

                                        parking_count
                                        parking_detail
                                        parking_img
이렇게 접근 가능

학교 정보는 사용자가 수정할 필요 없어서 생성하는 거는 안만들었음
일단 장고admin을 통해서만 수정 가능